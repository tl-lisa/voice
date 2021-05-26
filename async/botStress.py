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

#server = 'testing-api.xtars.com'
adminList = []

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
    # print('send time: ', datetime.now().strftime('%H:%M:%S'))
    # pprint(body)
    return body

async def audience():
    global adminList
    isActivate = False
    msgList = [
        '太冷了⋯⋯今天早點下班', '加油加油～聲聊上線～', '我是免費仔，絕對不送禮', '主播姐姐聲音真好聽', 
        '勉強送個禮好了，不然被人嫌', '狗腿一下小馬好帥', '寒流來襲，抱啥可以？', '想要一個大紅包⋯⋯',
        '天冷不出門，下雨不出門，心情不美不出門', '芷馨好棒棒，鈺琇讚讚讚', 'OMG⋯⋯全台都缺暖暖包T T'
    ]
    giftList = [
            'bfda0320-9c3e-4d95-9abd-76222386b69d', '9590ade5-2dd9-4967-aeb9-78dcf6dcc897', 
            '2aab021a-beb6-4630-83de-1e3217b46bb3', '5f0bb976-0bc7-459f-8a6a-67ee0b6e7758', 
            '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8',
            '0ad27d12-193c-4f4c-a652-beae87811bdf', '4dc99482-416b-4ed6-b002-d5e66623aa60',
            '9e63bbf0-3e86-4019-b3fc-e955c175569b', '74d6e57e-1d0c-4717-8ca7-65d5b5baef0c',
            '176fbe34-6f97-466a-99e4-6c5c755486f8'
    ]    
    audienceActionDic = {
            1:{'action': 'message', 'percentage': 145, 'parameter': {'content': None}},
            2:{'action': 'book_seat', 'percentage': 149, 'parameter': {}},
            3:{'action': 'phx_leave', 'percentage': 150, 'parameter': {}},
            4:{'action': 'track', 'percentage': 150, 'parameter': {'liveMasterId': None}},
            5:{'action': 'gift', 'percentage': 149, 'parameter': {'giftId': None, 'targetUserId': None, 'count': None}}
    }
    actionId = random.randint(1, 5)
    if random.randint(1, 150) > audienceActionDic[actionId]['percentage']:
        isActivate = True
        if audienceActionDic[actionId]['action'] == 'message': 
            audienceActionDic[actionId]['parameter']['content'] = msgList[random.randint(0, len(msgList)-1)] + '@' + datetime.now().strftime('%H:%M:%S')
        if audienceActionDic[actionId]['action'] == 'track': audienceActionDic[actionId]['parameter']['liveMasterId'] = adminList[random.randint(0, len(adminList)-1)]
        if all([audienceActionDic[actionId]['action'] == 'gift', len(adminList) > 0]):
            # print('送禮物看坐位列表-adminList')
            # pprint(adminList)
            audienceActionDic[actionId]['parameter']['giftId'] = giftList[random.randint(0, len(giftList)-1)]   
            audienceActionDic[actionId]['parameter']['targetUserId'] = adminList[random.randint(0, len(adminList)-1)]
            if audienceActionDic[actionId]['parameter']['giftId'] != '176fbe34-6f97-466a-99e4-6c5c755486f8':
                audienceActionDic[actionId]['parameter']['count'] = random.randint(1, 3)          
            else:
                audienceActionDic[actionId]['parameter']['count'] = 1
        action = audienceActionDic[actionId]['action']
        parameter = audienceActionDic[actionId]['parameter']
    else:
        action = 'heartbeat'
        parameter = {}
    if isActivate:
        if audienceActionDic[actionId]['action'] == 'abort_seat':
            audienceActionDic[actionId]['action'] = 'book_seat'
            audienceActionDic[actionId]['percentage'] = 145
        elif audienceActionDic[actionId]['action'] == 'book_seat':
            audienceActionDic[actionId]['action'] = 'abort_seat'
            audienceActionDic[actionId]['percentage'] = 125
        # if audienceActionDic[actionId]['action'] == 'phx_leave':
        #     isLeave = 're-Join'
        #     # isLeave = 'Leave' if random.randint(1, 100) > 98 else 're-Join'
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
    

async def botJob(userInfo):
    global adminList
    roomId = userInfo['roomId']
    serverList =  ['10.140.0.159']
    sNum = random.randint(0, len(serverList) - 1) if len(serverList) > 1 else 0
    connectStr = 'ws://%s/socket/websocket?token=%s&nonce=%s'%(serverList[sNum], userInfo['token'], userInfo['nonce'])
    try:
        ws = await websockets.connect(connectStr, ping_interval=None)
        await asyncio.sleep(random.randint(2, 5))
        await ws.send(json.dumps(await actionBody('phx_join', {}, roomId)))   
        await getData(json.loads(await ws.recv()), userInfo)
        while 1: 
            if not ws.open:
                print ('Websocket NOT connected. Trying to reconnect.')
                ws = await websockets.connect(connectStr, ping_interval=None)
                await ws.send(json.dumps(await actionBody('phx_join', {}, roomId)))   
                await getData(json.loads(await ws.recv()), userInfo)
            try:
                begTime = int(time.time())
                action, parameter = await audience()
                await ws.send(json.dumps(await actionBody(action, parameter, roomId)))
                await getData(json.loads(await ws.recv()), userInfo)
                if int(time.time()) - begTime > 10:
                    print('waiting time over 10 sec')
                else:
                    remainTime = 10 - (int(time.time()) - begTime)
                    await asyncio.sleep(remainTime)
            except Exception as e:
                print('Error!: ', e)
                traceback.print_exc()
                break
    except Exception as e:
        print('bot job get err: ', e)
        traceback.print_exc()
    finally:
       await ws.close()

def main(beg, end, num):
    taskList = []    
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    for i in range(beg, end):
        loginDic = {}
        account = 'guest' + str(999+i)
        loginDic = {
            'nickname': account,
            'token': account + 'token',
            'nonce': account + 'nonce',
            'idType': 'audience',
            'roomId': None,
            'ownerId': None,
            'id': None            
        }
        loginDic['roomId'] = random.randint(1, num) if num > 1 else 1
        task = loop.create_task(botJob(loginDic))
        # taskList.append(asyncio.ensure_future(botJob(loginDic)))
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
        accountBeg = int(sys.argv[1])
        accountEnd = int(sys.argv[2])
        chatNum = int(sys.argv[3])
        main(accountBeg, accountEnd, chatNum)