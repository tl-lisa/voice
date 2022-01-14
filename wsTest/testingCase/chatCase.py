from . import misc
from pprint import pprint
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

def getTestData(test_parameter, masterId):
    pwd = ''
    misc.get_test_data('QA', test_parameter, 'master', 5, 10, 30, 2)  
    pprint(test_parameter)    
    roomNo = getRoomId(test_parameter['prefix'], test_parameter[masterId]['token'], 
                        test_parameter[masterId]['nonce'], test_parameter[masterId]['nickname'], pwd)
    #check中的資料先以第一層為主，之後再看下層資料
    testData = [
        # (
        #     '驗證密碼房，官方場控、一般場控及user',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 0),                        
        #                 ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': test_parameter['track0012']['trueloveId']}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #                 ('live_room:' + str(roomNo), 'kickout_admin', {'targetUserId': test_parameter['track0012']['trueloveId']}, 4),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 2),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 2),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 4),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'lv000', 'wait': 3, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 2),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 4),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 5, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 2),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0013', 'wait': 7, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 2),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'room_in_bcst', 
        #             'position': 3,
        #             'check': 
        #             [
        #             ]
        #         },
        #         {
        #             'index': 'track0011', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']}, 
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'lv000', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['lv000']['id']}, 
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']}, 
        #             ]
        #         },
        #     ]
        # ),

        # (
        #     '驗證基本入房，發訊息及離房', #3365
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 30),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'message', {'content': '一般訊息欄位輸入的訊息'}, 1),
        #                 ('live_room:' + str(roomNo), 'barrage', {'barrageId': 1, 'content': '我是barrage的訊息'}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 30),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 4),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 2, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter[masterId]['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0013', 'wait': 3, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd, 'action': 'reconnect'}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 5),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0014', 'wait': 4, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd, 'action': 'reconnect'}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 5),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0015', 'wait': 5, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd, 'action': 'reconnect'}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 5),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'barrage_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['room', 'totalGiftPoints'], 'value': test_parameter[masterId]['dailyPoints'] + 119}, 
        #                 {'key': ['room', 'liveRanking'], 'value': 1}, 
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter[masterId]['dailyPoints'] + 119}, 
        #                 {'key': ['barrage', 'id'], 'value': 1}, 
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['barrage', 'points'], 'value': 119}, 
        #                 {'key': ['content'], 'value': '我是barrage的訊息'}, 
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']}, 
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},  
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']}, 
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},  
        #             ]
        #         },
        #         {
        #             'index': masterId, 
        #             'event': 'message_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 一般訊息欄位輸入的訊息'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 一般訊息欄位輸入的訊息'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 一般訊息欄位輸入的訊息'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'barrage', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['room', 'totalGiftPoints'], 'value': test_parameter[masterId]['dailyPoints'] + 119}, 
        #                 {'key': ['room', 'liveRanking'], 'value': 1}, 
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter[masterId]['dailyPoints'] + 119}, 
        #                 {'key': ['barrage', 'id'], 'value': 1}, 
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['barrage', 'points'], 'value': 119}, 
        #                 {'key': ['content'], 'value': '我是barrage的訊息'}, 
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']}, 
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter[masterId]['nickname']},  
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0011']['id']}, 
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},  
        #             ]
        #         },
        #         {
        #             'index': 'track0012', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']}, 
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']}, 
        #                 {'key': ['room', 'totalCount'], 'value': 2}, 
        #                 {'key': ['room', 'totalGiftPoints'], 'value': test_parameter[masterId]['dailyPoints'] + 119}, 
        #                 {'key': ['room', 'liveRanking'], 'value': 1}, 
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter[masterId]['dailyPoints'] + 119}, 
        #             ]
        #         },
        #     ]
        # ),

        # (
        #     '驗證nickname或發彈幕的訊息內容有禁詞,直播主及發送本人應可看到：', #3764
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 10),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 4),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'message', {'content': '輸入的訊息有詐騙'}, 1),
        #                 ('live_room:' + str(roomNo), 'barrage', {'barrageId': 1, 'content': 'barrage的訊息有欺騙'}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 5),
        #             ], 'sleep': 1 
        #         },
        #         {'user': 'track0020', 'wait': 3, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'message', {'content': 'nickname有forbidden一般訊息'}, 1),
        #                 ('live_room:' + str(roomNo), 'barrage', {'barrageId': 1, 'content': 'nickname有forbidden的barrage'}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 2),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0014', 'wait': 8, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 2),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [ 
        #         {
        #             'index': masterId, 
        #             'event': 'room_in_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0014']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0014']['nickname']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0014', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0014']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0014']['nickname']},
        #                 {'key': ['room', 'description'], 'value': 'master10開播，歡迎入群'},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'room_in_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0014']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0014']['nickname']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'barrage', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['barrage', 'id'], 'value': 1},
        #                 {'key': ['barrage', 'points'], 'value': 119},
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['content'], 'value': 'barrage的訊息有欺騙'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #             ]
        #         },             
        #         {
        #             'index': 'track0020', 
        #             'event': 'message', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} nickname有forbidden一般訊息'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} nickname有forbidden一般訊息'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} nickname有forbidden一般訊息'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0020']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0020']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'message_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #             ]
        #         },

        #         {
        #             'index': masterId, 
        #             'event': 'barrage', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['barrage', 'id'], 'value': 1},
        #                 {'key': ['barrage', 'points'], 'value': 119},
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['content'], 'value': 'nickname有forbidden的barrage'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0020']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0020']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'barrage', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['barrage', 'id'], 'value': 1},
        #                 {'key': ['barrage', 'points'], 'value': 119},
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['content'], 'value': 'barrage的訊息有欺騙'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #             ]
        #         },             

        #         {
        #             'index': masterId, 
        #             'event': 'barrage_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'room_in_bcst', 
        #             'position': 2,
        #             'check': 
        #             [
        #             ]
        #         },
        #     ]
        # ),

        # (
        #     '驗證基本入房, rconnect, 離房', #4383
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 30),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 30),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 4),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 2, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 30),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0013', 'wait': 3, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {'code': ''}, 30),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd, 'action': 'reconnect'}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 5),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0014', 'wait': 4, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd, 'action': 'reconnect'}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd, 'action': 'reconnect'}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd, 'action': 'reconnect'}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 5),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [ 
        #         {
        #             'index': 'track0014', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0014']['id']}, 
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']}, 
        #                 {'key': ['room', 'totalCount'], 'value': 4}, 
        #             ]
        #         },
        #     ]
        # ),


        # ('新增,移除場控及場控列表',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': test_parameter['track0012']['trueloveId']}, 1),
        #                 ('live_room:' + str(roomNo), 'get_admins', {}, 1),
        #                 ('live_room:' + str(roomNo), 'kickout_admin', {'targetUserId': test_parameter['track0012']['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'get_admins', {}, 1),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 3),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'admins_got', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['admins'], 'value': []},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'admins_got', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['admins'], 'value': [test_parameter['track0012']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'admin_pickedup_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['targetUserId'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['admins'], 'value': [test_parameter['track0012']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'admin_kickedout_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['targetUserId'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['admins'], 'value': []},
        #             ]
        #         },             
        #     ]
        # ),

        # ('在禁言名單內message不會廣播但barrage要可正常播放', #3517 #3797 #3703
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'mute_audience', {'targetUserId': test_parameter['track0013']['id']}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 7),
        #                 ('live_room:' + str(roomNo), 'unmute_audience', {'targetUserId': test_parameter['track0013']['id']}, 0),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 3),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0013', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'message', {'content': '我被禁言，別人看不到'}, 2),
        #                 ('live_room:' + str(roomNo), 'barrage', {'barrageId': 1,'content': 'barrage cannot broadcast since I am mute'}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 3),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'track0013', 
        #             'event': 'barrage_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['barrage', 'id'], 'value': 1},
        #                 {'key': ['barrage', 'points'], 'value': 119},
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['content'], 'value': 'barrage cannot broadcast since I am mute'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0013']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #                 {'key': ['room', 'liveRankingPoints'], 'value': 119},
        #                 {'key': ['room', 'totalGiftPoints'], 'value': 119},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'audience_muted_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': [test_parameter['track0013']['id']]},
        #                 {'key': ['content', 'en'], 'value': '{targetUser.name}已被{fromUser.name} Mute success'},
        #                 {'key': ['content', 'zh'], 'value': '{targetUser.name}已被{fromUser.name} 禁言成功'},
        #                 {'key': ['content', 'ja'], 'value': '{targetUser.name}已被{fromUser.name} ミュートの成功'},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'audience_unmute_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': []},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'message_bcst', 
        #             'position': 0,
        #             'check': 
        #             []
        #         },            
        #         {
        #             'index': masterId, 
        #             'event': 'barrage_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['barrage', 'id'], 'value': 1},
        #                 {'key': ['barrage', 'points'], 'value': 119},
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['content'], 'value': 'barrage cannot broadcast since I am mute'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0013']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter[masterId]['nickname']},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #                 {'key': ['room', 'liveRankingPoints'], 'value': 119},
        #                 {'key': ['room', 'totalGiftPoints'], 'value': 119},

        #             ]
        #         },            
        #     ]
        # ),

        # ('禁言,官方場控不可被禁言，一般場控被禁言後可以自己解除禁言',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 # ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': test_parameter['track0011']['trueloveId']}, 0),
        #                 # ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': test_parameter['track0012']['trueloveId']}, 0),
        #                 ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': '177'}, 0),
        #                 ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': '11693'}, 0),
        #                 ('live_room:' + str(roomNo), 'mute_audience', {'targetUserId': test_parameter['lv000']['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 7),
        #                 ('live_room:' + str(roomNo), 'kickout_admin', {'targetUserId': test_parameter['track0012']['id']}, 0),
        #                 ('live_room:' + str(roomNo), 'kickout_admin', {'targetUserId': test_parameter['track0011']['id']}, 0),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 8),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'mute_audience', {'targetUserId': test_parameter['track0012']['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 8),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 2, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'message', {'content': 'still in mute, cannot send message'},0),
        #                 ('live_room:' + str(roomNo), 'unmute_audience', {'targetUserId': test_parameter['track0012']['id']}, 2),
        #                 ('live_room:' + str(roomNo), 'message', {'content': '自己解除禁言，發言成功'}, 2),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 8),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'lv000', 'wait': 3, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'mute_audience', {'targetUserId': test_parameter['track0011']['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 4),
        #                 ('live_room:' + str(roomNo), 'unmute_audience', {'targetUserId': test_parameter['track0011']['id']}, 1),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'audience_muted_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': [test_parameter['track0011']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'audience_muted_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': [test_parameter['track0012']['id']]},
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} Mute success'}, 
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 禁言成功'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} ミュートの成功'},                
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'audience_unmute_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': []},                    ]
        #         },            
        #         {
        #             'index': masterId, 
        #             'event': 'message_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0012']['nickname']},  
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},   
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 自己解除禁言，發言成功'}, 
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 自己解除禁言，發言成功'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 自己解除禁言，發言成功'},                
        #             ]
        #         },            
        #     ]
        # ),

        # ('Ban踢出；一般場控可以ban user',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': test_parameter['track0012']['trueloveId']}, 0),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 # ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 3),
        #                 ('live_room:' + str(roomNo), 'get_violation', {}, 0),
        #                 ('live_room:' + str(roomNo), 'unban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'action': 'reconnect'}, 3),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter[masterId]['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'track0012', 
        #             'event': 'violation_got', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['muteAudience'], 'value': []},
        #                 {'key': ['banAudience'], 'value': [test_parameter['track0011']['id']]},
        #             ]
        #         },            
                # {
                #     'index': 'track0012', 
                #     'event': 'audience_banned_bcst', 
                #     'position': 0,
                #     'check': 
                #     [
                #         {'key': ['roomId'], 'value': roomNo},
                #         {'key': ['content', 'en'], 'value': '{targetUser.name} Successfully kicked out'},
                #         {'key': ['content', 'zh'], 'value': '{targetUser.name} 被踢出成功'},
                #         {'key': ['content', 'ja'], 'value': '{targetUser.name} 成功裏に追い出された'},
                #         {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
                #         {'key': ['targetUser', 'id'], 'value': test_parameter['track0011']['id']},
                #         {'key': ['banAudiences'], 'value': [test_parameter['track0011']['id']]},
                #     ]
                # },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'audience_unbanned_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['banAudiences'], 'value': []},
        #             ]
        #         },             
        #     ]
        # ),

        # ('Ban踢出；無法踢出官方場控及房主，被踢出後的user無法再進入該直播主所有開播的聊天室',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter['track0012']['id'], 'reasonId': 8}, 2),
        #                 ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter['lv000']['id'], 'reasonId': 8}, 1),
        #                 ('live_room:' + str(roomNo), 'get_violation', {}, 1),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 9),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0011', 'wait': 6, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 3),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'lv000', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter[masterId]['id'], 'reasonId': 8}, 0),
        #                 ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 2),
        #                 ('live_room:' + str(roomNo), 'unban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 2),
        #                 ('live_room:' + str(roomNo), 'unban_audience', {'targetUserId': test_parameter['track0012']['id'], 'reasonId': 8}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'violation_got', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['muteAudience'], 'value': []},
        #                 {'key': ['banAudience'], 'value': [test_parameter['track0012']['id'], test_parameter['track0011']['id']]},
        #             ]
        #         },            
        #         {
        #             'index': masterId, 
        #             'event': 'audience_banned_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '{targetUser.name} Successfully kicked out'},
        #                 {'key': ['content', 'zh'], 'value': '{targetUser.name} 被踢出成功'},
        #                 {'key': ['content', 'ja'], 'value': '{targetUser.name} 成功裏に追い出された'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['lv000']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['banAudiences'], 'value': [test_parameter['track0012']['id'], test_parameter['track0011']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'audience_banned_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '{targetUser.name} Successfully kicked out'},
        #                 {'key': ['content', 'zh'], 'value': '{targetUser.name} 被踢出成功'},
        #                 {'key': ['content', 'ja'], 'value': '{targetUser.name} 成功裏に追い出された'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['banAudiences'], 'value': [test_parameter['track0012']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'audience_unbanned_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['banAudiences'], 'value': []},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'room_in_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} Come in~'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 進來了～'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 入って〜'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},
        #             ]
        #         },             
        #     ]
        # ),


        # ('送禮、熱度及marquee',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 15),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter[masterId]['id'],
        #                     'giftId': '55f0ac47-9979-441f-8c49-23d5db7c2898', 'count': 40}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 3),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter[masterId]['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 0),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter[masterId]['id'],
        #                     'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'count': 10}, 2),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 2),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'gift_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['gift', 'id'], 'value': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60'},
        #                 {'key': ['gift', 'name', 'zh'], 'value': '幸福燃點'},
        #                 {'key': ['gift', 'count'], 'value': 2},
        #                 {'key': ['gift', 'multiple'], 'value': False},
        #                 {'key': ['gift', 'points'], 'value': 300000},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'marquee', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 3},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'marquee', 
        #             'position': 1,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 2},

        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'marquee', 
        #             'position': 2,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 3},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'marquee', 
        #             'position': 3,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 1},

        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter[masterId]['dailyPoints'] + 550000},
        #                 {'key': ['room', 'totalGiftPoints'], 'value': 550000},
        #                 {'key': ['room', 'userGiftPoints'], 'value': 400000},

        #             ]
        #         },             
        #     ]

        # ),


        # ('用戶分享直播間訊息deep link #3668 #3768 #3779',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 12),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'share', {}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 2),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 4, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'share', {}, 3),
        #                 ('live_room:' + str(roomNo), 'share', {}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 0),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0020', 'wait': 10, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'share', {}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 1),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'track0011', 
        #             'event': 'shared_bcst', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'shared_bcst', 
        #             'position': 1,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'shared_bcst', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'shared_bcst', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0020', 
        #             'event': 'shared', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0020']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #     ]

        # ),

        # ('直播主timeout應主動將user請出直播間並關閉該房 #3669',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 4),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 30),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 30),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 30),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 30),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'track0011', 
        #             'event': 'room_closed', 
        #             'position': 0,
        #             'check': [
        #                 {'key': [], 'value': None},
        #             ]
        #         },             
        #     ]

        # ),

        # ('暱稱中含有禁詞，送禮時直播主應收到通知，但其他用戶不會看到.一併驗證全域跑馬燈及熱度 #3808',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 15),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 1),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 1),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0020', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter[masterId]['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 2),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'gift', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['gift', 'id'], 'value': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60'},
        #                 {'key': ['gift', 'name', 'zh'], 'value': '幸福燃點'},
        #                 {'key': ['gift', 'count'], 'value': 2},
        #                 {'key': ['gift', 'multiple'], 'value': False},
        #                 {'key': ['gift', 'points'], 'value': 300000},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0020']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0020', 
        #             'event': 'gift', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['gift', 'id'], 'value': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60'},
        #                 {'key': ['gift', 'name', 'zh'], 'value': '幸福燃點'},
        #                 {'key': ['gift', 'count'], 'value': 2},
        #                 {'key': ['gift', 'multiple'], 'value': False},
        #                 {'key': ['gift', 'points'], 'value': 300000},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0020']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'marquee', 
        #             'position': 1,
        #             'check': []
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'marquee', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter[masterId]['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 3},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'gift_bcst', 
        #             'position': 0,
        #             'check': []
        #         },             
        #     ]
        # ),

        # ('追蹤&Block封鎖；無法封鎖官方場控，被封鎖後的user無法再進入該直播主所有開播的聊天室',
        #     [
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'block_audience', {'targetUserId': test_parameter['lv000']['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'block_audience', {'targetUserId': test_parameter['track0012']['id']}, 5),
        #                 ('live_room:' + str(roomNo), 'get_violation', {}, 1),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 15),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'track', {'targetUserId': test_parameter[masterId]['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 6),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0011', 'wait': 5, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0020', 'wait': 2, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'track', {'targetUserId': test_parameter[masterId]['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'lv000', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'block_audience', {'targetUserId': test_parameter['track0011']['id']}, 7),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 10),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterId, 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['response', 'err'], 'value': 'TARGET_USER_IS_LIVE_CONTROLLER'}
        #             ]
        #         },             

        #         {
        #             'index': masterId, 
        #             'event': 'audience_blocked_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '{targetUser.name} 已被 {fromUser.name}封鎖成功'},
        #                 {'key': ['content', 'zh'], 'value': '{targetUser.name} 已被 {fromUser.name}封鎖成功'},
        #                 {'key': ['content', 'ja'], 'value': '{targetUser.name} 已被 {fromUser.name}封鎖成功'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0012']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'audience_blocked_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '{targetUser.name} 已被 {fromUser.name}封鎖成功'},
        #                 {'key': ['content', 'zh'], 'value': '{targetUser.name} 已被 {fromUser.name}封鎖成功'},
        #                 {'key': ['content', 'ja'], 'value': '{targetUser.name} 已被 {fromUser.name}封鎖成功'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0012']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'tracked_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 追蹤了 {targetUser.name}！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 追蹤了 {targetUser.name}！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 追蹤了 {targetUser.name}！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'audience_blocked', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': 'Violated the rules and was kicked out of the room'},
        #                 {'key': ['content', 'zh'], 'value': '違反規定，被踢出房間'},
        #                 {'key': ['content', 'ja'], 'value': 'ルールに違反し、部屋から追い出された'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0012']['id']},
        #             ]
        #         },             
        #         {
        #             'index': masterId, 
        #             'event': 'room_in_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} Come in~'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 進來了～'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 入って〜'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},
        #             ]
        #         },             
        #     ]
        # ),


    #     ('message追加不同的message type',  #3602
    #         [
    #             {'user': masterId, 'wait': 0, 'action': [
    #                     ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
    #                     ('live_room:' + str(roomNo), 'ping', {}, 30),
    #                     ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 15),
    #                 ], 'sleep': 2
    #             },
    #             {'user': 'track0011', 'wait': 1, 'action': [
    #                     ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
    #                     ('live_room:' + str(roomNo), 'message', {'content': 'I am track0011'}, 1),
    #                     ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 2),
    #                 ], 'sleep': 1
    #             },
    #             {'user': 'track0020', 'wait': 3, 'action': [
    #                     ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
    #                     ('live_room:' + str(roomNo), 'message', {'content': 'I am track0020'}, 1),
    #                     ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 1),
    #                 ], 'sleep': 1
    #             },
    #         ],
    #         [
    #             {
    #                 'index': masterId, 
    #                 'event': 'message_bcst', 
    #                 'position': 0,
    #                 'check': 
    #                 [
    #                     {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},  
    #                     {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},   
    #                     {'key': ['content', 'en'], 'value': '{fromUser.name} I am track0011'}, 
    #                     {'key': ['content', 'zh'], 'value': '{fromUser.name} I am track0011'},
    #                     {'key': ['content', 'ja'], 'value': '{fromUser.name} I am track0011'},           
    #                     {'key': ['messageType'], 'value': 'conversation'}     
    #                 ]
    #             },
    #             {
    #                 'index': 'track0020', 
    #                 'event': 'message', 
    #                 'position': 0,
    #                 'check': [
    #                     {'key': ['fromUser', 'name'], 'value': test_parameter['track0020']['nickname']},  
    #                     {'key': ['fromUser', 'id'], 'value': test_parameter['track0020']['id']},   
    #                     {'key': ['content', 'en'], 'value': '{fromUser.name} I am track0020'}, 
    #                     {'key': ['content', 'zh'], 'value': '{fromUser.name} I am track0020'},
    #                     {'key': ['content', 'ja'], 'value': '{fromUser.name} I am track0020'},           
    #                     {'key': ['messageType'], 'value': 'conversation'}     
    #                 ]
    #             },         
    #             {
    #                 'index': 'track0020', 
    #                 'event': 'message', 
    #                 'position': 1,
    #                 'check': [
    #                     {'key': ['fromUser', 'name'], 'value': '小祕書'},  
    #                     {'key': ['fromUser', 'id'], 'value': '1234-5678'},   
    #                     {'key': ['content', 'en'], 'value': '平台禁止任何代儲(充)值服務'}, 
    #                     {'key': ['content', 'zh'], 'value': '平台禁止任何代儲(充)值服務'},
    #                     {'key': ['content', 'ja'], 'value': '平台禁止任何代儲(充)值服務'},           
    #                     {'key': ['messageType'], 'value': 'system'}     
    #                 ]
    #             },             
    
    #         ]

    #     ),

        # ('過年紅包活動，暖場、抽奬', #4619~4615  
        #     [       
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 0), 
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'track0011', 'wait': 2, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 1}, 1),
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 1}, 3),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0012', 'wait': 30, 'action': [ #進來時在暖場
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 0),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 100, 'action': [ #抽奬已結束
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 5), 
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0014', 'wait': 3, 'action': [ #在聲聊房轉進來抽奬
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'pin', {}, 40), 
        #                 ('vc_room:1', 'phx_leave', {}, 20),
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 5), 
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },

        #     ],  
        #     [
        #         {'index': 'track0013', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'], 'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'], 'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 1, 'check': [
        #                 {'key': ['progress'], 'value': 'WARM_UP'},
        #                 {'key': ['gatherPoints'],  'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'READY'},
        #                 {'key': ['gatherPoints'],  'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': True},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 4, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 0},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 3, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 15000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': ['response', 'err'], 'value': 'LUCKYMONEY_LOTTERY_UNAVAILABLE'},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': ['response', 'err'], 'value': 'LUCKYMONEY_GAINED'},
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'luckymoney_ready_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': True},
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'luckymoney_warm_up_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #     ]
        # ),

        # ('過年紅包活動，重新開播重新計算（含結束）', #4621
        #     [       
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 0), 
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'track0011', 'wait': 3, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 2}, 1), #15,000
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0012', 'wait': 30, 'action': [ #進來時在暖場
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:' + str(roomNo), 'barrage', {'barrageId': 1, 'content': 'barrage也視同禮物🎁'}, 1),                        
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 100, 'action': [ #抽奬已結束
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0014', 'wait': 1, 'action': [ #在聲聊房轉進來抽奬
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'ping', {}, 35), 
        #                 ('vc_room:1', 'phx_leave', {}, 28),
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 5), 
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },

        #     ],  
        #     [
        #         {'index': 'track0013', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'], 'value': 30119},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 3, 'check': [
        #                 {'key': ['progress'], 'value': 'WARM_UP'},
        #                 {'key': ['gatherPoints'],  'value': 30119},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'READY'},
        #                 {'key': ['gatherPoints'],  'value': 30119},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 5, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 0},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': ['response', 'err'], 'value': 'LUCKYMONEY_LOTTERY_UNAVAILABLE'},
        #             ]
        #         },
        #         {'index': masterId, 'event': 'luckymoney_ready_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': True},
        #             ]
        #         },
        #         {'index': masterId, 'event': 'luckymoney_warm_up_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #     ]
        # ),

        # ('過年紅包活動，暖場、抽奬', #4619~4615  
        #     [       
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 0), 
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'track0011', 'wait': 2, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 1}, 1),
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 1}, 3),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0012', 'wait': 30, 'action': [ #進來時在暖場
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 0),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 100, 'action': [ #抽奬已結束
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 5), 
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0014', 'wait': 3, 'action': [ #在聲聊房轉進來抽奬
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'pin', {}, 40), 
        #                 ('vc_room:1', 'phx_leave', {}, 20),
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 5), 
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },

        #     ],  
        #     [
        #         {'index': 'track0013', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'], 'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'], 'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 1, 'check': [
        #                 {'key': ['progress'], 'value': 'WARM_UP'},
        #                 {'key': ['gatherPoints'],  'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'READY'},
        #                 {'key': ['gatherPoints'],  'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': True},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 4, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 0},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 3, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 15000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': ['response', 'err'], 'value': 'LUCKYMONEY_LOTTERY_UNAVAILABLE'},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': ['response', 'err'], 'value': 'LUCKYMONEY_GAINED'},
        #             ]
        #         },
        #         {'index': masterId, 'event': 'luckymoney_ready_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': True},
        #             ]
        #         },
        #         {'index': masterId, 'event': 'luckymoney_warmup_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #     ]
        # ),

        ('過年紅包活動，重新開播重新計算（含結束）', #4621; 新秀主播
            [       
                {'user': masterId, 'wait': 0, 'action': [
                        ('live_room:%d'%roomNo, 'phx_join', {}, 0), 
                        ('live_room:%d'%roomNo, 'ping', {}, 35),
                        ('live_room:%d'%roomNo, 'ping', {}, 35),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
                    ], 'sleep': 7
                }, 
                {'user': 'track0019', 'wait': 3, 'action': [
                        ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
                        ('live_room:%d'%roomNo, 'gift', {'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'targetUserId': test_parameter[masterId]['id'], 'count': 2}, 1), #150,000
                        ('live_room:%d'%roomNo, 'ping', {}, 30),
                        ('live_room:%d'%roomNo, 'ping', {}, 30),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
                    ], 'sleep': 3
                },
                {'user': 'track0018', 'wait': 30, 'action': [ #進來時在暖場
                        ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
                        ('live_room:' + str(roomNo), 'barrage', {'barrageId': 1, 'content': 'barrage也視同禮物🎁'}, 1),                        
                        ('live_room:%d'%roomNo, 'ping', {}, 35),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'ping', {}, 40),
                        ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
                    ], 'sleep': 3
                },
                # {'user': 'track0013', 'wait': 100, 'action': [ #抽奬已結束
                #         ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
                #         ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'ping', {}, 30),
                #         ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                #         ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
                #     ], 'sleep': 3
                # },
                # {'user': 'track0014', 'wait': 1, 'action': [ #在聲聊房轉進來抽奬
                #         ('vc_room:1', 'phx_join', {}, 1), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'ping', {}, 35), 
                #         ('vc_room:1', 'phx_leave', {}, 25),
                #         ('live_room:%d'%roomNo, 'phx_join', {}, 5), 
                #         ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
                #         ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
                #     ], 'sleep': 3
                # },
                # {'user': 'track0015', 'wait': 540, 'action': [ #抽奬已全部結束
                #         ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
                #         ('live_room:%d'%roomNo, 'phx_leave', {}, 5),
                #     ], 'sleep': 3
                # },

            ],  
            [
                # {'index': 'track0014', 'event': 'luckymoney_data_changed_bcst', 'position': 1, 'check': [
                #         {'key': ['progress'], 'value': 'READY'},
                #         {'key': ['gatherPoints'],  'value': 300119},
                #         {'key': ['targetPoints'], 'value': 300000},
                #         {'key': ['displayed'], 'value': True},
                #         {'key': ['clicked'], 'value': True},
                #     ]
                # },
                # {
                #     'index': 'track0015', 'event': 'luckymoney_data_changed_bcst', 'position': 1, 'check': []
                # },
                # {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
                #         {'key': ['level'], 'value': 1},
                #         {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                #         {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                #         {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
                #         {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
                #     ]
                # },
                # {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 1, 'check': [
                #         {'key': ['level'], 'value': 1},
                #         {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                #         {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                #         {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
                #         {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
                #     ]
                # },
                # {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 2, 'check': [
                #         {'key': ['level'], 'value': 1},
                #         {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                #         {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                #         {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
                #         {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
                #     ]
                # },
                # {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 3, 'check': [
                #         {'key': ['level'], 'value': 1},
                #         {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                #         {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                #         {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
                #         {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
                #     ]
                # },
                # {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 4, 'check': [
                #         {'key': ['level'], 'value': 1},
                #         {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                #         {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                #         {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
                #         {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
                #     ]
                # },
                {'index': 'track0019', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
                        {'key': ['level'], 'value': 1},
                        {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
                        {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
                    ]
                },
                {'index': 'track0019', 'event': 'luckymoney_data_changed_bcst', 'position': 5, 'check': [
                        {'key': ['progress'], 'value': 'GATHER'},
                        {'key': ['gatherPoints'],  'value': 0},
                        {'key': ['targetPoints'], 'value': 30000},
                        {'key': ['displayed'], 'value': True},
                        {'key': ['clicked'], 'value': False},
                    ]
                },
                {'index': 'track0019', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
                        {'key': ['displayed'], 'value': True},
                        {'key': ['clicked'],  'value': False},
                    ]
                },
                # {'index': 'track0013', 'event': 'phx_reply', 'position': 0, 'check': [
                #         {'key': ['response', 'err'], 'value': 'LUCKYMONEY_LOTTERY_UNAVAILABLE'},
                #     ]
                # },
                # {'index': 'track0013', 'event': 'luckymoney_finish_bcst', 'position': 0, 'check': [
                #         {'key': ['displayed'], 'value': False},
                #         {'key': ['displayed'], 'value': False},
                #     ]
                # },
                # {'index': masterId, 'event': 'luckymoney_ready_bcst', 'position': 0, 'check': [
                #         {'key': ['displayed'], 'value': True},
                #         {'key': ['clicked'],  'value': True},
                #     ]
                # },
                # {'index': masterId, 'event': 'luckymoney_warmup_bcst', 'position': 0, 'check': [
                #         {'key': ['displayed'], 'value': True},
                #         {'key': ['clicked'],  'value': False},
                #     ]
                # },
            ]
        ),
 
        # ('過年紅包活動，暖場、抽奬', #4619~4615， 女神等級與新秀不同
        #     [       
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 0), 
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'track0011', 'wait': 2, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 3}, 1),
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 1}, 3),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 30),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0014', 'wait': 1, 'action': [ #在聲聊房轉進來抽奬
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'pin', {}, 40), 
        #                 ('vc_room:1', 'phx_leave', {}, 20),
        #             ], 'sleep': 3
        #         },
        #     ],  
        #     [
        #         {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 3, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 0},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 2, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 45000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 1, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 60000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 60000},
        #                 {'key': ['targetPoints'], 'value': 100000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': masterId, 'event': 'luckymoney_ready_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': True},
        #             ]
        #         },
        #         {'index': masterId, 'event': 'luckymoney_warmup_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #     ]
        # ),

        # ('過年紅包活動，暖場、抽奬', #4619~4615， 女神等級與新秀不同
        #     [       
        #         {'user': masterId, 'wait': 0, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 0), 
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 35),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'track0011', 'wait': 2, 'action': [
        #                 ('live_room:%d'%roomNo, 'phx_join', {}, 1), 
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 1}, 1),
        #                 ('live_room:%d'%roomNo, 'gift', {'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'targetUserId': test_parameter[masterId]['id'], 'count': 1}, 3),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'ping', {}, 30),
        #                 ('live_room:%d'%roomNo, 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('live_room:%d'%roomNo, 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #     ],  
        #     [
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter[masterId]['id']},
        #                 {'key': ['url'], 'value': 'xtars://room/%d'%roomNo},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 3, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 0},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 2, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 15000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 1, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 30000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 30000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'master11', 'event': 'luckymoney_ready_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': True},
        #             ]
        #         },
        #         {'index': 'master11', 'event': 'luckymoney_warm_up_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #     ]
        # ),

    ]   

    return testData