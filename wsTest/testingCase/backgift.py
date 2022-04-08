# 加入DB資料比對及key完整性檢查 
# for ticket #5084~5086; #5058~5060
from . import misc
from . import dbConnect
from pprint import pprint
from datetime import datetime, timedelta
import json

def getRoomId(prefix, token, nonce, nickname, pwd):
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}
    header['X-Auth-Token'] = token
    header['X-Auth-Nonce'] = nonce
    apiName = '/api/v2/liveMaster/zego/liveRoom'
    body = {
        "title" : nickname + "開播囉",
        "description" : nickname + "開播，歡迎入群",
        "events": [],
        "code": pwd
    }
    res = misc.apiFunction(prefix, header, apiName, 'post', body)
    result = json.loads(res.text)
    roomNo = result['data']['roomId']
    return roomNo

def sendBackpackGift(test_parameter, userList):
    uList = []
    for i in userList: uList.append(test_parameter[i]['id'])
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}
    header['X-Auth-Token'] =  test_parameter['tl-lisa']['token']
    header['X-Auth-Nonce'] = test_parameter['tl-lisa']['nonce']
    apiName = '/api/v2/backend/accomplishment/send'
    body = {
        "acmpId": 118,
        "users": uList,
        "tagIds": [],
        "availableTimeType": "TIME_OFFSET",
        "availableDays": 1,
        "activated": True,
        "suitStatus": False,
        "acmpItemIds": [2],
        "scheduleStatus": False,
        "quantity": 2
    }
    res = misc.apiFunction(test_parameter['prefix'], header, apiName, 'post', body)
    result = json.loads(res.text)
    return result['data']['id']

def getBackpackGift(test_parameter, loginList, deliveryId, is30Sec):
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}
    apiName = '/api/v2/identity/backpack/gift/list'
    for i in loginList:
        header['X-Auth-Token'] =  test_parameter[i]['token']
        header['X-Auth-Nonce'] = test_parameter[i]['nonce']
        res = misc.apiFunction(test_parameter['prefix'], header, apiName, 'get', None)
        result = json.loads(res.text)
        test_parameter[i]['backId'] = result['data']['gifts'][0]['id']
        test_parameter[i]['uuid'] = result['data']['gifts'][0]['uuid']
        test_parameter[i]['giftId'] = result['data']['gifts'][0]['giftId']
        test_parameter[i]['quantity'] = result['data']['gifts'][0]['quantity']
    if is30Sec:
        endTime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        sendTime = datetime.strftime(datetime.now() - timedelta(days=1), '%Y-%m-%d %H:%M:%S')
        sqlStr = "update %s set end_time = '%s' where backpack_id = %d"%('backpack_status', endTime, test_parameter[loginList[0]]['backId'])
        sqlStr1 = "update %s set send_time = '%s' where id = %d"%('backpack_delivery_history', sendTime, deliveryId)
        dbConnect.dbSetting(test_parameter['db'], [sqlStr, sqlStr1])

def getTestData(test_parameter):
    create_at = datetime.strftime(datetime.now() - timedelta(hours=8), '%Y-%m-%d %H:%M:%S')
    roomType = 'live_room' #'live_room', 'private_vc_room' 'vc_room'
    if roomType == 'live_room':
        send_at =  'liveroom' 
        masterId = 'master10' 
        misc.get_test_data('QA', test_parameter, 'master', 5, 10, 30, 2)   # master10
        roomNo = getRoomId(test_parameter['prefix'], test_parameter[masterId]['token'], 
                            test_parameter[masterId]['nonce'], test_parameter[masterId]['nickname'], '')
    else:
        send_at =  'voice' 
        if roomType == 'vc_room':
            masterId = 'broadcaster001' 
            misc.get_test_data('QA', test_parameter, 'broadcaster', 5, 1, 30, 3)  
            roomNo = 1
        else:
            masterId = 'priveate02' 
            misc.get_test_data('QA', test_parameter, 'private', 2, 1, 30, 2)  
            roomNo = 54
    deliveryId = sendBackpackGift(test_parameter, ['track0011', 'track0012', 'track0020'])
    getBackpackGift(test_parameter, ['track0011', 'track0012', 'track0020'], deliveryId,  False)
    # deliveryId = sendBackpackGift(test_parameter, ['track0011'])
    # getBackpackGift(test_parameter, ['track0011'], deliveryId, True)
    testData = [
        ('用戶送出背包禮-數量不足、暱稱含禁詞', #5084
            [       
                {'user': masterId, 'wait': 0, 'action': [
                        ('%s:%d'%(roomType, roomNo), 'phx_join', {}, 0), 
                        ('%s:%d'%(roomType, roomNo), 'phx_leave', {}, 20),
                    ], 'sleep': 5
                }, 
                {'user': 'track0011', 'wait': 2, 'action': [
                        ('%s:%d'%(roomType, roomNo), 'phx_join', {}, 0), 
                        ('%s:%d'%(roomType, roomNo), 'gift', 
                            {'giftId': test_parameter['track0011']['uuid'], 
                            'targetUserId': test_parameter[masterId]['id'], 'backpackId': test_parameter['track0011']['backId'], 'count': 1}, 1),
                        ('%s:%d'%(roomType, roomNo), 'phx_leave', {}, 5),
                    ], 'sleep': 3
                },
                {'user': 'track0012', 'wait': 3, 'action': [
                        ('%s:%d'%(roomType, roomNo), 'phx_join', {}, 0), 
                        ('%s:%d'%(roomType, roomNo), 'gift', 
                            {'giftId': test_parameter['track0012']['uuid'], 
                            'targetUserId': test_parameter[masterId]['id'], 'backpackId': test_parameter['track0012']['backId'], 'count': 5}, 1),
                        ('%s:%d'%(roomType, roomNo), 'phx_leave', {}, 5),
                    ], 'sleep': 3
                },
                {'user': 'track0020', 'wait': 4, 'action': [
                        ('%s:%d'%(roomType, roomNo), 'phx_join', {}, 0), 
                        ('%s:%d'%(roomType, roomNo), 'gift', 
                            {'giftId': test_parameter['track0020']['uuid'], 
                            'targetUserId': test_parameter[masterId]['id'], 'backpackId': test_parameter['track0020']['backId'], 'count': 1}, 1),
                        ('%s:%d'%(roomType, roomNo), 'phx_leave', {}, 5),
                    ], 'sleep': 3
                },
            ],  
            [
                {'index': masterId, 'event': 'gift_bcst', 'position': 0, 'check': [
                        {'key': ['data', 'gift', 'id'], 'value': test_parameter['track0011']['uuid']},
                        {'key': ['data', 'fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                        {'key': ['data', 'gift', 'categoryId'], 'value': 7},
                    ]
                },
                {'index': masterId, 'event': 'gift', 'position': 0, 'check': [
                        {'key': ['data', 'gift', 'id'], 'value': test_parameter['track0020']['uuid']},
                        {'key': ['data', 'fromUser', 'id'], 'value': test_parameter['track0020']['id']},
                        {'key': ['data', 'gift', 'categoryId'], 'value': 7},
                    ]
                },
                {'index': masterId, 'event': 'gift_bcst', 'position': 1, 'check': []},
                {'index': 'track0012', 'event': 'phx_reply', 'position': 1, 'check': [
                        {'key': ['response', 'err'], 'value': 'QUANTITY_NOT_ENOUGH'},
                    ]
                },
                {'index': 'track0011', 'event': 'gift_bcst', 'position': 0, 'keyList': [
                        'data', 'content', 'en', 'zh', 'ja', 'room', 'totalGiftPoints', 'liveRanking', 'hot', 'gift', 'id', 
                        'categoryId', 'name', 'en', 'zh', 'ja', 'url', 'duration', 'count', 'multiple', 'points', 'fromUser',
                        'id', 'name', 'roles', 'userLevel', 'levelId', 'levelNum', 'targetUser', 'id', 'name', 'roles', 'userLevel', 
                        'levelId', 'levelNum', 'sendTime'
                    ] 
                },
                {'index': 'track0020', 'event': 'gift', 'position': 0, 'keyList': [
                        'data', 'content', 'en', 'zh', 'ja', 'room', 'totalGiftPoints', 'liveRanking', 'hot', 'gift', 'id', 
                        'categoryId', 'name', 'en', 'zh', 'ja', 'url', 'duration', 'count', 'multiple', 'points', 'fromUser',
                        'id', 'name', 'roles', 'userLevel', 'levelId', 'levelNum', 'targetUser', 'id', 'name', 'roles', 'userLevel', 
                        'levelId', 'levelNum', 'sendTime'
                    ] 
                },
            ],
            [
                {
                    'sqlStr': "select %s, %s, %s, %s from %s where sender_id = '%s' and create_at >= '%s' order by id desc limit 1", 
                    'parameters': ('gift_type', 'point', 'count', 'receiver_id', 'point_consumption_history', test_parameter['track0011']['id'], create_at),
                    'check':[
                        {'fieldIndex': 0, 'value': send_at},
                        {'fieldIndex': 1, 'value': 0},
                        {'fieldIndex': 2, 'value': 1},
                        {'fieldIndex': 3, 'value': test_parameter[masterId]['id']}
                    ]
                },
                {
                    'sqlStr': "select %s from %s where backpack_id = %d", 
                    'parameters': ('quantity', 'backpack_status', test_parameter['track0011']['backId']),
                    'check':[{'fieldIndex': 0, 'value': 1}]
                },
                {
                    'sqlStr': "select %s from %s where backpack_id = %d", 
                    'parameters': ('quantity', 'backpack_status', test_parameter['track0012']['backId']),
                    'check':[
                        {'fieldIndex': 0, 'value': 2}
                    ]
                },
                {
                    'sqlStr': "select %s, %s from %s where room_id = %d and create_user_id = '%s' and create_at >= '%s' order by id desc limit 1", 
                    'parameters': ('consumption_point', 'gift_id', 'live_room_gift', roomNo, test_parameter['track0011']['id'], create_at),
                    'check':[
                        {'fieldIndex': 0, 'value': 0},
                        {'fieldIndex': 1, 'value': test_parameter['track0011']['uuid']}
                    ]
                },
                {
                    'sqlStr': "select %s, %s, %s from %s where create_user_id = '%s' and create_at >= '%s' order by id desc limit 1", 
                    'parameters': ('live_room_gift_id', 'add_points', 'source_from', 'remain_points_history', test_parameter['track0011']['id'], create_at),
                    'check':[
                        {'fieldIndex': 0, 'value': test_parameter['track0011']['giftId']},
                        {'fieldIndex': 1, 'value': 0},
                        {'fieldIndex': 2, 'value': 'backpack_gift'}
                    ]
                },

            ]
        ),

        # ('用戶送出背包禮-逾時未超過30秒、逾時已超過30秒', 
        #     [       
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('%s:%d'%(roomType, roomNo), 'phx_join', {}, 0), 
        #                 ('%s:%d'%(roomType, roomNo), 'phx_leave', {}, 20),
        #             ], 'sleep': 5
        #         }, 
        #         {'user': 'track0011', 'wait': 2, 'action': [
        #                 ('%s:%d'%(roomType, roomNo), 'phx_join', {}, 0), 
        #                 ('%s:%d'%(roomType, roomNo), 'gift', 
        #                     {'giftId': test_parameter['track0011']['uuid'], 
        #                     'targetUserId': test_parameter[masterId]['id'], 'backpackId': test_parameter['track0011']['backId'], 'count': 1}, 1),
        #                 ('%s:%d'%(roomType, roomNo), 'ping', {}, 30), 
        #                 ('%s:%d'%(roomType, roomNo), 'gift', 
        #                     {'giftId': test_parameter['track0011']['uuid'], 
        #                     'targetUserId': test_parameter[masterId]['id'], 'backpackId': test_parameter['track0011']['backId'], 'count': 1}, 1),
        #                 ('%s:%d'%(roomType, roomNo), 'phx_leave', {}, 5),
        #             ], 'sleep': 3
        #         },
        #     ],  
        #     [
        #         {'index': masterId, 'event': 'gift_bcst', 'position': 0, 'check': [
        #                 {'key': ['data', 'gift', 'id'], 'value': test_parameter['track0011']['uuid']},
        #                 {'key': ['data', 'fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['data', 'gift', 'categoryId'], 'value': 7},
        #             ]
        #         },
        #         {'index': masterId, 'event': 'gift_bcst', 'position': 1, 'check': []},
        #     ],
        #     [
        #         {
        #             'sqlStr': "select %s from %s where backpack_id = %d", 
        #             'parameters': ('quantity', 'backpack_status', test_parameter['track0011']['backId']),
        #             'check':[
        #                 {'fieldIndex': 0, 'value': 1}
        #             ]
        #         },
        #         {
        #             'sqlStr': "select count(*) from %s where create_user_id = '%s' and create_at >= '%s'", 
        #             'parameters': ('remain_points_history', test_parameter['track0011']['id'], create_at),
        #             'check':[
        #                 {'fieldIndex': 0, 'value': 1},
        #             ]
        #         },

        #     ]

        # ),

    ]   

    return testData        
