import time
import pytest
import threading
import pytest_check as check
from pprint import pprint
from .testingCase import dbConnect
from .testingCase import backgift
from . import chatlib39 as chatlib 
from .testingCase import conCallCase

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
        dd1 = dd[0] if type(dd) == list else dd
        itemName = keyList.pop(0)
        for key, value in dd1.items():
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
                check.equal(value[0], i['value'], 'expect %s is %s but actually get %s'%(verifyKey, i['value'], value))
            else:
                check.is_false(value, 'expect %s is %s but actually get empty'%(verifyKey, i['value']))

    def checkKeys(self, resources, expectKeyList):
        keyList = []
        self.getDicKeys(resources, keyList)
        for i in expectKeyList:
            check.is_in(i, keyList, 'expect get %s but actually not found(%s)'%(str(i), str(keyList)))
            check.equal(expectKeyList.count(i), keyList.count(i), '%s數量不一致 return(%s), check(%s)'%(i, str(expectKeyList), str(keyList)))
            expectKeyList.pop(i)
            keyList.pop(i)

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
        print('%s get is %s at %d'%(verifyInfo['event'], str(isGetEvent), verifyInfo['position']))
        if verifyInfo.get('check'):
            if verifyInfo['check']:
                print('expect isGetEvent is true and actully %s'%str(isGetEvent))
                check.is_true(isGetEvent, "(%s) cannot found event(%s) at expect position(%d)"%(verifyInfo['index'], verifyInfo['event'], verifyInfo['position']))
                if isGetEvent:
                    pprint(event)
                    self.checkValue(event['payload'], verifyInfo['check'])
            else:
                print('expect isGetEvent is false and actully %s'%str(isGetEvent))
                check.is_false(isGetEvent, "should not get check data, but get event(%s) at position(%d)"%(i['event'], position))
        if verifyInfo.get('keyList'): self.checkKeys(event['payload'], keyList)

    def checkDBData(self, checkInfo):
        sqlStr = checkInfo['sqlStr']%checkInfo['parameters']
        dbResult = dbConnect.dbQuery(test_parameter['db'], sqlStr)
        for i in checkInfo['check']: 
            if dbResult:
                check.equal(dbResult[0][i['fieldIndex']], i['value'], 'expect fieldIndex(%d) is %s but db values is %s-%s'%(
                    i['fieldIndex'], str(i['value']), str(dbResult[0][i['fieldIndex']]), sqlStr))
            else:
                assert 'Query DB result is empty'
                break
                        
    @pytest.mark.parametrize("scenario, data, verifyInfo, verifyDB", backgift.getTestData(test_parameter))
    def testChat(self, scenario, data, verifyInfo, verifyDB):   
        threadList = []
        self.wsDic.clear()
        for i in range(len(data)):
            threadList.append(threading.Thread(target = self.wsJob, args = (data[i], i, )))
            threadList[i].start()
        for i in reversed(threadList):
            i.join()
        pprint(self.wsDic)   
        if self.wsDic:
            for k in verifyInfo:
                if self.wsDic[k['index']]:
                    print('check: ', k['index'])
                    self.verifyResult(self.wsDic[k['index']], k) 
                else:
                    print('%s無資料比對'%scenario)
        else:
            print('無執行資訊')
        for k in verifyDB: self.checkDBData(k)
                
           