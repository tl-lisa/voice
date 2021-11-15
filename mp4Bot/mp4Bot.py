import asyncio
import requests
import orjson
import logging
import dbConnect
import chat
import voice

asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()
logging.basicConfig(level=logging.DEBUG,
	format='[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt='%Y%m%d %H:%M:%S',
)

def roomBot(roomInfoList):
    taskList = []    
    for i in range(1, 501):
        token = 'guest' + str(2999+i) 
        nonce = 'guest' + str(2999+i)
        task = loop.create_task(chat.roomInOut(token, nonce))
        taskList.append(task)
    for i in range(1, 501):
        token = 'guest' + str(1999+i) 
        nonce = 'guest' + str(1999+i)
        task = loop.create_task(voice.roomInOut(token, nonce, roomInfoList))
        taskList.append(task)
    try:
        loop.run_until_complete(asyncio.wait(taskList))
    except Exception as e:
        logging.error('main function get exception: ', e)
    finally:
        loop.close()

def getRoomInfo():
    prefix = 'testing-api.xtars.com'
    rList = []
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': 'guest1000', 'X-Auth-Nonce': 'guest1000'}
    for i in range(1, 3):
        url = 'https://%s/api/v2/identity/voiceChat/%s'%(prefix, str(i))
        res = requests.get(url, headers=header)
        result = orjson.loads(res.text)
        rList.append(
            {
                'roomId': str(result['data']['id']),
                'masterId': result['data']['masterId'],
                'socketDomain': result['data']['socketDomain']
            }
        )
    # pprint(rList)
    return rList

def setData():
    strSQL = "update remain_points set remain_points = 5000000 where identity_id in (select id from identity where login_id between 'guest3000' and 'guest3501')"
    strSQL1 = "update remain_points set remain_points = 5000000 where identity_id in (select id from identity where login_id between 'guest2000' and 'guest2501')"
    dbConnect.dbSetting('testing-api.xtars.com',[strSQL, strSQL1])

if __name__ == '__main__':
    roomInfoList = getRoomInfo()
    setData()
    roomBot(roomInfoList)            
    logging.info('process finish')
