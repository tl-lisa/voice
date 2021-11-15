import asyncio
import websockets
import aiohttp
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

async def ratJob(token, nonce, botNum):
    roomInfo = await createConnection(token, nonce, 'RAT')
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
                {'event': 'gift', 'body': {'giftId': 'c95857e5-8677-47c5-884b-89ab09f22fe4', 'targetUserId': roomInfo[index]['masterId'], 'count': 1}},
                {'event': 'barrage', 'body': {'barrageId': 1, 'content': '你有看到我剛剛含禁詞的訊息嗎？我也要用彈幕發相同的訊息囉'}},
                {'event': 'barrage', 'body': {'barrageId': 1, 'content': '代儲代充超級方便，有需要請找美女小編'}},
                {'event': 'message', 'body': {'content': '你有看到我剛剛含禁詞的彈幕嗎？'}},
                {'event': 'gift', 'body': {'giftId': 'dbe2c2c8-f9a5-4fa8-bfd8-10f2a1eb1246', 'targetUserId': roomInfo[index]['masterId'], 'count': 5}},
                {'event': 'message', 'body': {'content': '我是乖寶要離開了，陪伴區少人囉，我貢獻了 298 點'}}, 

            ],
            1:[ 
                {'event': 'phx_join', 'body': {}},
                {'event': 'phx_join', 'body': {}},
                {'event': 'message', 'body': {'content': '我嘴賤該被禁言。快來呀🙊🙊🙊'}},
                {'event': 'message', 'body': {'content': '禁言後除了訊息看不到，其他高級彈幕、送禮、分享及追蹤應該所有人都看到'}},
                {'event': 'barrage', 'body': {'barrageId': 2, 'content': '我是嘴錢被禁言，剛剛有送訊息你們看不到，只好花錢發高級彈幕'}},
                {'event': 'share', 'body': {}},
                {'event': 'track', 'body': {'targetUserId': roomInfo[index]['masterId']}},
                {'event': 'barrage', 'body': {'barrageId': 2, 'content': '我分享而且有追蹤直播主了'}},
                {'event': 'gift', 'body': {'giftId': 'f522ae8a-88c9-428e-964a-f626a3a96ec8', 'targetUserId': roomInfo[index]['masterId'], 'count': 1}},
                {'event': 'barrage', 'body': {'barrageId': 2, 'content': '你可以解除禁言了嗎'}},
                {'event': 'gift', 'body': {'giftId': '5b1646be-1400-4837-ab2e-d55d9945f8bc', 'targetUserId': roomInfo[index]['masterId'], 'count': 1}},
                {'event': 'message', 'body': {'content': '解除禁言第一次發言☝️☝️☝️'}},
                {'event': 'message', 'body': {'content': '解除禁言第二次發言'}},
                {'event': 'message', 'body': {'content': '嘴賤要離開了，陪伴區少人囉，我貢獻了 111,197 點'}},   
            ],
            2:[
                {'event': 'phx_join', 'body': {}},
                {'event': 'message', 'body': {'content': '我是暱稱有禁詞的人⋯⋯你應該看不到我的訊息'}}, 
                {'event': 'barrage', 'body': {'barrageId': 2, 'content': '我是暱稱有禁詞的人⋯⋯你應該看不到我的訊息，只好花錢發高級彈幕'}},
                {'event': 'share', 'body': {}},
                {'event': 'track', 'body': {'targetUserId': roomInfo[index]['masterId']}},
                {'event': 'barrage', 'body': {'barrageId': 2, 'content': '我分享而且有追蹤直播主了'}},
                {'event': 'gift', 'body': {'giftId': 'aec97465-e5c1-432e-b401-beed7d3a1d7a', 'targetUserId': roomInfo[index]['masterId'], 'count': 5}},
                {'event': 'barrage', 'body': {'barrageId': 2,'content': '嘴賤要離開了，陪伴區少人囉，我貢獻了 1,001,197 點'}},    
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
                await job(ws, roomInfo[index]['roomId'], refStr, 'ping', {}, token, execTimes + 1)
        except Exception as e:
            logging.error('Exception: ', e)
        finally:
            await job(ws, roomInfo[index]['roomId'], refStr, 'phx_leave', {}, token, execTimes + 1)
            logging.info(token + ' connection close after 30 sec')
            await asyncio.sleep(30)
            await ws.close()
    else:
        logging.info(token + ' is superfluous')

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
                elif (k >= 70 and k <= 85) or (k >= 170 and k <= 185):
                    await job(ws, roomInfo[sNum]['roomId'], refStr, 'phx_join', {'action': 'reconnect'}, token, testTimes) 
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

def ratBot():
    taskList = []    
    for i in range(1, 10):
        token = 'guest' + str(2999+i) 
        nonce = 'guest' + str(2999+i)
        task = loop.create_task(ratJob(token, nonce, i))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        logging.error('main function get exception: ', e)
    finally:
        loop.close()

def roomBot():
    taskList = []    
    for i in range(1, 351):
        token = 'guest' + str(2999+i) 
        nonce = 'guest' + str(2999+i)
        task = loop.create_task(roomInOut(token, nonce))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        logging.error('main function get exception: ', e)
    finally:
        loop.close()

def setData():
    strSQL = "delete from fans where fans_id in (select id from identity where login_id between 'guest3000' and 'guest3008')"
    strSQL1 = "update remain_points set remain_points = 5000000 where identity_id in (select id from identity where login_id between 'guest3000' and 'guest3008')"
    dbConnect.dbSetting('testing-api.xtars.com',[strSQL, strSQL1])

if __name__ == '__main__':
    jobList = {'all': [ratBot, roomBot], 'rat': [ratBot], 'inout': [roomBot]}
    if sys.argv[1]:
        option = sys.argv[1]
        isSleep = False
        if option != 'inout': setData()
        for i in jobList[option]:
            if isSleep:time.sleep(300) 
            else: isSleep = True
            i()            
        logging.info('process finish')
    else:
        logging.info('parameter error')
