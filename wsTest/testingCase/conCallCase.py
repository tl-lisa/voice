from . import misc
from . import dbConnect
<<<<<<< HEAD
=======
from pprint import pprint
>>>>>>> 85ad4a3 (finish concall case)
import json

def clearDBInfo(dbAddress):
    sqlList = []
<<<<<<< HEAD
    for i in ['call_out', 'call_out_identity']:
        sqlList.append('TRUNCATE TABLE %s'%i)
=======
    for i in ['call_out_identity', 'call_out']:
        sqlList.append('delete from %s'%i)
        sqlList.append('alter table %s auto_increment = 1'%i)
>>>>>>> 85ad4a3 (finish concall case)
    dbConnect.dbSetting(dbAddress, sqlList)

def getRoomId(test_parameter, masterList):
    header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}
    for i in masterList:
        header['X-Auth-Token'] = test_parameter[i]['token']
        header['X-Auth-Nonce'] = test_parameter[i]['nonce']
        apiName = '/api/v2/liveMaster/zego/liveRoom'
        body = {
            "title" : test_parameter[i]['nickname'] + "開播囉",
            "description" : test_parameter[i]['nickname'] + "開播，歡迎入群",
            "events": [],
            "code": None
        }
        res = misc.apiFunction(test_parameter['prefix'], header, apiName, 'post', body)
        result = json.loads(res.text)
        test_parameter[i]['roomId'] = str(result['data']['roomId'])
<<<<<<< HEAD
=======
        pprint(test_parameter[i])
>>>>>>> 85ad4a3 (finish concall case)
    return 

def getTestData(test_parameter, masterList):
    misc.get_test_data('QA', test_parameter, 'master', 5, 10, 30, 2)  
    clearDBInfo(test_parameter['db'])
    getRoomId(test_parameter, masterList)
    testData = [
<<<<<<< HEAD
        ('受𨘋者正在接受別人的通話邀請中及60秒內無接聽', #4747
            [
                {'user': masterList[0], 'wait': 0, 'action': [
                        ('live_room:%s'% test_parameter[masterList[0]]['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'% test_parameter[masterList[0]]['roomId'], 'call_out', 
                          {'invitees': [test_parameter[masterList[1]]['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 0),
                        ('live_room:%s'% test_parameter[masterList[0]]['roomId'], 'ping', {}, 35),
                        ('live_room:%s'% test_parameter[masterList[0]]['roomId'], 'ping', {}, 35),
                        ('live_room:%s'% test_parameter[masterList[0]]['roomId'], 'close_room', {'roomId': int(test_parameter[masterList[0]]['roomId'])}, 0),
                    ], 'sleep': 2
                },
                {'user': masterList[1], 'wait': 0, 'action': [
                        ('live_room:%s'%test_parameter[masterList[1]]['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'%test_parameter[masterList[1]]['roomId'], 'close_room', {'roomId': int(test_parameter[masterList[1]]['roomId'])}, 10),
                    ], 'sleep': 2
                },
                {'user': masterList[2], 'wait': 3, 'action': [
                        ('live_room:%s'%test_parameter[masterList[2]]['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'%test_parameter[masterList[0]]['roomId'], 'call_out', 
                          {'invitees': [test_parameter[masterList[1]]['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 0),
                        ('live_room:%s'%test_parameter[masterList[2]]['roomId'], 'close_room', {'roomId': int(test_parameter[masterList[2]]['roomId'])}, 10),
=======
        # ('受𨘋者正在接受別人的通話邀請中或60秒內無接聽', #4746, 4747, 4748
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 3),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 30),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 30),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 5),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:' + test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master12', 'wait': 3, 'action': [
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 5),
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'close_room', {'roomId': int(test_parameter['master12']['roomId'])}, 10),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1}
        #             ]
        #         },             
        #         {
        #             'index': 'master12', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 2}
        #             ]
        #         },             

        #     ]
        # ),

        # ('受𨘋者正在通話中；已接通後status應該改為running', #4746, 4747, 4748
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 15, 'goalPointSetting': 10}, 3),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master12', 'wait': 3, 'action': [
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 3),
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'close_room', {'roomId': int(test_parameter['master12']['roomId'])}, 10),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master11', 
        #             'event': 'call_out_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'CREATED'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_pickup_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #             ]
        #         },             
        #         {
        #             'index': 'master12', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 2}
        #             ]
        #         },             
        #         {
        #             'index': 'master11', 
        #             'event': 'call_out_pickup_bcst', 
        #             'position': 0,
        #             'keyList': 
        #             [
        #                 'data', 'id', 'startTime', 'endTime', 'type', 'status', 'duration', 'goalPointSetting', 'title', 'subTitle', 
        #                 'inviter', 'id', 'nickname', 'roles', 'userLevel', 'levelId', 'levelNum', 'profilePicture', 'room', 'type', 
        #                 'id', 'stremId', 'points', 'invitees', 'id', 'nickname', 'roles', 'userLevel', 'levelId', 'levelNum', 'profilePicture', 
        #                 'room', 'type', 'id', 'stremId', 'points', 'endBy', 'sendTime'
        #             ]
        #         },

        #     ]
        # ),

        # ('邀請方放棄等待受𨘋方回應', #4752
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 15, 'goalPointSetting': 10}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_abort', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 20),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master11', 
        #             'event': 'call_out_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'CREATED'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #             ]
        #         },             
        #         {
        #             'index': 'master11', 
        #             'event': 'call_out_abort_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1},
        #                 {'key': ['userId'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             

        #     ]
        # ),

        # ('結束聯播（休閒型）', #4750
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 15, 'goalPointSetting': 10}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 7, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_leave', {}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 10, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 2),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_leave', {}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_hangup', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 20),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_done', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'DONE'},
        #                 {'key': ['data', 'title'], 'value': ''},
        #                 {'key': ['data', 'subTitle'], 'value': ''},
        #                 {'key': ['data', 'endBy'], 'value':  None},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'call_out_info', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'call_out_done', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'DONE'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'call_out_bcst', 
        #             'position': 0,
        #             'check': []
        #         },             
   
        #     ]
        # ),

        ('時間到系統自動判定輸鸁，之後再送禮也不會變更點數（挑戰型）', #4750
            [ 
                {'user': 'master10', 'wait': 0, 'action': [
                        ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
                          {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 5, 'goalPointSetting': 10}, 3),
                        ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
                    ], 'sleep': 2
                },
                {'user': 'track0011', 'wait': 7, 'action': [
                        ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_leave', {}, 20),
                    ], 'sleep': 2
                },
                {'user': 'track0012', 'wait': 10, 'action': [
                        ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'%test_parameter['master11']['roomId'], 'gift', {'targetUserId': test_parameter['master11']['id'],
                            'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
                        ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_leave', {}, 10),
                    ], 'sleep': 2
                },
                {'user': 'master11', 'wait': 0, 'action': [
                        ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': 1}, 5),
                        ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_dismiss', {'callOutId': 1}, 15),
                        ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 2),
>>>>>>> 85ad4a3 (finish concall case)
                    ], 'sleep': 2
                },
            ],
            [
                {
                    'index': 'master10', 
                    'event': 'call_out_done', 
                    'position': 0,
                    'check': 
                    [
                        {'key': ['data', 'type'], 'value': 'CHALLENGE'},
                        {'key': ['data', 'status'], 'value': 'DONE'},
                        {'key': ['data', 'title'], 'value': '挑戰結束'},
                        {'key': ['data', 'subTitle'], 'value': '居然是平局！'},
                        {'key': ['data', 'endBy'], 'value':  None},
                    ]
                },             
                {
                    'index': 'track0011', 
                    'event': 'call_out_info', 
                    'position': 0,
                    'check': 
                    [
                        {'key': ['data', 'type'], 'value': 'CHALLENGE'},
                        {'key': ['data', 'status'], 'value': 'RUNNING'},
                        {'key': ['data', 'duration'], 'value': 10},
                        {'key': ['data', 'goalPointSetting'], 'value': 10},
                        {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
                        {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
                        {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
                        {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
                    ]
                },             
                {
                    'index': 'track0011', 
                    'event': 'call_out_done', 
                    'position': 0,
                    'check': 
                    [
                        {'key': ['data', 'type'], 'value': 'CHALLENGE'},
                        {'key': ['data', 'status'], 'value': 'DONE'},
                        {'key': ['data', 'duration'], 'value': 10},
                        {'key': ['data', 'goalPointSetting'], 'value': 10},
                        {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
                        {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
                        {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
                        {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
                    ]
                },             
                {
                    'index': 'track0012', 
                    'event': 'call_out_bcst', 
                    'position': 0,
                    'check': []
                },             
   
            ]
        ),

        # ('送禮點數到系統自動判定輸鸁，之後再送禮也不會變更點數（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 15, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 7, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_leave', {}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 10, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'gift', {'targetUserId': test_parameter['master11']['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_leave', {}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_dismiss', {'callOutId': 1}, 15),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 2),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_done', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'DONE'},
        #                 {'key': ['data', 'title'], 'value': '挑戰結束'},
        #                 {'key': ['data', 'subTitle'], 'value': '恭喜 {{獲勝者 nickname}} 獲勝！'},
        #                 {'key': ['data', 'endBy'], 'value':  '{{獲勝者 uuid}}'},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_dismiss_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1},
        #                 {'key': ['userId'], 'value': test_parameter['master11']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'call_out_info', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 10},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'call_out_done', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'DONE'},
        #                 {'key': ['data', 'duration'], 'value': 10},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'call_out_bcst', 
        #             'position': 0,
        #             'check': []
        #         },             
   
        #     ]
        # ),

        # ('挑戰過程中有人先關播（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 25, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_dismiss', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 2),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_failed', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'FAILURE'},
        #                 {'key': ['data', 'title'], 'value': '挑戰中止'},
        #                 {'key': ['data', 'subTitle'], 'value': '%s 離開了'%test_parameter['master11']['nickname']},
        #                 {'key': ['data', 'endBy'], 'value': test_parameter['master11']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_dismiss_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1},
        #                 {'key': ['userId'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #     ]
        # ),
 
        # ('挑戰過程中有人先掛斷（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 25, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_dismiss', {'callOutId': 1}, 12),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_hangup', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 2),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_failed', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'FAILURE'},
        #                 {'key': ['data', 'title'], 'value': '挑戰中止'},
        #                 {'key': ['data', 'subTitle'], 'value': '%s 離開了'%test_parameter['master11']['nickname']},
        #                 {'key': ['data', 'endBy'], 'value': test_parameter['master11']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_dismiss_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1},
        #                 {'key': ['userId'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #     ]
        # ),

        # ('挑戰過程中有人先斷線未連回直播間（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 25, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 35),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 35),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_dismiss', {'callOutId': 1}, 20),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 1),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': 1}, 5),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_failed', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'FAILURE'},
        #                 {'key': ['data', 'title'], 'value': '挑戰中止'},
        #                 {'key': ['data', 'subTitle'], 'value': '%s 離開了'%test_parameter['master11']['nickname']},
        #                 {'key': ['data', 'endBy'], 'value': test_parameter['master11']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_dismiss_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1},
        #                 {'key': ['userId'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #     ]
        # ),
 
        # ('送出聯播𨘋請，受邀方手動拒絕', #pass
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 25, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_unavailable', {'callOutId': 1}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 10),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1},
        #             ]
        #         },             
        #     ]
        # ),

        # ('送出聯播𨘋請，但邀請方在受邀方的黑名單中', #pass
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 25, 'goalPointSetting': 1000}, 5),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'block_audience', {'targetUserId': test_parameter['master10']['id']}, 1),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 10),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'master11', 
        #             'event': 'call_out_bcst', 
        #             'position': 0,
        #             'check': []
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 1},
        #             ]
        #         },             
        #     ]
        # ),

    ]   

    return testData