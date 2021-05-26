import time
import json
import pytest
import threading
import random
import types
import traceback
from pprint import pprint
from . import chatlib
from . import dbConnect
from . import misc
from . import chatCase

env = 'QA'
DB = '35.234.17.150'
test_parameter = {}
header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}

misc.get_test_data(env, test_parameter, 'master')    

class TestChatScoket(): 
    wsDic = {}
    def setUp_class(self):
        prefix = 'http://35.234.17.150'
        header['X-Auth-Token'] = test_parameter['tl-lisa']['token']
        header['X-Auth-Nonce'] = test_parameter['tl-lisa']['nonce']
        apiName = '/api/v3/task/resetLiveMasterHotMarqueeHistory'
        body = {'token' : test_parameter['master10']['id']}
        misc.apiFunction(prefix, header, apiName, 'post', body)

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
        chat = chatlib.chatUser(info, eventList, data['sleep'], data['wait'], id)
        try:
            self.wsDic[account] = chat.messageList
        except Exception as err:
            print('get Error: ', err)
        finally:
            del chat

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
                if event['event'] == 'room_closed':
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

                        
    @pytest.mark.parametrize("scenario, data, verifyInfo", chatCase.getTestData(test_parameter))
    def testChat(self, scenario, data, verifyInfo):   
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
                #print('check: ', k['index'])
                self.verifyResult(self.wsDic[k['index']], k) 
            else:
                print('無資料比對')
                
           