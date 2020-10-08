import json
import sys
import time
import asyncio
import websocket
from  websockets import connect
from  websocket import WebSocketApp
from pprint import pprint

class voiceUser():
    messageList = None
    def __init__(self, info, eventList, sleepTime, id):
        self.actionList = eventList
        self.sleepTime = sleepTime
        self.id = id
        self.messageList = []
        print('web socket-', id, ' setting: ', info)
        self.ws = WebSocketApp(info, 
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close
        )
        self.ws.on_open = self.on_open
        self.ws.run_forever(ping_interval=60,ping_timeout=5)

    def __del__(self):
        self.messageList = None
        self.actionList = None
        print('web socket-', self.id, ' over at ', int(time.time()))

    def on_message(self, message): 
        data = json.loads(message)
        self.messageList.insert(0, data)

    def on_error(self, error):
        print('get ', self.id, ' error: ', error)

    def on_close(self):
        print("webSocket-", self.id, " has been closed at ", int(time.time()))

    def on_open(self):
        for i in self.actionList:
            self.ws.send(json.dumps(i))
            time.sleep(0.2)
        time.sleep(self.sleepTime)
        
class aioUser():
    def __init__(self, info):
        self.info = info

    def __await__(self):
        return self._async_init().__await__()

    async def _async_init(self):
        print(self.info)
        self._conn = connect(self.info)
        self.ws = await self._conn.__aenter__()
        return self

    async def close(self):
        print('connect close')
        await self._conn.__aexit__(*sys.exc_info())

    async def send(self, message):
        for i in message:
            pprint(i)
            await self.ws.send(i)
            data = await self.ws.recv()
            pprint(data)

    async def receive(self):
        data = await self.ws.recv()
        pprint(data)

    # async def __aenter__(self):
    #     print('connect: ', self.info)
    #     self._conn = connect(self.info)
    #     self.ws = await self._conn.__aenter__()        
    #     return self

    # async def __aexit__(self, *args, **kwargs):
    #     print('disconnect')
    #     await self._conn.__aexit__(*args, **kwargs)

    async def process(self, event):
        messageList = []
        count = 0
        while count < 4:
            if len(event) > 0:
                pprint(event[0])
                await self.ws.send(event[0])
                event.pop(0)
            data = json.loads(await self.ws.recv())
            pprint(data)
            if data:
                messageList.insert(0, data)
            else:
                count +=1
            await asyncio.sleep(0.3)
        return messageList
        

