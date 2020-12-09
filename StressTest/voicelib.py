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
    #觀眾只要測申請上麥，自行取消下麥，送禮及發送訊息，追蹤，離房再進入
    ws = None
    def __init__(self, server, userDic, roomDic, roomId):
        self.userDic = userDic
        self.roomId = roomId
        self.roomDic = roomDic
        self.server = server
        self.connect_setting

    def actionBody(self, action, targetUser):
        giftList=[
            'ac3250eb-20fb-4bd3-a93a-92bf10eb90c0',

        ]
        giftIndex = random.randint(0, len(giftList))
        giftCount = random.randint(1,5)
        actionDic = {
            'phx_join': {},
            'book_seat': {},
            'abort_seat': {},
            'pin': {},
            'phx_leave': {},
            'take_seat': {'seatIndex': self.userDic['seatId'] },
            'leave_seat': {},
            'get_mics_mgm': {},
            'get_violation': {},
            'mute_seat': {'targetUserId': targetUser},
            'unmute_seat': {'targetUserId': targetUser},
            'message': {'content': targetUser+'發言'},
            'gift': {'giftId': giftList[giftIndex], 'targetUserId': targetUser, 'count': giftCount+5}
        }
        body = {
                'ref': str(int(time.time()*1000)),
                'join_ref': str(int(time.time()*1000)),
                'topic': 'vc_room:' + str(self.roomId),
                'event': action,
                'payload': actionDic[action]
        }
        return body
 
    def on_message(self, message): 
        pass

    def on_error(self, error):
        print(error)

    def on_close(self):
        self.ws.close()

    def connect_setting(self):
        connectStr = 'ws://%s/socket/websocket?token=%s&nonce=%s'%(self.server, self.userDic['token'], self.userDic['nonce'])
        self.ws = WebSocketApp(connectStr, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close
        )
        self.ws.on_open = self.on_open    
 
    def audience(self):
        actionDic = {
            0:{'action': 'message', 'percentage': 60, 'parameter': None},
            1:{'action': 'book_seat', 'percentage': 20, 'parameter': None},
            2:{'action': 'gift', 'percentage':85, 'parameter': self.roomDic[self.roomId][random.randint(0, 3)]},
            3:{'action': 'phx_leave', 'percentage': 95, 'parameter': None}
        }
        actionId = random.randint(1, time.time()) % 6
        if (random.randint(1, time.time()) % 100) >= actionDic[actionId]['percentage']:
            self.ws.send(json.dumps(self.actionBody(actionDic[actionId]['action'], actionDic[actionId]['action'])))
            if actionId == 1: 
                if actionDic[actionId]['action'] == 'abort_seat':
                    actionDic[actionId]['action'] = 'book_seat'
                    actionDic[actionId]['percentage'] = 20
                else:
                    actionDic[actionId]['action'] = 'abort_seat'
                    actionDic[actionId]['percentage'] = 75
        return

    def admin(self):
        actionDic = {
            0: {'action': 'message', 'percentage': 40, 'parameter': None},
            1: {'action': 'take_seat', 'percentage': 20, 'parameter': None},
            2: {'action': 'get_mics_mgm', 'percentage':50, 'parameter': None},
            3: {'action': 'phx_leave', 'percentage': 95, 'parameter': None},
            4: {'action': 'get_violation', 'percentage':50, 'parameter': None},
            5: {'action': 'mute_seat', 'percentage':50, 'parameter': self.userDic['id']}
        }
        actionId = random.randint(1, time.time()) % 6
        if (random.randint(1, time.time()) % 100) >= actionDic[actionId]['percentage']:
            self.ws.send(json.dumps(self.actionBody(actionDic[actionId]['action'], actionDic[actionId]['action'])))            
            if actionId in (1, 5):
                if actionDic[actionId]['action'] == 'take_seat': 
                    actionDic[actionId]['action'] = 'leave_seat'
                    actionDic[actionId]['percentage'] = 75
                else:
                    actionDic[actionId]['action'] = 'take_seat'
                    actionDic[actionId]['percentage'] = 20
                actionDic[actionId]['action'] = 'unmute_seat' if actionDic[actionId]['action'] == 'mute_seat' else 'mute_seat'
        return

    def owner(self):
        actionDic = {
            0:{'action': 'message', 'percentage': 40},
            1:{'action': 'abort_seat', 'percentage': 75, 'status': True},
            2:{'action': 'gift', 'percentage':85},
            3:{'action': 'phx_leave', 'percentage': 95}
        }
        actionId = random.randint(1, time.time()) % 4
        if (random.randint(1, time.time()) % 100) >= actionDic[actionId]['percentage']:
            self.ws.send(json.dumps(self.actionBody(actionDic[actionId]['action'], actionDic[actionId]['action'])))
            if all([actionId == 1, actionDic[actionId]['status']]):
                actionDic[actionId]['action'] = 'book_seat'
                actionDic[actionId]['status'] = False
                actionDic[actionId]['percentage'] = 20
            else:
                actionDic[actionId]['action'] = 'abort_seat'
                actionDic[actionId]['status'] = True
                actionDic[actionId]['percentage'] = 75
        return

    def on_open(self):
        aciotnDic = {'audience': self.audience, 'admin': self.admin, 'owner': self.owner}
        self.ws.send(json.dumps(self.actionBody('phx_join', None)))    
        while 1:
            time.sleep(10)
            self.ws.send(json.dumps(self.actionBody('pin', None)))
            aciotnDic[self.userDic['idType']]
