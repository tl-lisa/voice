import asyncio
import botlib
import time
from pprint import pprint

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()

async def botJob(num):
    roomType = {'room': 'live_room:', 'voiceChat': 'vc_room:'}
    token = 'guest' + str(1999+num) 
    nonce = 'guest' + str(1999+num)
    ref = int(time.time()*1000)
    bot = botlib.botUser(str(ref))
    await bot.connServer('testing-api.xtars.com', token, nonce)
    await bot.sendMsg('phx_join', 'vc_room:3', {})
    while True:
        msg = await bot.recvMsg()
        pprint(msg)
        staySec = int(time.time()) - ref / 1000
        if staySec % 30 == 0:
            await bot.sendMsg('message', 'vc_room:3', {'content': '%s已經待了%d秒'%(token, staySec)})
        elif int(time.time()) - ref / 1000 > 180: break
    await bot.sendMsg('message', 'vc_room:3', {'content': '%s走囉～'%token})
    await bot.sendMsg('phx_leave', 'vc_room:3', {})
    await bot.ws.close()
    
def roomBot():
    taskList = []    
    for i in range(1, 3):
        task = loop.create_task(botJob(i))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        print('main function get exception: ', e)
    finally:
        loop.close()

if __name__ == '__main__':
    roomBot()
    # strT = 'xtars://room/5248'    
    # str2 = strT.split('/')  
    # print(str2[len(str2) - 1], str2[len(str2)-2])      
    print('process finish')
