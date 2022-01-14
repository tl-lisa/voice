import time
import pytest
import threading
from pprint import pprint
from . import chatlib
from . import voiceCase

env = 'QA'
DB = '35.234.17.150'
test_parameter = {}
header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}


class TestChatScoket(): 
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
        chat = chatlib.chatUser(info, eventList, data['sleep'], data['wait'], id)
        try:
            self.wsDic[account] = chat.messageList
        except Exception as err:
            print('get Error: ', err)
        finally:
            del chat

    def getVal(self, dd, keyList, vList):  
        itemName = keyList.pop(0)
        for key, value in dd.items():
            if key == itemName:
                if len(keyList) > 0:
                    self.getVal(value, keyList, vList) 
                else:
                    vList.append(value)
                    break
            else:
                continue
        return 

    def getDicKeys(self, dd, keyList):  
        for keys, values in dd.items():
            keyList.append(keys)
            if type(values) == dict:
                self.getDicKeys(values, keyList)
            elif all([type(values) == list, values]):
                if type(values[0]) == dict: self.getDicKeys(values[0], keyList)
            else:
                continue          
        return 

    def checkValue(self, resource, valueList):
        value = []
        for i in valueList:
            value.clear()
            verifyKey = i['key'][len(i['key']) - 1]
            self.getVal(resource, i['key'], value)
            if value:
                assert value[0] == i['value'], 'expect %s is %s but actually get %s'%(verifyKey, i['value'], value)
            else:
                assert value, 'expect %s is %s but actually get empty'%(verifyKey, i['value'])

    def checkKeys(self, resources, expectKeyList):
        keyList = []
        self.getDicKeys(resources, keyList)
        assert len(keyList) == len(expectKeyList), 'expect get %d keys but actually get %d'%(len(expectKeyList), len(keyList))
        for i in expectKeyList:
            assert i in keyList, 'expect get %s but actually not found(%s)'%(str(i), str(keyList))

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
                self.checkValue(event['payload'], verifyInfo['check'])
        elif verifyInfo.get('keyList'):
            self.checkKeys(event['payload'], keyList)

                        
    @pytest.mark.parametrize("scenario, data, verifyInfo", voiceCase.getTestData(test_parameter))
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
                print('check: ', k['index'])
                self.verifyResult(self.wsDic[k['index']], k) 
            else:
                print('%s無資料比對'%scenario)
                
           