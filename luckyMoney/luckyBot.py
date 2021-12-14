import asyncio
import botlib
import time
import random
import requests
import paramiko
from pprint import pprint

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()

async def botJob(num):
    roomType = {'room': 'live_room:', 'voiceChat': 'vc_room:'}
    currentTopic = 'vc_room:%d'%(random.randint(1, 3))
    token = 'guest' + str(1999+num) 
    nonce = 'guest' + str(1999+num)
    ref = int(time.time()*1000)
    bot = botlib.botUser(str(ref))
    await asyncio.sleep(random.randint(3, 7))
    await bot.connServer('testing-api.xtars.com', token, nonce)
    await bot.sendMsg('phx_join', currentTopic, {})
    while True:
        msg = await bot.recvMsg()
        staySec = int(time.time()) - (ref / 1000)
        if msg['event'] in ('luckymoney_lottery', 'phx_reply'):
            pprint(msg)
        elif msg['event'] == 'luckymoney_marquee':
            urlList = []
            url = msg['payload']['data']['url']
            urlList = url.split('/')
            newTopic = roomType[urlList[2]] + urlList[3]
            if bot.isChanged:
                if newTopic != currentTopic:
                    await bot.sendMsg('phx_leave', currentTopic, {})
                    await asyncio.sleep(random.randint(3, 10))
                    await bot.sendMsg('phx_join', newTopic, {})
                    currentTopic = newTopic
                bot.isChanged = False
        elif msg['event'] == 'luckymoney_warm_up_bcst':
            bot.isChanged = False
        elif msg['event'] == 'luckymoney_ready_bcst':
            await asyncio.sleep(random.randint(1, 3))
            await bot.sendMsg('luckymoney_lottery', currentTopic, {"type": "2022CN.Lottery"}) 
            bot.isChanged = True
        elif int(time.time()) - (ref / 1000) > 900: 
            break
        elif random.randint(1,100) > 95:
            await bot.sendMsg('message', currentTopic, {'content': '%s已經待了%d秒'%(token, staySec)})
    await bot.sendMsg('message', currentTopic, {'content': '%s走囉～'%token})
    await bot.sendMsg('phx_leave', currentTopic, {})
    await bot.ws.close()
    
def roomBot():
    taskList = []    
    for i in range(10, 20):
        task = loop.create_task(botJob(i))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        print('main function get exception: ', e)
    finally:
        loop.close()

def clearCache(hostAddr, cmd):
    keyfile = './lisakey'  
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostAddr, username='lisa', key_filename=keyfile)
    # cmd = 'redis-cli flushdb;'
    ssh.exec_command(cmd)
    ssh.close()

def clearVoiceLuckyMoney():
    import datetime
    apiList = ['/api/v3/task/resetVoiceChatHistory', '/api/v3/task/resetVoiceChatLuckyMoney']
    url = 'http://testing-api.truelovelive.com.tw'
    hostAddress = 'testing-api.truelovelive.com.tw'
    for i in range(1,6):
        for j in range(1, 3):
            keyName = 'vc_room:luckmoney_data:%s:%d:%d-remainPoints'%(str(datetime.date.today()), j, i)
            clearCache(hostAddress, 'redis-cli -n 5 DEL %s;'%keyName)
            keyName = 'vc_room:luckmoney_data:%s:%d:%d-UserPoints'%(str(datetime.date.today()), j, i)
            clearCache(hostAddress, 'redis-cli -n 5 DEL %s;'%keyName)
    header = {'Connection': 'application/json'}
    body = {"token" : "123"}    
    for i in apiList:
        apiName = url+i
        requests.post(apiName, headers=header, json=body)

if __name__ == '__main__':
    clearVoiceLuckyMoney()
    roomBot()
    print('process finish')
