import asyncio
import websockets
import requests
import time
import sys
import random
import traceback
import orjson
import logging
import datetime
from pprint import pprint
from datetime import datetime

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()
logging.basicConfig(level=logging.INFO,
	format='[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt='%Y%m%d %H:%M:%S',
)

async def joinRoom(ws, roomInfo, sNum):
    refStr = str(int(time.time()))
    joinRoom = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'vc_room:' + roomInfo[sNum]['roomId'],
        'event': 'phx_join',
        'payload': {'password': ''}
    }
    await ws.send(orjson.dumps(joinRoom))
    logging.info('join room(%s)'%roomInfo[sNum]['roomId'])
    return

async def leaveRoom(ws, roomInfo, sNum):
    refStr = str(int(time.time()))
    leaveRoom = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'vc_room:' + roomInfo[sNum]['roomId'],
        'event': 'phx_leave',
        'payload': {}
    }
    await ws.send(orjson.dumps(leaveRoom))
    logging.info('leave room(%s)'%roomInfo[sNum]['roomId'])
    return

async def sendMsg(ws, roomInfo, sNum):
    refStr = str(int(time.time()))
    msgStr = '現在時間-' + datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    leaveRoom = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'vc_room:' + roomInfo[sNum]['roomId'],
        'event': 'message',
        'payload': {'content': msgStr}
    }
    await ws.send(orjson.dumps(leaveRoom))
    return
    
async def sendGift(ws, roomInfo, sNum):
    giftList = ['bfda0320-9c3e-4d95-9abd-76222386b69d', '425d0f5f-5f93-4b23-b1cb-1e2526c02e8c']
    refStr = str(int(time.time()))
    giftStr = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'vc_room:' + roomInfo[sNum]['roomId'],
        'event': 'gift',
        'payload': {
            'giftId': giftList[random.randint(0, 1)], 
            'targetUserId': roomInfo[sNum]['masterId'], 
            'count': 1
        }
    }
    await ws.send(orjson.dumps(giftStr))
    return

async def pinFun(ws):
    refStr = str(int(time.time()))
    ping = {
        'ref': refStr,
        'join_ref': refStr, 
        'topic': 'phoenix',
        'event': 'heartbeat',
        'payload': {}
    }
    await ws.send(orjson.dumps(ping))
    return

async def botJob(token, nonce, roomInfo):
    sNum = random.randint(0, len(roomInfo) - 1) if len(roomInfo) > 1 else 0
    connectStr = 'wss://%s/socket/websocket?token=%s&nonce=%s'%(roomInfo[sNum]['socketDomain'], token, nonce)
    logging.info(connectStr)
    try:
        await asyncio.sleep(random.randint(2, 5))
        ws = await websockets.connect(connectStr, ping_interval=None)
        await joinRoom(ws, roomInfo, sNum)
        testTimes = 0  
        connected = True  
        while connected:
            k = int(random.random() * 200)
            try:
                if k < 25:
                    await leaveRoom(ws, roomInfo, sNum)
                    await asyncio.sleep(2)
                    await joinRoom(ws, roomInfo, sNum)
                elif k in (60, 120, 180):
                    await sendMsg(ws, roomInfo, sNum)
                elif k == 75:
                    await sendGift(ws, roomInfo, sNum)
                else:
                    await pinFun(ws)
                    await asyncio.sleep(45)
                testTimes += 1
                if testTimes > 10:
                    await leaveRoom(ws, roomInfo, sNum)
                    break
            except Exception as e1:
                connected = False  
                while not connected:  
                    try:  
                        sNum = random.randint(0, len(roomInfo) - 1) if len(roomInfo) > 1 else 0
                        connectStr = 'wss://%s/socket/websocket?token=%s&nonce=%s'%(roomInfo[sNum]['socketDomain'], token, nonce)
                        ws = await websockets.connect(connectStr, ping_interval=None)
                        await joinRoom(ws, roomInfo, sNum)
                        logging.error(token + ' reconnect success')
                        connected = True  
                    except Exception as e2: 
                        logging.error(token + ' reconnect failed try again')
                        await asyncio.sleep(3)    
    except Exception as e:
        logging.error('Exception: ', e)
    finally:
       await ws.close()
       logging.info(token + ' connection close')

def getRoomInfo(token, nonce):
    prefix = 'staging-api.xtars.com'
    rList = []
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': token, 'X-Auth-Nonce': nonce}
    for i in range(10, 11):
        url = 'https://%s/api/v2/identity/voiceChat/%s'%(prefix, str(i))
        res = requests.get(url, headers=header)
        result = orjson.loads(res.text)
        pprint(result)
        rList.append(
            {
                'roomId': str(result['data']['id']),
                'masterId': result['data']['masterId'],
                'socketDomain': result['data']['socketDomain']
            }
        )
    # pprint(rList)
    return rList

def main():
    taskList = []    
    beg = int(sys.argv[1])
    end = int(sys.argv[2])
    data = [line.strip() for line in open("./token.data", 'r')]
    token, nonce = data[0].split(',', 1)
    roomInfoList = getRoomInfo(token, nonce)
    # pprint(roomInfoList)
    for i in range(beg, end):
        token, nonce = data[i].split(',', 1)
        task = loop.create_task(botJob(token, nonce, roomInfoList))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
        # loop.run_until_complete(asyncio.sleep(2.0))
    except Exception as e:
        logging.error('main function get exception: ', e)
        traceback.print_exc()
    finally:
        loop.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        logging.info('請輸入測試帳號起迄值及聲聊房數, ', sys.argv)
        sys.exit(1)
    else:
        logging.info('run main')
        main()
