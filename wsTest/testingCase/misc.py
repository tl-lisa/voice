import json
import requests
import paramiko
from hashids import Hashids
from pprint import pprint
from . import dbConnect

def apiFunction(prefix, head, apiName, way, body):
    resquestDic = {
        'post':requests.post,
        'put':requests.put,
        'patch':requests.patch,
        'get':requests.get,
        'delete':requests.delete}
    url = prefix + apiName
    if body:
        head['Content-Type'] = 'application/json'
        res1 = resquestDic[way](url, headers=head, json=body)
    else:
        if head.get('Content-Type'):
            del head['Content-Type']
        res1 = resquestDic[way](url, headers=head)
    # print(head)
    # print('url = %s, method= %s'% (url, way))
    # print(body) if body else print('no body')
    # pprint('status code = %d'%res1.status_code)
    # pprint(json.loads(res1.text))
    return res1

def clearCache(hostAddr):
    keyfile = './lisakey'  
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostAddr, username='lisa', key_filename=keyfile)
    cmd = 'redis-cli flushdb;'
    ssh.exec_command(cmd)
    ssh.close()

def changeRole(prefix, token, nonce, idList, roleType):
    #5:一般用戶；4:直播主
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}
    header['X-Auth-Token'] = token
    header['X-Auth-Nonce'] = nonce
    url = '/api/v2/backend/user/role'
    body = {'ids': idList, 'role': roleType}
    res = apiFunction(prefix, header, url, 'patch', body)
    return res

def getDicKeys(dd, keyList):  
    for keys, values in dd.items():
        keyList.append(keys)
        if type(values) == dict:
            getDicKeys(values, keyList)
        elif all([type(values) == list, values]):
            if type(values[0]) == dict: getDicKeys(values[0], keyList)
        else:
            continue          
    return 

def getTrueLoveId(tureLoveId):
    hashids = Hashids(
            salt = 'ChktKbMtT7bG6h87PbQ7',
            min_length=8,
            alphabet="ACDEFGHJKLMNPRSTWXY35679",
    )
    return hashids.encode(tureLoveId)

def add_test_data(env, test_parameter, masterPrefix, beg, end, fillzero):    
    if env == 'QA':
        test_parameter['prefix'] = 'http://35.234.17.150'
        test_parameter['db'] = '35.234.17.150'
    elif env == 'test':
        test_parameter['prefix'] = 'http://testing-api.xtars.com.tw'
        test_parameter['db'] = 'testing-api.xtars.com.tw'
    sqlStr  = "select login_id, id, token, nonce, truelove_id, nickname from identity "
    sqlStr += "where login_id in ('"
    for i in range(beg, end):
        account = masterPrefix + str(i).zfill(fillzero)
        sqlStr += account + "', '" if i < (end - 1) else account + "')"
    result = dbConnect.dbQuery(test_parameter['db'], sqlStr)
    for i in result:
        if all([i[2], i[3]]):
            test_parameter[i[0]] = {
                'id': i[1],
                'token': i[2],
                'nonce': i[3],
                'trueloveId': getTrueLoveId(i[4]),
                'nickname': i[5]
            }
        else:
            body = {
                'account': i[0],
                'password': '123456',
                'pushToken': ''}
            header = {'Content-Type': 'application/json', 'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}
            res = apiFunction(test_parameter['prefix'],header, '/api/v2/identity/auth/login', 'post', body)
            resText = json.loads(res.text)
            test_parameter[i[0]] = {
                'id': i[1],
                'token': resText['data']['token'],
                'nonce': resText['data']['nonce'],
                'trueloveId': getTrueLoveId(i[4]),
                'nickname': i[5]
            }
    return

def get_test_data(env, test_parameter, masterPrefix, masterCount, beg, end, fillzero):    
    if env == 'QA':
        test_parameter['prefix'] = 'http://35.234.17.150'
        test_parameter['db'] = '35.234.17.150'
    elif env == 'test':
        test_parameter['prefix'] = 'http://testing-api.xtars.com.tw'
        test_parameter['db'] = 'testing-api.xtars.com.tw'
    test_parameter['errAccount'] = {'token': 'aa24385', 'nonce': 'noceiw'}
    sqlStr  = "select login_id, id, token, nonce, truelove_id, nickname from identity "
    sqlStr += "where login_id in ('tl-lisa', 'lv000', 'lv001', 'lv002', '"
    for i in range(beg, end):
        account = 'track' + str(i).zfill(4)
        sqlStr += account + "', '" if i < (end - 1) else account + "')"
        if masterCount > 0:
            account = masterPrefix + str(i).zfill(fillzero)
            sqlStr += account + "', '"
            masterCount -= 1
    result = dbConnect.dbQuery(test_parameter['db'], sqlStr)
    for i in result:
        if all([i[2], i[3]]):
            test_parameter[i[0]] = {
                'id': i[1],
                'token': i[2],
                'nonce': i[3],
                'trueloveId': getTrueLoveId(i[4]),
                'nickname': i[5]
            }
        else:
            body = {
                'account': i[0],
                'password': '123456',
                'pushToken': ''}
            header = {'Content-Type': 'application/json', 'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}
            res = apiFunction(test_parameter['prefix'],header, '/api/v2/identity/auth/login', 'post', body)
            resText = json.loads(res.text)
            test_parameter[i[0]] = {
                'id': i[1],
                'token': resText['data']['token'],
                'nonce': resText['data']['nonce'],
                'trueloveId': getTrueLoveId(i[4]),
                'nickname': i[5]
            }

    #pprint(test_parameter)
    sqlStr  = "INSERT INTO remain_points(remain_points, ratio, identity_id) VALUES ("
    sqlStr += "200000, 4, '" + test_parameter['track0020']['id'] + "') ON DUPLICATE KEY "
    sqlStr += "UPDATE remain_points = 20000, ratio = 4"
    sqlStr1  = "UPDATE remain_points SET remain_points = 100000 WHERE identity_id = "
    sqlStr1 += "'" + test_parameter['track0019']['id'] + "'"
    sqlStr2 = "TRUNCATE TABLE user_blocks"
    sqlStr3 = "TRUNCATE TABLE user_banned"
    sqlStr4 = "TRUNCATE TABLE fans"
    dbConnect.dbSetting(test_parameter['db'], [sqlStr, sqlStr1, sqlStr2, sqlStr3, sqlStr4])
    return

