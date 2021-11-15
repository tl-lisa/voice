import asyncio
import websockets
import requests
import time
import sys
import random
import traceback
import orjson
import logging
#import datetime
from pprint import pprint
from datetime import datetime, timedelta

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()
#log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
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
        'payload': {}
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
    nowis = datetime.now() + timedelta(hours=8)
    msgStr = '現在時間-' + nowis.strftime("%Y/%m/%d %H:%M:%S")  
    leaveRoom = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'vc_room:' + roomInfo[sNum]['roomId'],
        'event': 'message',
        'payload': {'content': msgStr}
    }
    await ws.send(orjson.dumps(leaveRoom))
    return
    
async def sendGift(ws, roomInfo, sNum, giftId):
    countList = [1, 2, 4, 6]
    if giftId == 'ddc2eadf-e40f-4e33-896f-764674366dd9':
        counts = random.randint(0, 3)
    else:
        counts = 0
    refStr = str(int(time.time()))
    giftStr = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'vc_room:' + roomInfo[sNum]['roomId'],
        'event': 'gift',
        'payload': {
            'giftId': giftId, 
            'targetUserId': roomInfo[sNum]['masterId'], 
            'count': countList[counts]
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
        ws = await websockets.connect(connectStr, ping_interval=None)
        await asyncio.sleep(random.randint(2, 5))
        await joinRoom(ws, roomInfo, sNum)
        testTimes = 0  
        connected = True  
        while connected:
            k = int(random.random() * 200)
            try:
                if k <= 10:
                    await leaveRoom(ws, roomInfo, sNum)
                    await asyncio.sleep(2)
                    await joinRoom(ws, roomInfo, sNum)
                elif k in (30, 60, 120, 180):
                    await sendMsg(ws, roomInfo, sNum)
                elif k in (55, 100, 110, 125) :
                    await sendGift(ws, roomInfo, sNum, 'ddc2eadf-e40f-4e33-896f-764674366dd9')
                elif k in (75, 165) :
                    await sendGift(ws, roomInfo, sNum, '1a51e630-3956-46e0-8bb9-e334f06b5634') #10萬點
                else:
                    await asyncio.sleep(45)
                    await pinFun(ws)
                testTimes += 1
                if testTimes > 90:
                    await leaveRoom(ws, roomInfo, sNum)
                    break
            except Exception as e1:
                connected = False  
                retryTimes = 0
                while not connected:  
                    retryTimes += 1
                    try:  
                        sNum = random.randint(0, len(roomInfo) - 1) if len(roomInfo) > 1 else 0
                        connectStr = 'wss://%s/socket/websocket?token=%s&nonce=%s'%(roomInfo[sNum]['socketDomain'], token, nonce)
                        ws = await websockets.connect(connectStr, ping_interval=None)
                        await joinRoom(ws, roomInfo, sNum)
                        logging.error(token + ' reconnect success')
                        connected = True  
                    except Exception as e2: 
                        logging.error(token + ' reconnect failed try again')
                        if retryTimes > 10:
                            logging.error('reconnect over 10, exit loop')
                            break
                        else:
                            await asyncio.sleep(3)    
    except Exception as e:
        logging.error('Exception: ', e)
    finally:
       await ws.close()
       logging.info(token + ' connection close')

def getRoomInfo():
    prefix = 'testing-api.xtars.com'
    rList = []
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': 'guest1000', 'X-Auth-Nonce': 'guest1000'}
    for i in range(1, 3):
        url = 'https://%s/api/v2/identity/voiceChat/%s'%(prefix, str(i))
        res = requests.get(url, headers=header)
        result = orjson.loads(res.text)
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
    roomInfoList = getRoomInfo()
    for i in range(beg, end):
        token = 'guest' + str(999+i) 
        nonce = 'guest' + str(999+i)
        task = loop.create_task(botJob(token, nonce, roomInfoList))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
        loop.run_until_complete(asyncio.sleep(2.0))
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
