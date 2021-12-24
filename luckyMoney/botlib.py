import orjson
import asyncio
import  websockets
from pprint import pprint

class botUser():
    isChanged = True
    def __init__(self, ref):
        self.ws = None
        self.refStr = ref        

    async def connServer(self, info, token, nonce):
        conStr = 'ws://%s/socket/websocket?token=%s&nonce=%s'%(info, token, nonce)
        self.ws = await websockets.connect(conStr, ping_interval=35)

    async def recvMsg(self): 
        data = orjson.loads(await self.ws.recv())
        # pprint(data)
        return data

    async def sendMsg(self, action, topic, body):
        actStr = {
            'ref': self.refStr,
            'join_ref': self.refStr, 
            'topic': topic,
            'event': action,
            'payload': body
        }
        # pprint(actStr)
        await self.ws.send(orjson.dumps(actStr)) 


