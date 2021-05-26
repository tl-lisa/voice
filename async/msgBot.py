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

async def actionBody(action, parameter, roomId):
    payload = {}
    bodyDic = {
        'noPayload': ['phx_join', 'heartbeat', 'phx_leave', 'book_seat', 'leave_seat', 'abort_seat', 'get_mics_mgm', 'get_violation'],
        'take_seat': ['seatIndex'],
        'message': ['content'],
        'mute_seat': ['targetUserId'],
        'unmute_seat': ['targetUserId'],
        'track': ['liveMasterId'],
        'send_sticker': ['stickerId'],
        'gift': ['giftId', 'targetUserId', 'count']
    }
    if action in bodyDic['noPayload']:
        payload = {}
    else:
        for i in bodyDic[action]:
            payload[i] = parameter[i]
    topicStr = 'phoenix' if action == 'heartbeat' else 'vc_room:' + str(roomId)
    body = {
            'ref': str(int(time.time()*1000)),
            'join_ref': str(int(time.time()*1000)),
            'topic': topicStr,
            'event': action,
            'payload': payload
    }
    return body

async def audience():
    action = ''
    parameter = {}
    msgList = [
        '太冷了⋯⋯今天早點下班', '加油加油～聲聊上線～', '我是免費仔，絕對不送禮', '主播姐姐聲音真好聽', 
        '勉強送個禮好了，不然被人嫌', '狗腿一下小馬好帥', '寒流來襲，抱啥可以？', '想要一個大紅包⋯⋯',
        '天冷不出門，下雨不出門，心情不美不出門', '芷馨好棒棒，鈺琇讚讚讚', 'OMG⋯⋯全台都缺暖暖包T T'
    ]
    audienceActionDic = {
            1:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            2:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            3:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            4:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            5:{'action': 'message', 'percentage': 145, 'parameter': {'content': None}}
    }
    while action == '':
        actionId = random.randint(1, 5)
        if random.randint(1, 100) > audienceActionDic[actionId]['percentage']:
            if audienceActionDic[actionId]['action'] == 'message': 
                audienceActionDic[actionId]['parameter']['content'] = msgList[random.randint(0, len(msgList)-1)] + '@' + datetime.now().strftime('%H:%M:%S')
            action = audienceActionDic[actionId]['action']
            parameter = audienceActionDic[actionId]['parameter']
    return action, parameter
 
async def getData(recMsg, userInfo):
    global adminList
    upList = []
    if recMsg['event'] == 'voiceroom_in': 
        userInfo['ownerId'] = recMsg['payload']['data']['ownerUserId']
        userInfo['id'] = recMsg['payload']['data']['joinUserId']
    if recMsg['event'] in ('seat_left', 'seat_taken', 'voiceroom_in', 'voiceroom_left_bcst'):        
        for i in recMsg['payload']['data']['seats']:
            if i['userId']: upList.append(i['userId'])
        if all([userInfo['ownerId'], userInfo['ownerId'] not in upList]): upList.append(userInfo['ownerId']) 
    if upList: adminList = upList
    return 
    

async def botJob(token, nonce):
    roomId = 1
    serverList = ['testing-api.xtars.com']
    sNum = random.randint(0, len(serverList) - 1) if len(serverList) > 1 else 0
    connectStr = 'ws://%s/socket/websocket?token=%s&nonce=%s'%(serverList[sNum], token, nonce)
    try:
        await asyncio.sleep(random.randint(2, 5))
        ws = await websockets.client.connect(connectStr, ping_interval=None)
        await ws.send(json.dumps(await actionBody('phx_join', {}, roomId)))   
        while 1: 
            action, parameter = await audience()
            await ws.send(json.dumps(await actionBody(action, parameter, roomId)))
            await asyncio.sleep(55)
    except Exception as e:
        print('bot job get err: ', e)
        traceback.print_exc()
    finally:
       await ws.close()

def main():
    taskList = []    
    beg = int(sys.argv[1])
    end = int(sys.argv[2])
    for i in range(beg, end):
        token = 'guest' + str(999+i) + 'token'
        nonce = 'guest' + str(999+i) + 'nonce'
        task = loop.create_task(botJob(token, nonce))
        taskList.append(task)
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
        main()