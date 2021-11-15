import asyncio
import websockets
import aiohttp
import requests
import time
import sys
import random
import orjson
import logging
import dbConnect
from aiohttp import ClientError
from datetime import datetime
from datetime import timedelta

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()
#log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
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

async def pinFun(ws, refStr, token, times):
    ping = {
        'ref': refStr,
        'join_ref': refStr, 
        'topic': 'phoenix',
        'event': 'heartbeat',
        'payload': {}
    }
    await ws.send(orjson.dumps(ping))
    logging.info('who: %s  event: %s  execute: %d'%(token, 'ping', times))
    return

async def ratJob(token, nonce, botNum, roomInfo):
    sTime = 60 if botNum % 3 == 0 else botNum % 3
    await asyncio.sleep(5 * sTime)
    if botNum <= len(roomInfo) * 3:  
        index =  int(botNum / 3 - 1) if botNum % 3 == 0 else int(botNum / 3)
        action = {
            0:[
                {'event': 'phx_join', 'body': {}},
                {'event': 'message', 'body': {'content': '我是乖寶-'+ (datetime.now() + timedelta(hours=8)).strftime("%Y/%m/%d %H:%M:%S")}},
                {'event': 'message', 'body': {'content': '我等下要做reconnect囉⋯⋯'}},
                {'event': 'phx_join', 'body': {'action': 'reconnect'}},
                {'event': 'message', 'body': {'content': 'reconnect完囉，應該沒有看到我進來了吧？'}},
                {'event': 'message', 'body': {'content': '我是乖寶我要發有禁詞的訊息囉'}},
                {'event': 'message', 'body': {'content': '代儲代充超級方便，有需要請找美女編'}},
                {'event': 'gift', 'body': {'giftId': '728e32fa-96a1-43a0-a493-56997ea30bed', 'targetUserId': roomInfo[index]['masterId'], 'count': 1}},
                {'event': 'book_seat', 'body': {}},
                {'event': 'message', 'body': {'content': '我是乖寶記得讓我上麥，我要測sticker'}},
                {'event': 'send_sticker', 'body': {'stickerId': 48}},
                {'event': 'send_sticker', 'body': {'stickerId': 17}},
                {'event': 'send_sticker', 'body': {'stickerId': 29}},
                {'event': 'message', 'body': {'content': '我是乖寶要離開了，陪伴區少人囉，在麥位上會消失，我貢獻了 20 點'}}, 
            ],
            1:[ 
                {'event': 'phx_join', 'body': {}},
                {'event': 'message', 'body': {'content': '我嘴賤該被禁言。快來呀🙊🙊🙊'}},
                {'event': 'message', 'body': {'content': '禁言後除了訊息看不到，其他高級彈幕、送禮、分享及追蹤應該所有人都看到'}},
                {'event': 'share', 'body': {}},
                {'event': 'track', 'body': {'targetUserId': roomInfo[index]['masterId']}},
                {'event': 'gift', 'body': {'giftId': '5f0bb976-0bc7-459f-8a6a-67ee0b6e7758', 'targetUserId': roomInfo[index]['masterId'], 'count': 2}},
                {'event': 'book_seat', 'body': {}},
                {'event': 'message', 'body': {'content': '解除禁言第一次發言☝️☝️☝️'}},
                {'event': 'message', 'body': {'content': '解除禁言第二次發言'}},
                {'event': 'message', 'body': {'content': '第二次申請上麥喲'}},
                {'event': 'book_seat', 'body': {}},
                {'event': 'message', 'body': {'content': '自己取消上麥，我應該不在列表裡了'}}, 
                {'event': 'abort_seat', 'body': {}},
                {'event': 'message', 'body': {'content': '嘴賤要離開了，陪伴區少人囉，我貢獻了 400,000 點'}},   
            ],
            2:[
                {'event': 'phx_join', 'body': {}},
                {'event': 'message', 'body': {'content': '我是暱稱有禁詞的人⋯⋯你應該看不到我的訊息'}}, 
                {'event': 'book_seat', 'body': {}},
                {'event': 'share', 'body': {}},
                {'event': 'track', 'body': {'targetUserId': roomInfo[index]['masterId']}},
                {'event': 'gift', 'body': {'giftId': 'a700b291-362a-42fa-9db4-6d29d4541273', 'targetUserId': roomInfo[index]['masterId'], 'count': 2}},
            ]
        }

        try:
            connectStr = 'wss://%s/socket/websocket?token=%s&nonce=%s'%(roomInfo[index]['socketDomain'], token, nonce)
            ws = await websockets.connect(connectStr, ping_interval=None)
            refStr = str(int(time.time()))
            execTimes = 0
            actionIndex = 2 if botNum % 3 == 0 else (botNum % 3 - 1)
            for i in action[actionIndex]:
                await job(ws, roomInfo[index]['roomId'], refStr, i['event'], i['body'], token, execTimes + 1)
                await asyncio.sleep(40)
                await pinFun(ws, refStr, token, execTimes + 1)
        except Exception as e:
            logging.error('Exception: ', e)
        finally:
            await job(ws, roomInfo[index]['roomId'], refStr, 'phx_leave', {}, token, execTimes + 1)
            logging.info(token + ' connection close after 30 sec')
            await asyncio.sleep(30)
            await ws.close()
    else:
        logging.info(token + ' is superfluous')

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
                await pinFun(ws, refStr, token, testTimes)
                if k < 20:
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_leave', {}, token, testTimes)
                    await ws.close()
                    await asyncio.sleep(random.randint(3,10))
                    sNum, ws = await createConnection(token, nonce, roomInfo)
                    refStr = str(int(time.time()))
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {}, token, testTimes) 
                elif (k >= 70 and k <= 85) or (k >= 170 and k <= 185):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {'action': 'reconnect'}, token, testTimes) 
                elif k in (99, 197):
                    secStay = str(int(time.time() - int(refStr)))
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'message', {'content': '我在房內待了 '+secStay+'秒'}, token, testTimes)
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

def ratBot(roomInfoList):
    taskList = []    
    for i in range(1, 7):
        token = 'guest' + str(1999+i) 
        nonce = 'guest' + str(1999+i)
        task = loop.create_task(ratJob(token, nonce, i, roomInfoList))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        logging.error('main function get exception: ', e)
    finally:
        loop.close()

def roomBot(roomInfoList):
    taskList = []    
    for i in range(7, 411):
        token = 'guest' + str(1999+i) 
        nonce = 'guest' + str(1999+i)
        task = loop.create_task(roomInOut(token, nonce, roomInfoList))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        logging.error('main function get exception: ', e)
    finally:
        loop.close()

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


def setData():
    strSQL = "delete from fans where fans_id in (select id from identity where login_id between 'guest2000' and 'guest2008')"
    strSQL1 = "update remain_points set remain_points = 5000000 where identity_id in (select id from identity where login_id between 'guest2000' and 'guest2008')"
    dbConnect.dbSetting('testing-api.xtars.com',[strSQL, strSQL1])

if __name__ == '__main__':
    jobList = {'all': [ratBot, roomBot], 'rat': [ratBot], 'inout': [roomBot]}
    if sys.argv[1]:
        option = sys.argv[1]
        isSleep = False
        roomInfoList = getRoomInfo()
        if option != 'inout': setData()
        for i in jobList[option]:
            if isSleep:time.sleep(300) 
            else: isSleep = True
            i(roomInfoList)            
        logging.info('process finish')
    else:
        logging.info('parameter error')
