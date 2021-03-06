import time
import json
import pytest
import threading
import random
import types
import traceback
from pprint import pprint
from . import voicelib
from . import dbConnect
from . import misc
from . import testingCase

env = 'QA'
DB = '35.234.17.150'
test_parameter = {}
idlist = []
header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}

misc.get_test_data(env, test_parameter, 'broadcaster0')  
def createVoiceRoom(account):
    header['X-Auth-Token'] = test_parameter['tl-lisa']['token']
    header['X-Auth-Nonce'] = test_parameter['tl-lisa']['nonce']
    apiName = '/api/v2/backend/voiceChat'
    body = {
        'typeId':1,
        'masterId': test_parameter[account]['id'],
        'title': account+'的直播間',
        'description': '快來加入'+account+'的直播間吧！',
        'password': '',
        'status': 1
    }
    misc.apiFunction(test_parameter['prefix'], header, apiName, 'post', body)
    return 
      

@pytest.fixture(scope="class")
def editInit():
    # 建立聲聊房資訊。若已建立則不需再call
    # misc.clearVoice(test_parameter['db'])
    # misc.clearCache(test_parameter['db'])
    # createVoiceRoom('broadcaster010')
    # header['X-Auth-Token'] = test_parameter['broadcaster010']['token']
    # header['X-Auth-Nonce'] = test_parameter['broadcaster010']['nonce']
    # for i in range(11, 15):
    #     admin = 'broadcaster0' + str(i)
    #     apiName = '/api/v2/liveMaster/voiceChat/admin'
    #     body = {
    #         'roomId': 1,
    #         'userId': test_parameter[admin]['id']
    #     }
    #     misc.apiFunction(test_parameter['prefix'], header, apiName, 'post', body)
    # misc.changeRole(test_parameter['prefix'], test_parameter['tl-lisa']['token'], test_parameter['tl-lisa']['nonce'], [test_parameter['broadcaster021']['id']], 4)
    pass
    

class TestVoiceScoket(): 
    wsDic = {}
    def wsJob(self, data, id):
        #print('%d start at %d'%(id, int(time.time())))
        eventList = []
        for j in data['action']:
            ref1 = str(int(time.time()*1000))
            body = {
                'ref': ref1,
                'join_ref': ref1,
                'topic': j[0],
                'event': j[1],
                'payload': j[2],
                'sleep': j[3]
            }
            eventList.append(body)
        account = data['user']
        info  = 'ws://'+test_parameter['db']+'/socket/websocket?token='+test_parameter[account]['token'] + '&nonce=' + test_parameter[account]['nonce']
        voice = voicelib.voiceUser(info, eventList, data['sleep'], data['wait'], id)
        try:
            self.wsDic[account] = voice.messageList
        except Exception as err:
            print('get Error: ', err)
        finally:
            del voice

    def oldverifyResult(self, data, verifyInfo):
        isGetEvent = False 
        position = 0
        event = None
        for i in data:
            print('data event=', i['event'],' verify event=',verifyInfo['event'], ' position=', position,' verify position=',verifyInfo['position'])
            if i['event'] == verifyInfo['event']:
                if i['event'] == 'audience_blocked':
                    pass #check user_blocks  
                elif i['event'] == '':
                    pass #check fnas
                if verifyInfo['position'] == position:
                    isGetEvent = True
                    event = i
                    break
                else:
                    position += 1
        if verifyInfo['check']:
            assert isGetEvent, "should get check data, but not"
        else:
            assert not isGetEvent, "should not get check data, but get event(%s) at position(%d)"%(i['event'], position)
        if isGetEvent:
            for j in verifyInfo['check']:
                count = 0
                tmp = event
                isGetKey = False
                while not isGetKey:
                    if tmp:
                        for key, value in tmp.items():
                            if key == j['key']:
                                if j['value'] and type(j['value']) == list:
                                    isGetValue = False
                                    for vv in j['value']:
                                        print('check key is ',key, ' check event is', event, ' check value is', vv)
                                        isGetValue = True if vv in value else False
                                    assert isGetValue
                                else:
                                    print('check key is ',key, ' check event is', event, ' check value is', value)
                                    assert j['value'] == value
                                isGetKey = True
                                break
                            else:
                                if type(value) == dict:
                                    tmp = tmp[key]
                                    break
                    else:
                        break
                    if count > 8:
                        break
                    else:
                        count += 1                   
                assert isGetKey, "Cannot get key("+j['key']+ ")"

    def verifyResult(self, data, verifyInfo):
        isGetEvent = False 
        position = 0
        event = None
        for i in data:
            print('data event=', i['event'],' verify event=',verifyInfo['event'], ' position=', position,' verify position=',verifyInfo['position'])
            if i['event'] == verifyInfo['event']:
                if verifyInfo['position'] == position:
                    isGetEvent = True
                    event = i
                    break
                else:
                    position += 1
        if verifyInfo['check']:
            assert isGetEvent, "should get check data, but not"
        else:
            assert not isGetEvent, "should not get check data, but get event(%s) at position(%d)"%(i['event'], position)
        if isGetEvent:
            pprint(event)
            for j in verifyInfo['check']:
                if event['event'] == 'phx_reply':
                    kk = event['payload']
                else:
                    kk = event['payload']['data']
                    pprint(kk)
                    isFound = False
                    findKey = j['key']
                    # print('find key is ', findKey)
                    itemName = findKey.pop(0)
                    for key, value in kk.items():
                        # print('get key(%s) compare itemName(%s)'%(key, itemName))
                        if key == itemName:
                            # print('get key(', itemName, ')')
                            if len(findKey) > 0:
                                yy = value     
                                itemName = findKey.pop(0)
                                isContinue = True
                                while isContinue:
                                    # print('while loop remaind value: %s and next key is %s'%(str(yy), itemName))
                                    for k1, v1 in yy.items():
                                        # print('for loop get key(%s) compare itemName(%s)'%(k1, itemName))
                                        if all([k1 == itemName, len(findKey) == 0]):
                                            # print('check [%s] get value = %s and we expected value = %s'%(itemName, str(v1), str(j['value'])))
                                            assert v1 == j['value']
                                            isContinue = False
                                            isFound = True
                                            break
                                        elif all([k1 == itemName, len(findKey) > 0]):
                                            yy = v1    
                                            itemName = findKey.pop(0)
                                            isContinue = True
                                            break
                                        else:
                                            isContinue = False
                            else:
                                assert value == j['value']
                                isFound = True
                            break
                    assert isFound, "should not get check key(%s) at event(%s)"%(itemName, i['event'])            

    @pytest.mark.parametrize("scenario, data, verifyInfo", testingCase.getTestData(test_parameter))
    def testVoice(self, editInit, scenario, data, verifyInfo):   
        threadList = []
        self.wsDic.clear()
        for i in range(len(data)):
            threadList.append(threading.Thread(target = self.wsJob, args = (data[i], i, )))
            threadList[i].start()
        for i in reversed(threadList):
            i.join()
        pprint(self.wsDic)   
        for k in verifyInfo:
            if self.wsDic[k['index']]:
                print('check: ', k['index'])
                self.verifyResult(self.wsDic[k['index']], k) 
                if all([k['index'] == 'track0012', k['event'] == 'voiceroom_in']): #for ticket2585 查詢陪伴區的觀眾
                    header['X-Auth-Token'] = test_parameter['track0012']['token']
                    header['X-Auth-Nonce'] = test_parameter['track0012']['nonce']
                    apiName = '/api/v2/identity/roomAudiences/voiceChat/1'
                    res = misc.apiFunction(test_parameter['prefix'], header, apiName, 'get', None)
                    resText = json.loads(res.text)
                    assert len(resText['data']) == 2
                    assert all([item in resText['data'] for item in [
                        test_parameter['track0012']['id'], test_parameter['track0012']['id'], 
                        test_parameter['track0012']['id'], test_parameter['track0011']['id']
                    ]]) == True
            else:
                print('無資料比對')
                
           