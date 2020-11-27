import json
import time
import sys
import requests
import os
from pprint import pprint
from . import dbConnect

env = 'https://testing-api.xtars.com'
db = 'testing-api.xtars.com'

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
    loginDic = {}
    sqlStr  = "select login_id, id, token, nonce from identity "
    sqlStr += "where login_id like 'track%' and length(login_id) < 10"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    for i in dbResult:
        loginDic[i[0]] = {
            'id': i[1],
            'token': i[2],
            'nonce': i[3]
        }
    sqlStr  = "select login_id, id, token, nonce from identity "
    sqlStr += "where login_id like 'broadcaster%' and length(login_id) = 14"
    dbResult = dbConnect.dbQuery(db, sqlStr)
    for i in dbResult:
        loginDic[i[0]] = {
            'id': i[1],
            'token': i[2],
            'nonce': i[3]
        }

    with open('loginInfo.txt', 'w') as outfile:
        json.dump(loginDic, outfile)
    return

if __name__ == '__main__':
    accountLogin()
    createLoginInfo()