import asyncio
import botlib
import time
import random
import requests
import paramiko
import dbConnect
import orjson
from pprint import pprint

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()

async def botJob(num, rType, roomList):
    roomType = {
        'room': 'live_room', 
        'voiceChat': 'vc_room'
    }
    if rType == 'room':
        currentTopic = '%s:%d'%(roomType[rType],roomList[random.randint(0, len(roomList)-1)])
    else:
        currentTopic = '%s:%d'%(roomType[rType],random.randint(1, 3))
    token = 'guest' + str(1999+num) 
    nonce = 'guest' + str(1999+num)
    ref = int(time.time()*1000)
    bot = botlib.botUser(str(ref))
    await asyncio.sleep(random.randint(3, 7))
    await bot.connServer('testing-api.xtars.com', token, nonce)
    await bot.sendMsg('phx_join', currentTopic, {})
    while True:
        msg = await bot.recvMsg()
        if msg['event'] == 'luckymoney_lottery':
            bot.isChanged = True
        elif msg['event'] == 'luckymoney_data_changed_bcst':
            bot.isChanged = True if msg['payload']['data']['progress'] == 'GATHER' else False
            # print('%s change is %s'%(token, str(bot.isChanged)))
        elif msg['event'] == 'luckymoney_marquee':
            urlList = []
            url = msg['payload']['data']['url']
            urlList = url.split('/')
            newTopic = '%s:%s'%(roomType[urlList[2]], urlList[3])
            # print('%s receive marquee from %s and changed(%s)'%(token, newTopic, str(bot.isChanged)))
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
            await asyncio.sleep(random.randint(0, 3))
            bot.isChanged = True
            await bot.sendMsg('luckymoney_lottery', currentTopic, {"type": "2022CN.Lottery"}) 
        elif msg['event'] == 'close_room':
            newTopic = '%s:%d'%(roomType['voiceChat'],random.randint(1, 3))
            await bot.sendMsg('phx_leave', currentTopic, {})
            await asyncio.sleep(random.randint(3, 10))
            await bot.sendMsg('phx_join', newTopic, {})
            currentTopic = newTopic
        elif all([int(time.time()) - (ref / 1000) > 300, bot.isChanged]) : 
            break
    await bot.sendMsg('message', currentTopic, {'content': '%s走囉～'%token})
    await bot.sendMsg('phx_leave', currentTopic, {})
    await bot.ws.close()

def getOnline(hostAddress):
    roomList = []
    sqlStr = 'select id from live_room where status = 1 and password is NULL'
    dbResult = dbConnect.dbQuery(hostAddress, sqlStr)
    for i in dbResult:
        roomList.append(i[0])
    return roomList

def roomBot(hostAddress):
    taskList = []    
    roomList = getOnline(hostAddress)
    for i in range(10, 20):
        roomType = 'room' if all([i % 2 == 0, roomList]) else 'voiceChat'
        task = loop.create_task(botJob(i, roomType, roomList))
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
    ssh.exec_command(cmd)
    ssh.close()

def clearVoiceLuckyMoney(hostAddress):
    import datetime
    apiList = ['/api/v3/task/resetVoiceChatHistory', '/api/v3/task/resetVoiceChatLuckyMoney']
    for round in range(1,6):
        for roomId in range(1, 3):
            keyName = 'vc_room:luckmoney_data:%s:%d:%d-remainPoints'%(str(datetime.date.today()), roomId, round)
            clearCache(hostAddress, 'redis-cli -n 5 DEL %s;'%keyName)
            keyName = 'vc_room:luckmoney_data:%s:%d:%d-UserPoints'%(str(datetime.date.today()), roomId, round)
            clearCache(hostAddress, 'redis-cli -n 5 DEL %s;'%keyName)
    for i in apiList:
        apiName = 'https://%s%s'%(hostAddress,i)
        res = requests.post(apiName, headers={'Connection': 'application/json'}, json={"token" : "b603a650825c440d89c5f45a6703d5f8"})

if __name__ == '__main__': 
    host = 'testing-api.xtars.com'
    clearVoiceLuckyMoney(host)
    roomBot(host)
    print('process finish')
