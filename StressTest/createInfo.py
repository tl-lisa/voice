import json
import time
import sys
import requests
import os
import paramiko
from hashids import Hashids
from pprint import pprint
import dbConnect

env = 'https://testing-api.xtars.com'
db = 'testing-api.xtars.com'
# env = 'http://35.234.17.150'
# db = '35.234.17.150'
header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}

def clearCache(hostAddr):
    keyfile = './lisakey'  
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostAddr, username='lisa', key_filename=keyfile)
    cmd = 'redis-cli flushdb;'
    ssh.exec_command(cmd)
    ssh.close()

def getTrueLoveId(tureLoveId):
    hashids = Hashids(
            salt = 'ChktKbMtT7bG6h87PbQ7',
            min_length=8,
            alphabet="ACDEFGHJKLMNPRSTWXY35679",
    )
    return hashids.encode(tureLoveId)

def apiFunction(prefix, head, apiName, way, body):
    resquestDic = {
        'post':requests.post,
        'put':requests.put,
        'patch':requests.patch, 
        'get':requests.get, 
        'delete':requests.delete
    }
    url = prefix + apiName  
    if body:
        head['Content-Type'] = 'application/json'
        res1 = resquestDic[way](url, headers=head, json=body)
    else: 
        if head.get('Content-Type'): del head['Content-Type']          
        res1 = resquestDic[way](url, headers=head)
    print(head)
    print('url = %s, method= %s'% (url, way))  
    print(body) if body else print('no body')
    pprint('status code = %d'%res1.status_code)
    pprint(json.loads(res1.text))
    return res1 

def user_login(account):
    url = env + '/api/v2/identity/auth/login'
    body = {
        "account": account,
        "password": '123456',
        "pushToken": ''
    }
    requests.post(url, json=body)
    time.sleep(1)
    return

def accountLogin():   
    print('account logging')
    for i in range(1, 5000):
        if i < 101: user_login('broadcaster' + str(i).zfill(3))
        user_login('guest' + str(999 + i).zfill(4))
        if i % 100 == 0: print('login account', 'guest' + str(999 + i).zfill(4))
    return

def createLoginInfo():
    print('create login file')
    sqlList = []
    loginDic = {}
    adminDic = {}
    roomDic = {}
    sqlStr  = "select login_id, id, token, nonce from identity "
    sqlStr += "where login_id like 'guest%' and length(login_id) = 9 "
    # sqlStr += "and login_id < 'track0101'"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    for i in dbResult:
        loginDic[i[0]] = {
            'id'    : i[1],
            'token' : i[2],
            'nonce' : i[3],
            'trueloveId': None,
            'roomId': None,
            'idType': 'audience',
            'seatId': None
        }
        sqlStr  = "INSERT INTO remain_points(remain_points, ratio, identity_id) VALUES ("
        sqlStr += "2000000, 4, '" + i[1] + "') ON DUPLICATE KEY "
        sqlStr += "UPDATE remain_points = 2000000, ratio = 4"
        sqlList.append(sqlStr)
    with open('loginInfo.txt', 'w') as outfile:
        json.dump(loginDic, outfile)
    dbConnect.dbSetting(db, sqlList)
    sqlStr  = "select i.login_id, i.id, i.token, i.nonce, i.truelove_id, va.voice_chat_room_id "
    sqlStr += "from identity i, voice_chat_admin va where i.id=va.live_master_id"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    j = 1
    for i in dbResult:
        adminDic[i[0]] = {
            'id'   : i[1],
            'token': i[2],
            'nonce': i[3],
            'trueloveId': getTrueLoveId(i[4]),
            'roomId': i[5],
            'idType': 'admin',
            'seatId': j
        }
        j+= 1
    sqlStr  = "select i.login_id, i.id, i.token, i.nonce, i.truelove_id, va.id "
    sqlStr += "from identity i, voice_chat_room va where i.id=va.master_id"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    for i in dbResult:
        adminDic[i[0]] = {
            'id'   : i[1],
            'token': i[2],
            'nonce': i[3],
            'trueloveId': getTrueLoveId(i[4]),
            'roomId': i[5],
            'idType': 'owner',
            'seatId': 0
        }
    with open('voiceAdmin.txt', 'w') as outfile:
        json.dump(adminDic, outfile)
    sqlStr  = "(select id, master_id from voice_chat_room order by id) union "
    sqlStr += "(select voice_chat_room_id, live_master_id from voice_chat_admin order by voice_chat_room_id)"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    for i in dbResult:
        if i[0] in roomDic:
            roomDic[i[0]].append(i[1])
        else:
            roomDic[i[0]] = [i[1]] 
    with open('adminList.txt', 'w') as outfile:
        json.dump(roomDic, outfile)
    return

def createVoiceOwner(lisa, account, roomId):
    print('create voice owner')
    header['X-Auth-Token'] = lisa[0]
    header['X-Auth-Nonce'] = lisa[1]
    sqlStr = "select id, token, nonce from identity where login_id = '" + account + "'"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    apiName = '/api/v2/backend/voiceChat'
    body = {
        'typeId':1,
        'masterId': dbResult[0][0], 
        'title': account+'的聲聊間',
        'description': '快來加入'+account+'的聲聊間吧！',
        'password': '',
        'streamId':[
            'voiceChat_'+ str(roomId)+'_1',
            'voiceChat_'+ str(roomId)+'_2',
            'voiceChat_'+ str(roomId)+'_3',
        ]
    }
    apiFunction(env, header, apiName, 'post', body)
    return dbResult[0][1], dbResult[0][2]

def createVoiceAdmin(header, roomId, account):
    print('create voice admin')
    sqlStr = "select id from identity where login_id = '" + account + "'"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    apiName = '/api/v2/liveMaster/voiceChat/admin'
    body = {
        'roomId': roomId,
        'userId': dbResult[0][0]
    }
    apiFunction(env, header, apiName, 'post', body)

def clearVoice(db):
    print('clear voice room')
    sqlList = []
    tableList = ['voice_chat_gift_history', 'voice_chat_admin', 'voice_chat_history', 'voice_chat_stream']
    for i in tableList:
        sqlStr = "TRUNCATE TABLE " + i
        sqlList.append(sqlStr)   
    deleteList = ['voice_chat_room'] 
    for tableName in deleteList:
        sqlList.append("delete from " + tableName)
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def createVoiceRoom(lisa):
    clearVoice(db)
    clearCache(db)
    for i in range(5):
        ownerAccount = 'broadcaster' + str(1 + i * 5).zfill(3)
        header['X-Auth-Token'], header['X-Auth-Nonce'] = createVoiceOwner(lisa, ownerAccount, i+1)
        for j in range(4):
            adminAccount = 'broadcaster' + str(1 + i * 5 + j).zfill(3)
            createVoiceAdmin(header, i+1, adminAccount)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        accountLogin()
    elif sys.argv[1] == '2':
        sqlStr = "select token, nonce from identity where login_id = 'tl-lisa'"
        dbResult = dbConnect.dbQuery(db, sqlStr)
        lisa = [dbResult[0][0], dbResult[0][1]]
        pprint(lisa)
        createVoiceRoom(lisa)
    elif sys.argv[1] == '3':
        createLoginInfo()
    else:
        print('get step is : ', sys.argv[1])
    
