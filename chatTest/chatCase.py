from . import misc
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

def getTestData(test_parameter):
    pwd = ''
    roomNo = getRoomId(test_parameter['prefix'], test_parameter['master10']['token'], 
                        test_parameter['master10']['nonce'], test_parameter['master10']['nickname'], pwd)
    #check中的資料先以第一層為主，之後再看下層資料
    testData = [
        # (
        #     '驗證密碼房，官方場控、一般場控及user',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
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
        #             'index': 'master10', 
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
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'lv000', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['lv000']['id']}, 
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']}, 
        #             ]
        #         },
        #     ]
        # ),

        # (
        #     '驗證基本入房，發訊息及離房', #3365
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 0),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'message', {'content': '一般訊息欄位輸入的訊息'}, 1),
        #                 ('live_room:' + str(roomNo), 'barrage', {'barrageId': 1, 'content': '我是barrage的訊息'}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 4),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 5, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': pwd}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 2),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'barrage_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['room', 'totalGiftPoints'], 'value': test_parameter['master10']['dailyPoints'] + 119}, 
        #                 {'key': ['room', 'liveRanking'], 'value': 1}, 
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter['master10']['dailyPoints'] + 119}, 
        #                 {'key': ['barrage', 'id'], 'value': 1}, 
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['barrage', 'points'], 'value': 119}, 
        #                 {'key': ['content'], 'value': '我是barrage的訊息'}, 
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']}, 
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},  
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']}, 
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter['master10']['nickname']},  
        #             ]
        #         },
        #         {
        #             'index': 'master10', 
        #             'event': 'message_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 一般訊息欄位輸入的訊息'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 一般訊息欄位輸入的訊息'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 一般訊息欄位輸入的訊息'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0011']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter['master10']['nickname']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'barrage', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['room', 'totalGiftPoints'], 'value': test_parameter['master10']['dailyPoints'] + 119}, 
        #                 {'key': ['room', 'liveRanking'], 'value': 1}, 
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter['master10']['dailyPoints'] + 119}, 
        #                 {'key': ['barrage', 'id'], 'value': 1}, 
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['barrage', 'points'], 'value': 119}, 
        #                 {'key': ['content'], 'value': '我是barrage的訊息'}, 
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']}, 
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['master10']['nickname']},  
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0011']['id']}, 
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter['master10']['nickname']},  
        #             ]
        #         },
        #         {
        #             'index': 'track0012', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']}, 
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']}, 
        #                 {'key': ['room', 'totalCount'], 'value': 2}, 
        #                 {'key': ['room', 'totalGiftPoints'], 'value': test_parameter['master10']['dailyPoints'] + 119}, 
        #                 {'key': ['room', 'liveRanking'], 'value': 1}, 
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter['master10']['dailyPoints'] + 119}, 
        #             ]
        #         },
        #     ]
        # ),

        # (
        #     '驗證nickname或發訊的訊息內容有禁詞,check room_in_bcst, message_bcst, barrage_bcst',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
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
        #             'index': 'master10', 
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
        #                 {'key': ['room', 'totalGiftPoints'], 'value': 238},
        #                 {'key': ['room', 'liveRankingPoints'], 'value': 238},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
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
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter['master10']['nickname']},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #                 {'key': ['room', 'liveRankingPoints'], 'value': 238},
        #                 {'key': ['room', 'totalGiftPoints'], 'value': 238},
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
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter['master10']['nickname']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'message_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #             ]
        #         },
        #         {
        #             'index': 'master10', 
        #             'event': 'barrage_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'room_in_bcst', 
        #             'position': 2,
        #             'check': 
        #             [
        #             ]
        #         },
        #     ]
        # ),

        # ('新增,移除場控及場控列表',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
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
        #             'index': 'master10', 
        #             'event': 'admins_got', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['admins'], 'value': []},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'admins_got', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['admins'], 'value': [test_parameter['track0012']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
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
        #             'index': 'master10', 
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

        # ('在禁言名單內message及barrage皆不會廣播', #3517
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
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
        #             'event': 'barrage', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['barrage', 'id'], 'value': 1},
        #                 {'key': ['barrage', 'points'], 'value': 119},
        #                 {'key': ['barrage', 'type'], 'value': 'general'},
        #                 {'key': ['content'], 'value': 'barrage cannot broadcast since I am mute'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['fromUser', 'name'], 'value': test_parameter['track0013']['nickname']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
        #                 {'key': ['targetUser', 'name'], 'value': test_parameter['master10']['nickname']},
        #                 {'key': ['room', 'liveRanking'], 'value': 1},
        #                 {'key': ['room', 'liveRankingPoints'], 'value': 119},
        #                 {'key': ['room', 'totalGiftPoints'], 'value': 119},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'audience_muted_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': [test_parameter['track0013']['id']]},
        #                 {'key': ['content', 'en'], 'value': '@{targetUser.name}已被@{fromUser.name} Mute success'},
        #                 {'key': ['content', 'zh'], 'value': '@{targetUser.name}已被@{fromUser.name} 禁言成功'},
        #                 {'key': ['content', 'ja'], 'value': '@{targetUser.name}已被@{fromUser.name} ミュートの成功'},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'audience_unmute_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': []},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'message_bcst', 
        #             'position': 0,
        #             'check': 
        #             []
        #         },            
        #         {
        #             'index': 'master10', 
        #             'event': 'barrage_bcst', 
        #             'position': 0,
        #             'check': 
        #             []
        #         },            
        #     ]
        # ),

        # ('禁言,官方場控不可被禁言，一般場控被禁言後可以自己解除禁言',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
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
        #             'index': 'master10', 
        #             'event': 'audience_muted_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': [test_parameter['track0011']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
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
        #             'index': 'master10', 
        #             'event': 'audience_unmute_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['muteAudiences'], 'value': []},                    ]
        #         },            
        #         {
        #             'index': 'master10', 
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
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'pickup_admin', {'xtarsId': test_parameter['track0012']['trueloveId']}, 0),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 1),
        #                 ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 1),
        #                 ('live_room:' + str(roomNo), 'get_violation', {}, 0),
        #                 ('live_room:' + str(roomNo), 'unban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #             ], 'sleep': 5
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
        #         {
        #             'index': 'track0012', 
        #             'event': 'audience_banned_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '{targetUser.name} Successfully kicked out'},
        #                 {'key': ['content', 'zh'], 'value': '{targetUser.name} 被踢出成功'},
        #                 {'key': ['content', 'ja'], 'value': '{targetUser.name} 成功裏に追い出された'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['banAudiences'], 'value': [test_parameter['track0011']['id']]},
        #             ]
        #         },             
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
        #         {'user': 'master10', 'wait': 0, 'action': [
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
        #                 ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter['master10']['id'], 'reasonId': 8}, 0),
        #                 ('live_room:' + str(roomNo), 'ban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 2),
        #                 ('live_room:' + str(roomNo), 'unban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 2),
        #                 ('live_room:' + str(roomNo), 'unban_audience', {'targetUserId': test_parameter['track0012']['id'], 'reasonId': 8}, 3),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 3),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
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
        #             'index': 'master10', 
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
        #             'index': 'master10', 
        #             'event': 'audience_banned_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '{targetUser.name} Successfully kicked out'},
        #                 {'key': ['content', 'zh'], 'value': '{targetUser.name} 被踢出成功'},
        #                 {'key': ['content', 'ja'], 'value': '{targetUser.name} 成功裏に追い出された'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['master10']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['banAudiences'], 'value': [test_parameter['track0012']['id']]},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'audience_unbanned_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['banAudiences'], 'value': []},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
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

        # ('Block封鎖，僅直播主本身可以執行。且有追蹤會取消追蹤關係',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'block_audience', {'targetUserId': test_parameter['track0013']['id']}, 1),
        #                 ('live_room:' + str(roomNo), 'block_audience', {'targetUserId': test_parameter['track0011']['id']}, 3),
        #                 ('live_room:' + str(roomNo), 'get_violation', {}, 0),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'track', {'targetUserId': test_parameter['master10']['id']}, 0),
        #                 ('live_room:' + str(roomNo), 'pin', {}, 4),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0013', 'wait': 2, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 4, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'track', {'targetUserId': test_parameter['master10']['id']}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'lv000', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #                 ('live_room:' + str(roomNo), 'block_audience', {'targetUserId': test_parameter['track0012']['id'], 'reasonId': 8}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 9),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'track0011', 
        #             'event': 'audience_blocked', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': 'Violated the rules and was kicked out of the room'},
        #                 {'key': ['content', 'zh'], 'value': '違反規定，被踢出房間'},
        #                 {'key': ['content', 'ja'], 'value': 'ルールに違反し、部屋から追い出された'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['master10']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0011']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'audience_blocked_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '@{targetUser.name} 已被 @{fromUser.name}封鎖成功'},
        #                 {'key': ['content', 'zh'], 'value': '@{targetUser.name} 已被 @{fromUser.name}封鎖成功'},
        #                 {'key': ['content', 'ja'], 'value': '@{targetUser.name} 已被 @{fromUser.name}封鎖成功'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['master10']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['track0011']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'tracked_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['roomId'], 'value': roomNo},
        #                 {'key': ['content', 'en'], 'value': '@{fromUser.name} 追蹤了直播主！'},
        #                 {'key': ['content', 'zh'], 'value': '@{fromUser.name} 追蹤了直播主！'},
        #                 {'key': ['content', 'ja'], 'value': '@{fromUser.name} 追蹤了直播主！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'audience_banned_bcst', 
        #             'position': 1,
        #             'check': []
        #         },             
        #     ]
        # ),

        # ('送禮、熱度及marquee',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 15),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': '55f0ac47-9979-441f-8c49-23d5db7c2898', 'count': 40}, 1),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 3),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 0),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {}, 1),
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 1),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'count': 10}, 2),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 10),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 2),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
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
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'marquee', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 50 萬熱度，真是太厲害了！'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 3},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'marquee', 
        #             'position': 1,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0011']['nickname'] + ' 的 幸福燃點'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 2},

        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'marquee', 
        #             'position': 2,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 3},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'marquee', 
        #             'position': 3,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter['master10']['nickname'] + ' 收到 ' + test_parameter['track0012']['nickname'] + ' 的 對妳動心'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 1},

        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'room_in', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['room', 'liveRankingPoints'], 'value': test_parameter['master10']['dailyPoints'] + 550000},
        #                 {'key': ['room', 'totalGiftPoints'], 'value': 550000},
        #                 {'key': ['room', 'userGiftPoints'], 'value': 400000},

        #             ]
        #         },             
        #     ]

        # ),
        # ('送禮及marquee,暱稱有禁詞者不會顯示,但熱度會正常顯示',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 40),
        #                 ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0020', 'wait': 1, 'action': [
        #                 ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + str(roomNo), 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'count': 15}, 2),
        #                 ('live_room:' + str(roomNo), 'ping', {}, 5),
        #                 ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 2),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'gift_bcst', 
        #             'position': 0,
        #             'check': []
        #         },             
        #         {
        #             'index': 'track0020', 
        #             'event': 'gift', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 送了 {gift.count} 個 {gift.name} ({gift.points}) 給 {targetUser.name}'},
        #                 {'key': ['gift', 'id'], 'value': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53'},
        #                 {'key': ['gift', 'name', 'zh'], 'value': '對妳動心'},
        #                 {'key': ['gift', 'count'], 'value': 15},
        #                 {'key': ['gift', 'multiple'], 'value': False},
        #                 {'key': ['gift', 'points'], 'value': 225000},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'marquee', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'en'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'zh'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['content2', 'ja'], 'value': '恭喜' +  test_parameter['master10']['nickname'] +'今日已突破 20 萬熱度，真是太厲害了！'},
        #                 {'key': ['count'], 'value': 3},
        #                 {'key': ['level'], 'value': 3},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'marquee', 
        #             'position': 1,
        #             'check': []
        #         },             
        #     ]

        # ),

        ('用戶分享直播間訊息deep link #3668',
            [
                {'user': 'master10', 'wait': 0, 'action': [
                        ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
                        ('live_room:' + str(roomNo), 'close_room', {'roomId': roomNo}, 12),
                    ], 'sleep': 2
                },
                {'user': 'track0011', 'wait': 1, 'action': [
                        ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
                        ('live_room:' + str(roomNo), 'share', {}, 1),
                        ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 2),
                    ], 'sleep': 1
                },
                {'user': 'track0012', 'wait': 4, 'action': [
                        ('live_room:' + str(roomNo), 'phx_join', {'code': ''}, 0),
                        ('live_room:' + str(roomNo), 'share', {}, 3),
                        ('live_room:' + str(roomNo), 'share', {}, 3),
                        ('live_room:' + str(roomNo), 'phx_leave', {'code': ''}, 0),
                    ], 'sleep': 1
                },
            ],
            [
                {
                    'index': 'track0011', 
                    'event': 'shared_bcst', 
                    'position': 0,
                    'check': [
                        {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
                        {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
                        {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
                    ]
                },             
                {
                    'index': 'track0012', 
                    'event': 'shared_bcst', 
                    'position': 1,
                    'check': [
                        {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
                        {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
                        {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間，提升了直播間熱度！'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
                    ]
                },             
                {
                    'index': 'track0012', 
                    'event': 'shared_bcst', 
                    'position': 0,
                    'check': [
                        {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
                        {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
                        {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} 的直播間！'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter['master10']['id']},
                    ]
                },             
            ]

        ),

        # ('直播主timeout應主動將user請出直播間並關閉該房 #3669',
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
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

    ]   
    return testData