import json
import sys
import time
import asyncio
import random         
import websocket
from  websockets import connect
from  websocket import WebSocketApp
from pprint import pprint

class voice():
    def __init__(self, server, userDic, adminList, roomId):
        self.gift = ['4b5d7cbe-485c-41dc-a78c-f0b06cf61a25', 'a700b291-362a-42fa-9db4-6d29d4541273', '49853090-e4cd-47da-826e-1131388bd6c4', 'ddc2eadf-e40f-4e33-896f-764674366dd9', '1a51e630-3956-46e0-8bb9-e334f06b5634']
        self.userDic = userDic
        self.roomId = roomId
        self.adminList = adminList
        self.server = server
        connectStr = 'ws://%s/socket/websocket?token=%s&nonce=%s'%(self.server, self.userDic['token'], self.userDic['nonce'])
        # print('connectStr: ', connectStr)
        self.ws = WebSocketApp(connectStr, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close)
        self.ownerActionDic = {
            0: {'action': 'mute_seat', 'percentage':50, 'parameter': {'targetUserId': self.userDic['id']}},
            1: {'action': 'message', 'percentage': 60, 'parameter': {'content': self.userDic['id']+'發言'}},
            2: {'action': 'phx_leave', 'percentage': 85, 'parameter': {}},
            3: {'action': 'send_sticker', 'percentage':50, 'parameter': {'stickerId': None}},
            4: {'action': 'get_mics_mgm', 'percentage':50, 'parameter': {}},
            5: {'action': 'get_violation', 'percentage':50, 'parameter': {}},
        }
        self.adminActionDic = {
            0: {'action': 'mute_seat', 'percentage':50, 'parameter': {'targetUserId': self.userDic['id']}},
            1: {'action': 'message', 'percentage': 60, 'parameter': {'content': self.userDic['id']+'發言'}},
            2: {'action': 'take_seat', 'percentage': 20, 'parameter': {'seatIndex': self.userDic['seatId']}},
            3: {'action': 'phx_leave', 'percentage': 85, 'parameter': {}},
            4: {'action': 'get_mics_mgm', 'percentage':50, 'parameter': {}},
            5: {'action': 'get_violation', 'percentage':50, 'parameter': {}},
            6: {'action': 'send_sticker', 'percentage':50, 'parameter': {'stickerId': None}},
        }
        self.audienceActionDic = {
            1:{'action': 'message', 'percentage': 60, 'parameter': {'content': self.userDic['id']+'發言'}},
            2:{'action': 'book_seat', 'percentage': 20, 'parameter': {}},
            3:{'action': 'phx_leave', 'percentage': 85, 'parameter': {}},
            4:{'action': 'track', 'percentage': 65, 'parameter': {}},
            5:{'action': 'gift', 'percentage': 100, 'parameter': {
                'giftId': None, 
                'targetUserId': random.randint(0, len(adminList)-1), 
                'count': random.randint(1, 3)}
            },
        }

    def actionBody(self, action, parameter):
        payload = {}
        bodyDic = {
            'noPayload': ['phx_join', 'ping', 'phx_leave', 'book_seat', 'leave_seat', 'abort_seat', 'get_mics_mgm', 'get_violation'],
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
        body = {
                'ref': str(int(time.time()*1000)),
                'join_ref': str(int(time.time()*1000)),
                'topic': 'vc_room:' + str(self.roomId),
                'event': action,
                'payload': payload
        }
        #pprint(body)
        return body
 
    def on_message(self, message): 
        data = json.loads(message)
        pprint(data)

    def on_error(self, error):
        print(error)

    def on_close(self):
        self.ws.close()
 
    def on_connect(self):
        # print('setting open function')
        self.ws.on_open = self.on_open    
        self.ws.run_forever()

    def audience(self):
        isLeave = False
        actionId = random.randint(1, 5)
        if (random.randint(1, int(time.time())) % 100) >= self.audienceActionDic[actionId]['percentage']:
            if self.adminActionDic[actionId]['action'] == 'gift':
                    self.adminActionDic[actionId]['parameter']['giftId'] = self.gift[random.randint(0,4)]                    
            self.ws.send(json.dumps(self.actionBody(self.audienceActionDic[actionId]['action'], self.audienceActionDic[actionId]['parameter'])))
            if self.audienceActionDic[actionId]['action'] in ('abort_seat', 'book_seat'): 
                if self.audienceActionDic[actionId]['action'] == 'abort_seat':
                    self.audienceActionDic[actionId]['action'] = 'book_seat'
                    self.audienceActionDic[actionId]['percentage'] = 20
                else:
                    self.audienceActionDic[actionId]['action'] = 'abort_seat'
                    self.audienceActionDic[actionId]['percentage'] = 75
            if self.audienceActionDic[actionId]['action'] == 'phx_leave':
                if random.randint(1, int(time.time())) % 100 >= 70:
                    isLeave = True
                else:
                    self.ws.send(json.dumps(self.actionBody('phx_join', [])))
        return isLeave

    def admin(self):
        isLeave = False
        actionId = random.randint(0, 6)
        while all([actionId == 0, self.adminActionDic[2]['action'] == 'take_seat']):
            actionId = random.randint(0, 6)
        if (random.randint(1, int(time.time())) % 100) >= self.adminActionDic[actionId]['percentage']:
            if self.adminActionDic[actionId]['action'] == 'send_sticker':
                self.adminActionDic[actionId]['parameter']['stickerId'] = random.randint(11, 55)
            self.ws.send(json.dumps(self.actionBody(self.adminActionDic[actionId]['action'], self.adminActionDic[actionId]['parameter'])))   
            if actionId == 2:         
                if  self.adminActionDic[actionId]['action'] == 'take_seat':               
                    self.adminActionDic[actionId]['action'] = 'leave_seat'
                    self.adminActionDic[actionId]['percentage'] = 75
                else:
                    self.adminActionDic[actionId]['action'] = 'take_seat'
                    self.adminActionDic[actionId]['percentage'] = 20
            if actionId == 0:
                self.adminActionDic[actionId]['action'] = 'unmute_seat' if self.adminActionDic[actionId]['action'] == 'mute_seat' else 'mute_seat'
            if  self.adminActionDic[actionId]['action'] == 'phx_leave':
                if random.randint(1, int(time.time())) % 100 >= 70:
                    isLeave = True
                else:
                    self.ws.send(json.dumps(self.actionBody('phx_join', [])))
        return isLeave

    def owner(self):
        isLeave = False
        actionId = random.randint(0, 5)
        if (random.randint(1, int(time.time())) % 100) >= self.ownerActionDic[actionId]['percentage']:
            if self.adminActionDic[actionId]['action'] == 'send_sticker':
                self.adminActionDic[actionId]['parameter']['stickerId'] = random.randint(11, 55)
            self.ws.send(json.dumps(self.actionBody(self.ownerActionDic[actionId]['action'], self.ownerActionDic[actionId]['parameter'])))
            if actionId == 0:
                self.ownerActionDic[actionId]['action'] = 'unmute_seat' if self.ownerActionDic[actionId]['action'] == 'mute_seat' else 'mute_seat'
            if self.ownerActionDic[actionId]['action'] == 'phx_leave':
                if random.randint(1, int(time.time())) % 100 >= 70:
                    isLeave = True
                else:
                    self.ws.send(json.dumps(self.actionBody('phx_join', [])))
        return isLeave

    def on_open(self):
        aciotnDic = {'audience': self.audience, 'admin': self.admin, 'owner': self.owner}
        self.ws.send(json.dumps(self.actionBody('phx_join', {})))    
        while 1:
            time.sleep(10)
            self.ws.send(json.dumps(self.actionBody('ping', {})))
            if aciotnDic[self.userDic['idType']](): break

