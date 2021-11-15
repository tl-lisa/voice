import asyncio
import websockets
import aiohttp
import time
import random
import orjson
import logging
from aiohttp import ClientError

logging.basicConfig(level=logging.DEBUG,
	format='[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt='%Y%m%d %H:%M:%S',
)


async def getRoomInfo():
    rList = []
    roomInfo = []
    masterList = [
        '9afc753b-af58-457c-bb87-13796aa958bf', 
        '0240eec3-2234-4315-b5fc-259b4144b4f3',
        '2b35fab0-5369-4add-a778-30801e9ee8b4',
        '59e7e953-3c5a-4d28-827e-902b356b1696'
    ]
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
                        if result['data']['liveMasterId'] in masterList:
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

async def createConnection(token, nonce, actionType):
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
    if actionType == 'RAT':
        return roomInfo
    else:
        return await websockets.connect(connectStr, ping_interval=None), sNum, roomInfo


async def job(ws, roomId, refStr, event, body, token, times):
    action = {
        'ref': refStr,
        'join_ref': refStr, 
        'topic': 'live_room:' + str(roomId),
        'event': event,
        'payload': body
    }
    await ws.send(orjson.dumps(action))
    logging.info('who: %s  event: %s  execute: %d'%(token, event, times))
    return

async def roomInOut(token, nonce):
    ws, sNum, roomInfo = await createConnection(token, nonce, 'InOut')
    await asyncio.sleep(random.randint(5,15))
    testTimes = 0  
    try:
        refStr = str(int(time.time()))
        await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {}, token, testTimes) 
        connected = True  
        while connected:
            testTimes += 1
            k = int(random.random() * 200)
            try:
                await asyncio.sleep(45)
                if k < 20:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_leave', {}, token, testTimes)
                    await ws.close()
                    await asyncio.sleep(random.randint(3,10))
                    ws, sNum, roomInfo = await createConnection(token, nonce, 'InOut')
                    refStr = str(int(time.time()))
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {}, token, testTimes) 
                elif (k >= 70 and k < 85) or (k >= 170 and k < 185):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {'action': 'reconnect'}, token, testTimes) 
                elif k == 25:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'barrage', {'barrageId': 2, 'content': '發了一個彈幕'}, token, testTimes) 
                elif k == 98:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': '5b1646be-1400-4837-ab2e-d55d9945f8bc', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes) 
                elif k in(33, 133):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': 'f522ae8a-88c9-428e-964a-f626a3a96ec8', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes) 
                elif k in(44, 144):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': 'dbe2c2c8-f9a5-4fa8-bfd8-10f2a1eb1246', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes) 
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': 'dbe2c2c8-f9a5-4fa8-bfd8-10f2a1eb1246', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes) 
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': 'dbe2c2c8-f9a5-4fa8-bfd8-10f2a1eb1246', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes) 
                elif k in(55, 155):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': '32f81979-b3a1-48d8-9dea-1f6a2a27f6b9', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes) 
                elif k in (99, 197):
                    secStay = str(int(refStr) - int(time.time()))
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'message', {'content': '我在房內待了 '+secStay+'秒'}, token, testTimes)
                else:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'ping', {}, token, testTimes)        
                if testTimes > 80:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'message', {'content': '執行次數已滿，結束連線囉 881'}, token, testTimes)
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_leave', {}, token, testTimes)
                    connected = False 
            except Exception as e1:
                connected = False 
                retryTimes = 0 
                logging.error(token + ' get exception in while loop')
                logging.error('Exception: ', e1)
                while not connected:  
                    retryTimes += 1
                    try:  
                        ws, sNum, roomInfo = await createConnection(token, nonce, 'InOut')
                        refStr = str(int(time.time()))
                        await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {}, token, testTimes) 
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
       await asyncio.sleep(30)
       await ws.close()
