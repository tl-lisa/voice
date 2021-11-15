import asyncio
import websockets
import aiohttp
import time
import sys
import random
import orjson
import logging
# import datetime
from aiohttp import ClientError
from pprint import pprint
from datetime import datetime
from datetime import timedelta

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()
#log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
logging.basicConfig(level=logging.DEBUG,
	format='[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt='%Y%m%d %H:%M:%S',
)


async def getRoomInfo():
    rList = []
    roomInfo = []
    prefix = 'testing-api.xtars.com'
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': 'guest1000', 'X-Auth-Nonce': 'guest1000'}
    url = 'https://%s/api/v2/live/list/home/more'%(prefix)
    try:        
        await asyncio.sleep(2)
        async with aiohttp.request("GET", url, headers=header) as resp:
            if resp.status == 200:
                resp_body = await resp.text()
                if resp_body != "":
                    result = orjson.loads(resp_body)
                    # pprint(result)
                    for i in result['data']:
                        if all([i['socketType'] == 'web', i['type'] == 'liveRoom']):
                            if i['roomStatus'] == 1:
                                if not i['needPassword']:
                                    rList.append(i['roomId'])
                            else:
                                break
    except ClientError as err:
                logging.error(err, exc_info=True)
    for i in rList:
        url = 'https://%s/api/v2/room/info/%s'%(prefix, i)
        try:
            async with aiohttp.request("GET", url, headers=header) as resp:
                if resp.status == 200:
                    resp_body = await resp.text()
                    if resp_body != "":
                        result = orjson.loads(resp_body)
                        roomInfo.append(
                            {
                                'roomId': i, 
                                'masterId': result['data']['liveMasterId'],
                                'socketDomain': result['data']['socketDomain']
                            }
                        )
        except ClientError as err:
                    logging.error(err, exc_info=True)
    return roomInfo

async def createConnection(token, nonce):
    roomInfo = []
    getTimes = 0
    while getTimes <= 10:
        getTimes += 1
        roomInfo = await getRoomInfo()
        if len(roomInfo) == 0:
            logging.info('room list is empty, after 20 sec try again')
            await asyncio.sleep(20)
        else:
            break
    logging.info('get room: %s'%str(roomInfo))
    sNum = random.randint(0, len(roomInfo) - 1) if len(roomInfo) > 1 else 0
    connectStr = 'wss://%s/socket/websocket?token=%s&nonce=%s'%(roomInfo[sNum]['socketDomain'], token, nonce)
    # logging.info(connectStr)
    return await websockets.connect(connectStr, ping_interval=None), sNum, roomInfo

async def joinRoom(ws, roomInfo, sNum, token, testTimes):
    refStr = str(int(time.time()))
    joinRoom = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'live_room:' + roomInfo[sNum]['roomId'],
        'event': 'phx_join',
        'payload': {}
    }
    await ws.send(orjson.dumps(joinRoom))
    logging.info('%s join room(%s) at %d'%(token,roomInfo[sNum]['roomId'],testTimes))
    return

async def leaveRoom(ws, roomInfo, sNum, token, testTimes):
    refStr = str(int(time.time()))
    leaveRoom = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'live_room:' + roomInfo[sNum]['roomId'],
        'event': 'phx_leave',
        'payload': {}
    }
    await ws.send(orjson.dumps(leaveRoom))
    logging.info('%s leave room(%s) at %d'%(token, roomInfo[sNum]['roomId'],testTimes))
    return

async def sendMsg(ws, roomInfo, sNum, token, testTimes):
    refStr = str(int(time.time()))
    nowis = datetime.now() + timedelta(hours=8)
    msgStr = '現在時間-' + nowis.strftime("%Y/%m/%d %H:%M:%S")  
    leaveRoom = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'live_room:' + roomInfo[sNum]['roomId'],
        'event': 'message',
        'payload': {'content': msgStr}
    }
    await ws.send(orjson.dumps(leaveRoom))
    logging.info('%s send message at %d'%(token, testTimes))
    return

async def sendBarrage(ws, roomInfo, sNum, token, testTimes):
    refStr = str(int(time.time()))
    nowis = datetime.now() + timedelta(hours=8)
    msgStr = '現在時間-' + nowis.strftime("%Y/%m/%d %H:%M:%S")  
    barrage = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'live_room:' + roomInfo[sNum]['roomId'],
        'event': 'barrage',
        'payload': {
            'barrageId': 1, 
            'content': msgStr
        }
    }
    await ws.send(orjson.dumps(barrage))
    logging.info('%s send barrage at %d'%(token, testTimes))
    return

    
async def sendGift(ws, roomInfo, sNum, token, testTimes, giftId):
    countList = [1, 2, 4, 6]
    if giftId == 'f30dd819-116d-454c-b316-bcdc5255b171':
        counts = random.randint(0, 3)
    else:
        counts = 0
    refStr = str(int(time.time()))
    giftStr = {
        'ref': refStr, 
        'join_ref': refStr, 
        'topic': 'live_room:' + roomInfo[sNum]['roomId'],
        'event': 'gift',
        'payload': {
            'giftId': giftId, 
            'targetUserId': roomInfo[sNum]['masterId'], 
            'count': countList[counts]
        }
    }
    await ws.send(orjson.dumps(giftStr))
    logging.info('%s send gift at %d'%(token, testTimes))
    return

async def pinFun(ws, roomInfo, sNum, token, testTimes):
    refStr = str(int(time.time()))
    ping = {
        'ref': refStr,
        'join_ref': refStr, 
        'topic': 'live_room:' + roomInfo[sNum]['roomId'],
        'event': 'ping',
        'payload': {}
    }
    await ws.send(orjson.dumps(ping))
    logging.info('%s ping at %d'%(token, testTimes))
    return

async def botJob(token, nonce):
    ws, sNum, roomInfo = await createConnection(token, nonce)
    await asyncio.sleep(2)
    try:
        await joinRoom(ws, roomInfo, sNum, token, 0)
        testTimes = 0  
        connected = True  
        while connected:
            k = int(random.random() * 200)
            try:
                if k < 20:
                    await leaveRoom(ws, roomInfo, sNum, token, testTimes)
                    await ws.close()
                    logging.info(token + ' connect is closed')
                    await asyncio.sleep(3)
                    ws, sNum, roomInfo = await createConnection(token, nonce)
                    await joinRoom(ws, roomInfo, sNum, token, testTimes)
                    logging.info(token + ' join room again')
                elif k in (60, 120, 180):
                    await sendMsg(ws, roomInfo, sNum, token, testTimes)
                elif k in (80, 160):
                    await sendBarrage(ws, roomInfo, sNum, token, testTimes)
                elif k in (33, 99, 159, 199):
                    await sendGift(ws, roomInfo, sNum, token, testTimes, 'f30dd819-116d-454c-b316-bcdc5255b171')
                elif k in (77, 144):
                    await sendGift(ws, roomInfo, sNum, token, testTimes, 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60') #10萬點
                else:
                    await asyncio.sleep(45)
                    await pinFun(ws, roomInfo, sNum, token, testTimes)        
                testTimes += 1
                if testTimes > 80:
                    await leaveRoom(ws, roomInfo, sNum, token, testTimes)
                    logging.info('%s 已執行滿設定次數'%token)
                    connected = False 
            except Exception as e1:
                connected = False 
                retryTimes = 0 
                logging.error(token + ' get exception in while loop')
                logging.error('Exception: ', e1)
                while not connected:  
                    retryTimes += 1
                    try:  
                        ws, sNum, roomInfo = await createConnection(token, nonce)
                        await joinRoom(ws, roomInfo, sNum, token, testTimes)
                        logging.info(token + ' reconnect success')
                        connected = True  
                    except Exception as e2: 
                        logging.error(token + ' reconnect failed try again')
                        logging.error('Exception: ', e2)
                        await asyncio.sleep(3)
                        if retryTimes > 10:
                            logging.error(token + ' reconnect over 10, exit loop')
                            break
        logging.info('%s leave while loop'%token)
    except Exception as e:
        logging.error('Exception: ', e)
    finally:
       logging.info(token + ' connection close')
       await ws.close()

def main():
    taskList = []    
    beg = int(sys.argv[1])
    end = int(sys.argv[2])
    for i in range(beg, end):
        token = 'guest' + str(2999+i) 
        nonce = 'guest' + str(2999+i)
        task = loop.create_task(botJob(token, nonce))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        logging.error('main function get exception: ', e)
    finally:
        loop.close()
        logging.info('process finish')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        logging.info('請輸入測試帳號起迄值及聲聊房數, ', sys.argv)
        sys.exit(1)
    else:
        logging.info('run main')
        main()
