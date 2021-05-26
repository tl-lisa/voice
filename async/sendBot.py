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
    giftList = [
            'bfda0320-9c3e-4d95-9abd-76222386b69d', '9590ade5-2dd9-4967-aeb9-78dcf6dcc897', 
            '2aab021a-beb6-4630-83de-1e3217b46bb3', '5f0bb976-0bc7-459f-8a6a-67ee0b6e7758', 
            '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8',
            '0ad27d12-193c-4f4c-a652-beae87811bdf', '4dc99482-416b-4ed6-b002-d5e66623aa60',
            '9e63bbf0-3e86-4019-b3fc-e955c175569b', '74d6e57e-1d0c-4717-8ca7-65d5b5baef0c',
            '176fbe34-6f97-466a-99e4-6c5c755486f8'
    ]    
    audienceActionDic = {
            1:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            2:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            3:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            4:{'action': 'heartbeat', 'percentage': 0, 'parameter': {}},
            5:{'action': 'gift', 'percentage': 99, 'parameter': {'giftId': None, 'targetUserId': None, 'count': None}}
    }
    while action == '':
        actionId = random.randint(1, 5)
        if random.randint(1, 100) > audienceActionDic[actionId]['percentage']:
            if audienceActionDic[actionId]['action'] == 'gift':
                audienceActionDic[actionId]['parameter']['giftId'] = giftList[random.randint(0, len(giftList)-1)]   
                audienceActionDic[actionId]['parameter']['targetUserId'] = '1e50e13d-1f41-40e2-b752-50fbf83777b4'
                if audienceActionDic[actionId]['parameter']['giftId'] != '176fbe34-6f97-466a-99e4-6c5c755486f8':
                    audienceActionDic[actionId]['parameter']['count'] = random.randint(1, 3)          
                else:
                    audienceActionDic[actionId]['parameter']['count'] = 1
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
        print('run main')
        main()