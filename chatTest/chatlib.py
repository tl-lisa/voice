import json
import sys
import time
import asyncio
import random   
import websocket      
from  websocket import WebSocketApp
from pprint import pprint

class chatUser():
    messageList = None
    def __init__(self, info, eventList, sleepTime, waitTime, id):
        self.actionList = eventList
        self.sleepTime = sleepTime
        self.id = id
        self.messageList = []
        time.sleep(waitTime)
        print('\nweb socket-', id, ' setting: ', info, ' start_at: ', int(time.time() * 1000))
        self.ws = WebSocketApp(info, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close
        )
        self.ws.on_open = self.on_open
        self.ws.run_forever()     

    def __del__(self):
        self.messageList = None
        self.actionList = None

    def on_message(self, message): 
        data = json.loads(message)
        pprint(data)
        self.messageList.insert(0, data)

    def on_error(self, error):
        print('get ', self.id, ' error: ', error)

    def on_close(self):
        print("webSocket-", self.id, " has been closed at ", int(time.time()))

    def on_open(self):
        for i in self.actionList:
            pprint(i)
            waitTime = i.pop('sleep')
            time.sleep(waitTime)
            self.ws.send(json.dumps(i))
        time.sleep(self.sleepTime)
