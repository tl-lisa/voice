import json
import time
import sys
import requests
import os
from hashids import Hashids
from pprint import pprint
from . import dbConnect

# env = 'https://testing-api.xtars.com'
# db = 'testing-api.xtars.com'
env = 'http://35.234.17.150'
db = '35.234.17.150'

def getTrueLoveId(tureLoveId):
    hashids = Hashids(
            salt = 'ChktKbMtT7bG6h87PbQ7',
            min_length=8,
            alphabet="ACDEFGHJKLMNPRSTWXY35679",
    )
    return hashids.encode(tureLoveId)

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
    #user login
    for i in range(1, 6001):
        account = 'track'
        if i < 10:
            account += '000' + str(i)
        elif i < 100:
            account += '00' + str(i)
        elif i < 1000:
            account += '0' + str(i+1)
        else:
            account += str(i+1)
        user_login(account)

    #master login
    for i in range(1, 101):
        account = 'broadcaster'
        if i < 10:
            account += '00' + str(i)
        elif i < 100:
            account += '0' + str(i)
        else:
            account += str(i+1)
        user_login(account)
    return

def createLoginInfo():
    sqlList = []
    loginDic = {}
    adminDic = {}
    sqlStr  = "select login_id, id, token, nonce from identity "
    sqlStr += "where login_id like 'track%' and length(login_id) < 10"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    for i in dbResult:
        loginDic[i[0]] = {
            'id'    : i[1],
            'token' : i[2],
            'nonce' : i[3],
            'trueloveId': getTrueLoveId(i[4]),
            'roomId': i[5],
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
    return

if __name__ == '__main__':
    accountLogin()
    createLoginInfo()