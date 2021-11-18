import json
import time
from . import misc
from  websockets import connect
from  websocket import WebSocketApp
from pprint import pprint

class voiceUser():
    messageList = None
    def __init__(self, info, eventList, sleepTime, waitTime, id):
        time.sleep(waitTime)
        self.actionList = eventList
        self.sleepTime = sleepTime
        self.id = id
        self.messageList = []
        self.ws = WebSocketApp(info, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close
        )
        print('web socket-', id, ' setting: ', info, ' start_at: ', int(time.time() * 1000))
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def __del__(self):
        self.messageList = None
        self.actionList = None

    def on_message(self, message): 
        data = json.loads(message)
        self.messageList.insert(0, data)

    def on_error(self, error):
        pass

    def on_close(self):
        print("webSocket-", self.id, " has been closed at ", int(time.time()))

    def on_open(self):
        for i in self.actionList:
            sleep = i.pop('sleep')
            time.sleep(sleep)
            if i.get('apiName'):
                misc.apiFunction(i['prefix'], i['header'], i['apiName'], i['method'], i['body'])
            else:
                self.ws.send(json.dumps(i))
                # pprint(i)
        time.sleep(self.sleepTime)