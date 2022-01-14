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
from . import privateCase

env = 'QA'
DB = '35.234.17.150'
test_parameter = {}
idlist = []
header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}

misc.get_test_data(env, test_parameter, 'private', 1, 21, 3)      

@pytest.fixture(scope="class")
def clearCach():
    misc.clearCache(DB)

class TestVoiceScoket(): 
    wsDic = {}
    def wsJob(self, data, id):
        #print('%d start at %d'%(id, int(time.time())))
        eventList = []
        ref1 = str(int(time.time()*1000))
        for j in data['action']:
            if j[0] == 'api':
                body = j[1]
                body['sleep'] = j[2]
            else:
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

    def checkValue(self, checkList, event):
        kk = event['payload']
        for j in checkList:
            isFound = False
            findKey = j['key']
            print('find key is ', findKey)
            itemName = findKey.pop(0)
            for key, value in kk.items():
                print('get key(%s) compare itemName(%s)'%(key, itemName))
                if key == itemName:
                    print('get key(', itemName, ')')
                    if len(findKey) > 0:
                        yy = value     
                        itemName = findKey.pop(0)
                        isContinue = True
                        while isContinue:
                            print('while loop remaind value: %s and next key is %s'%(str(yy), itemName))
                            if yy:
                                for k1, v1 in yy.items():
                                    print('for loop get key(%s) compare itemName(%s)'%(k1, itemName))
                                    if all([k1 == itemName, len(findKey) == 0]):
                                        print('check [%s] get value = %s and we expected value = %s'%(itemName, str(v1), str(j['value'])))
                                        if 'index' in j:
                                            assert v1[j['index']] == j['value'],'check [%s] get value = %s but we expected value = %s'%(itemName, str(v1[j['index']]), str(j['value']))
                                        else: 
                                            assert v1 == j['value'], 'check [%s] get value is: %s but we expected result is: %s'%(itemName, str(v1), str(j['value']))
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
                                isContinue = False
                    else:
                        if j.get('index'):
                            assert value[j['index']] == j['value']
                        else:
                            assert value == j['value']
                        isFound = True
                    break
            assert isFound, "should get key(%s) at event(%s), but didn't"%(itemName, event['event'])            

    def verifyResult(self, data, verifyInfo):
        isGetEvent = False 
        position = 0
        event = None
        keyList = []
        for i in data:
            print('data event=', i['event'],' verify event=',verifyInfo['event'], ' position=', position,' verify position=',verifyInfo['position'])
            if i['event'] == verifyInfo['event']:
                if verifyInfo['position'] == position:
                    isGetEvent = True
                    event = i
                    break
                else:
                    position += 1
        if verifyInfo.get('check'):
            if verifyInfo['check']:
                assert isGetEvent, "(%s) cannot found event(%s) at expect position(%d)"%(verifyInfo['index'], verifyInfo['event'], verifyInfo['position'])
            else:
                assert not isGetEvent, "should not get check data, but get event(%s) at position(%d)"%(i['event'], position)
            if isGetEvent:
                pprint(event)
                self.checkValue(verifyInfo['check'], event)
        elif verifyInfo.get('keyList'):
            misc.getDicKeys(event['payload'], keyList)
            assert len(keyList) == len(verifyInfo['keyList']), "取得資料長度不一致：source(%s) & expect(%s)"%(str(keyList), str(verifyInfo['keyList']))
            for i in verifyInfo['keyList']:
                assert i in keyList , "not found key(%s) in keyList(%s)"%(i, str(keyList))

    @pytest.mark.parametrize("scenario, data, verifyInfo", privateCase.getTestData(test_parameter))
    def testPrivate(self, scenario, data, verifyInfo):   
        threadList = []
        self.wsDic.clear()
        for i in range(len(data)):
            threadList.append(threading.Thread(target = self.wsJob, args = (data[i], i, )))
            threadList[i].start()
        for i in reversed(threadList):
            i.join()
        pprint(self.wsDic)   
        print('scenario is: %s'%scenario)
        for k in verifyInfo:
            if self.wsDic[k['index']]:
                print('check: ', k['index'])
                self.verifyResult(self.wsDic[k['index']], k) 
            else:
                print('無資料比對')
                
           