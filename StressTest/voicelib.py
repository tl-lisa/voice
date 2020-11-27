import json
import sys
import time
import asyncio
import random         
import websocket
from  websockets import connect
from  websocket import WebSocketApp
from pprint import pprint


class audience():
    #觀眾只要測申請上麥，自行取消下麥，送禮及發送訊息
    def __init__(self, ):
        self.ws = WebSocketApp(info, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close
        )
        self.ws.on_open = self.on_open

    def on_message(self, message): 
        pass

    def on_error(self, error):
        print('get ', self.id, ' error: ', error)

    def on_close(self):
        pass

    def on_open(self):
        while 1:
            for i in self.actionList:
                sleep = i.pop('sleep')
                time.sleep(sleep)
                #pprint(i)
                self.ws.send(json.dumps(i))
            time.sleep(self.sleepTime)
 

class admin():
    #2位管理員，三不五時取得申請上麥列表及違規列表
    def __init__(self, ):
        self.ws = WebSocketApp(info, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close
        )
        self.ws.on_open = self.on_open

    def on_message(self, message): 
        pass

    def on_error(self, error):
        print('get ', self.id, ' error: ', error)

    def on_close(self):
        pass

    def on_open(self):
        while 1:

        for i in self.actionList:
            sleep = i.pop('sleep')
            time.sleep(sleep)
            #pprint(i)
            self.ws.send(json.dumps(i))
        time.sleep(self.sleepTime)

class owner():
    #房主會取得靜音列表，申請上麥列表，違規列表
    def __init__(self, ):
        self.ws = WebSocketApp(info, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close
        )
        self.ws.on_open = self.on_open

    def on_message(self, message): 
        pass

    def on_error(self, error):
        print('get ', self.id, ' error: ', error)

    def on_close(self):
        pass

    def on_open(self):
        while 1:

        for i in self.actionList:
            sleep = i.pop('sleep')
            time.sleep(sleep)
            #pprint(i)
            self.ws.send(json.dumps(i))
        time.sleep(self.sleepTime)
