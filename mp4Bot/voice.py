import asyncio
import websockets
import time
import random
import orjson
import logging

logging.basicConfig(level=logging.DEBUG,
	format='[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt='%Y%m%d %H:%M:%S',
)


async def job(ws, roomId, refStr, event, body, token, times):
    action = {
        'ref': refStr,
        'join_ref': refStr, 
        'topic': 'vc_room:' + str(roomId),
        'event': event,
        'payload': body
    }
    await ws.send(orjson.dumps(action))
    logging.info('who: %s  event: %s  execute: %d'%(token, event, times))
    return

async def createConnection(token, nonce, roomInfo):
    sNum = random.randint(0, len(roomInfo) - 1) if len(roomInfo) > 1 else 0
    connectStr = 'wss://%s/socket/websocket?token=%s&nonce=%s'%(roomInfo[sNum]['socketDomain'], token, nonce)
    ws = await websockets.connect(connectStr, ping_interval=None)
    return sNum, ws

async def roomInOut(token, nonce, roomInfo):
    testTimes = 0  
    try:
        sNum, ws = await createConnection(token, nonce, roomInfo)
        refStr = str(int(time.time()))
        await asyncio.sleep(random.randint(3, 10))
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
                    sNum, ws = await createConnection(token, nonce, roomInfo)
                    refStr = str(int(time.time()))
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {}, token, testTimes) 
                elif (k >= 70 and k < 85) or (k >= 170 and k < 185):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {'action': 'reconnect'}, token, testTimes) 
                elif k == 95:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': '5f0bb976-0bc7-459f-8a6a-67ee0b6e7758', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes)
                elif k in (33, 188):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': '728e32fa-96a1-43a0-a493-56997ea30bed', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes)
                elif k in (44, 144):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'gift', {'giftId': '3fb4eafc-12ad-4af5-9249-9680df60635e', 'targetUserId': roomInfo[sNum]['masterId'], 'count': 1}, token, testTimes)
                elif k in (99, 197):
                    secStay = str(int(time.time() - int(refStr)))
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'message', {'content': '我在房內待了%s秒'%secStay}, token, testTimes)
                else:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'ping', {}, token, testTimes) 
                if testTimes > 10:
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
                        sNum, ws = await createConnection(token, nonce, roomInfo)
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
