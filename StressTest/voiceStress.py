import json
import time
import sys
import os
import threading
import random
import traceback
from pprint import pprint
from lib import voicelib
# server = '35.234.17.150'
server = 'testing-api.xtars.com'
loginDic = {}
roomDic = {}
voiceDic = {}

def job (userInfo, userType):
    voice = voicelib.voice(server, userInfo, roomDic[str(userInfo['roomId'])], userInfo['roomId'])
    try:
        voice.on_connect()
    except Exception as err:
        print('get Error: ', err)
    finally:
        del voice
    

def main(beg, end, num):
    threadList = []    
    if beg <= 20:
        for i in range(beg, end):
            account = 'broadcaster' + str(i).zfill(3)
            if voiceDic.get(account):
                threadList.append(threading.Thread(target=job, args=(voiceDic[account], voiceDic[account]['idType'], )))                
    for i in range(beg, end):
        account = 'guest' + str(999 + i).zfill(4)
        loginDic[account]['roomId'] = random.randint(1, num) if num > 1 else 1
        threadList.append(threading.Thread(target=job, args=(loginDic[account], loginDic[account]['idType'], )))
    try:
        for p in threadList:
            p.start()
    except Exception as err:
        print('Process abnormal %s' % err)
        traceback.print_exc()
    finally:
        for p in threadList:
            p.join()
        print('Process end.')

if __name__ == '__main__':
    if os.path.isfile('loginInfo.txt'):
        with open('loginInfo.txt') as json_file:
            loginDic = json.load(json_file)
    if os.path.isfile('adminList.txt'):
        with open('adminList.txt') as json_file:
            roomDic = json.load(json_file)
    if os.path.isfile('voiceAdmin.txt'):
        with open('voiceAdmin.txt') as json_file:
            voiceDic = json.load(json_file)
    if len(sys.argv) != 4:
        print('請輸入測試帳號起迄值及聲聊房數, ', sys.argv)
        sys.exit(1)
    else:
        accountBeg = int(sys.argv[1])
        accountEnd = int(sys.argv[2])
        chatNum = int(sys.argv[3])
        main(accountBeg, accountEnd, chatNum)