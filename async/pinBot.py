import asyncio
import websockets
import json
import time
import sys
import os
import random
import traceback
from pprint import pprint
from datetime import datetime

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()

async def botJob(token, nonce):
    roomId = 1
    serverList = ['testing-api.xtars.com']
    sNum = random.randint(0, len(serverList) - 1) if len(serverList) > 1 else 0
    connectStr = 'ws://%s/socket/websocket?token=%s&nonce=%s'%(serverList[sNum], token, nonce)
    print(connectStr)
    ping = {
        'ref': None, 
        'join_ref': None, 
        'topic': 'phoenix',
        'event': 'heartbeat',
        'payload': {}
    }
    joinRoom = {
        'ref': str(int(time.time())), 
        'join_ref': str(int(time.time())), 
        'topic': 'vc_room:' + str(roomId),
        'event': 'phx_join',
        'payload': {}
    }

    try:
        await asyncio.sleep(random.randint(2, 5))
        ws = await websockets.connect(connectStr, ping_interval=None)
        await ws.send(json.dumps(joinRoom))   
        while 1:
            ping['ref'] = str(int(time.time()))
            ping['join_ref'] = str(int(time.time()))
            await ws.send(json.dumps(ping))
            await asyncio.sleep(30)
    except Exception as e:
        print('bot job get err: ', e)
        traceback.print_exc()
    finally:
       await ws.close()

def main():
    taskList = []    
    beg = int(sys.argv[1])
    end = int(sys.argv[2])
    chatNum = int(sys.argv[3])
    print('beg= ',beg, ' end= ', end)
    for i in range(beg, end):
        # loginDic = {}
        token = 'guest' + str(999+i) + 'token'
        nonce = 'guest' + str(999+i) + 'nonce'
        # loginDic = {
        #     'nickname': account,
        #     'token': account + 'token',
        #     'nonce': account + 'nonce',
        #     'idType': 'audience',
        #     'roomId': None,
        #     'ownerId': None,
        #     'id': None            
        # }
        # loginDic['roomId'] = random.randint(1, chatNum) if chatNum > 1 else 1
        task = loop.create_task(botJob(token, nonce))
        taskList.append(task)
    print('job add finish')
    try:
        loop.run_until_complete(asyncio.wait(taskList))
        loop.run_until_complete(asyncio.sleep(2.0))
    except Exception as e:
        print('main function get exception: ', e)
        traceback.print_exc()
    finally:
        loop.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('請輸入測試帳號起迄值及聲聊房數, ', sys.argv)
        sys.exit(1)
    else:
        print('run main')
        main()