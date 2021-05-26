import asyncio
import websockets
import time
import sys
import random
import traceback
import orjson
import logging
from pprint import pprint
from datetime import datetime

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()
logging.basicConfig(level=logging.DEBUG)

async def botJob(token, nonce):
    roomId = 1
    serverList = ['testing-api.xtars.com']
    sNum = random.randint(0, len(serverList) - 1) if len(serverList) > 1 else 0
    connectStr = 'ws://%s/socket/websocket?token=%s&nonce=%s'%(serverList[sNum], token, nonce)
    logging.info(connectStr)
    ping = {
        'ref': None, 
        'join_ref': None, 
        'topic': 'phoenix',
        'event': 'heartbeat',
        'payload': {}
    }
    joinRoom = {
        'ref': str(int(time.time())), 
        'join_ref': str(int(time.time())), 
        'topic': 'vc_room:' + str(roomId),
        'event': 'phx_join',
        'payload': {}
    }

    leaveRoom = {
        'ref': str(int(time.time())), 
        'join_ref': str(int(time.time())), 
        'topic': 'vc_room:' + str(roomId),
        'event': 'phx_leave',
        'payload': {}
    }

    try:
        await asyncio.sleep(random.randint(2, 5))
        ws = await websockets.connect(connectStr, ping_interval=None)
        await ws.send(orjson.dumps(joinRoom)) 
        testTimes = 0  
        connected = True  
        while connected:
            k = int(random.random() * 100)
            try:
                if k > 75:
                    await ws.send(orjson.dumps(leaveRoom))
                    await asyncio.sleep(2)
                    await ws.send(orjson.dumps(joinRoom)) 
                await ws.send(orjson.dumps(ping))
                await asyncio.sleep(30)
                testTimes += 1
                if testTimes > 3000:
                    await ws.send(orjson.dumps(leaveRoom))
                    break
            except Exception as e1:
                connected = False  
                while not connected:  
                    try:  
                        ws = await websockets.connect(connectStr, ping_interval=None)
                        await ws.send(orjson.dumps(joinRoom)) 
                        logging.error('reconnect success: ', e1)
                        testTimes = 0  
                        connected = True  
                    except Exception as e2: 
                        logging.error('reconnect failed: ', e2)
                        await asyncio.sleep(2)    
    except Exception as e:
        logging.error('Exception: ', e2)
        traceback.print_exc()
    finally:
       await ws.close()

def main():
    taskList = []    
    beg = int(sys.argv[1])
    end = int(sys.argv[2])
    chatNum = int(sys.argv[3])
    #print('beg= ',beg, ' end= ', end)
    for i in range(beg, end):
        token = 'guest' + str(999+i) 
        nonce = 'guest' + str(999+i)
        task = loop.create_task(botJob(token, nonce))
        taskList.append(task)
    #print('job add finish')
    try:
        loop.run_until_complete(asyncio.wait(taskList))
        loop.run_until_complete(asyncio.sleep(2.0))
    except Exception as e:
        logging.error('main function get exception: ', e)
        traceback.print_exc()
    finally:
        loop.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        logging.info('請輸入測試帳號起迄值及聲聊房數, ', sys.argv)
        sys.exit(1)
    else:
        logging.info('run main')
        main()
