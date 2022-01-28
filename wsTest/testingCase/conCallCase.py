from . import misc
from . import dbConnect
import json

def getCalloutId(dbAddress): 
    sqlStr = 'select max(id) from call_out'
    dbResult = dbConnect.dbQuery(dbAddress, sqlStr)
    calloutId = dbResult[0][0] if dbResult[0][0] else 0
    print('callout id = %d'%calloutId)
    return calloutId

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
    return 

def getTestData(test_parameter, masterList):
    misc.get_test_data('QA', test_parameter, 'master', 5, 10, 30, 2)  
    calloutId = getCalloutId(test_parameter['db']) + 1
    getRoomId(test_parameter, masterList)
    testData = [
        ('受𨘋者正在接受別人的通話邀請中或60秒內無接聽', #4746, 4747, 4748
            [
                {'user': 'master10', 'wait': 0, 'action': [
                        ('live_room:%s'% test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'% test_parameter['master10']['roomId'], 'call_out', 
                          {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 3),
                        ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 30),
                        ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 30),
                        ('live_room:%s'% test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 5),
                    ], 'sleep': 2
                },
                {'user': 'master11', 'wait': 0, 'action': [
                        ('live_room:' + test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:' + test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 30),
                    ], 'sleep': 2
                },
                {'user': 'master12', 'wait': 3, 'action': [
                        ('live_room:%s'%test_parameter['master12']['roomId'], 'phx_join', {'code': ''}, 0),
                        ('live_room:%s'%test_parameter['master12']['roomId'], 'call_out', 
                          {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 5),
                        ('live_room:%s'%test_parameter['master12']['roomId'], 'close_room', {'roomId': int(test_parameter['master12']['roomId'])}, 10),
                    ], 'sleep': 2
                },
            ],
            [
                {
                    'index': 'master10', 
                    'event': 'call_out_unavailable_bcst', 
                    'position': 0,
                    'check': 
                    [
                        {'key': ['callOutId'], 'value': calloutId}
                    ]
                },             
                {
                    'index': 'master11', 
                    'event': 'call_out_bcst', 
                    'position': 1,
                    'check': []
                },             
                {
                    'index': 'master11', 
                    'event': 'call_out_bcst', 
                    'position': 0,
                    'check': [
                        {'key': ['data', 'type'], 'value': 'CASUAL'},
                        {'key': ['data', 'status'], 'value': 'CREATED'},
                        {'key': ['data', 'duration'], 'value': 300},
                        {'key': ['data', 'goalPointSetting'], 'value': 10},
                        {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
                        {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
                        {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
                        {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
                    ]
                },             
                {
                    'index': 'master12', 
                    'event': 'call_out_unavailable_bcst', 
                    'position': 0,
                    'check': 
                    [
                        {'key': ['callOutId'], 'value': calloutId + 1}
                    ]
                },             
            ]
        ),

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
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
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
        #         {
        #             'index': 'master12', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': calloutId + 1}
        #             ]
        #         },             

        #     ]
        # ),

        # ('受𨘋者已發起𨘋請給其他人；則不會再收到其他人的call_out_bcst', #4746, 4747, 4748
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
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master12', 'wait': 3, 'action': [
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master10']['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 1),
        #                 ('live_room:%s'%test_parameter['master12']['roomId'], 'close_room', {'roomId': int(test_parameter['master12']['roomId'])}, 10),
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
        #             'index': 'master12', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': calloutId + 1}
        #             ]
        #         },             

        #     ]
        # ),


        # ('邀請者取消，受𨘋者卻已接受聯播；則不會有pickup_bcst', #4746, 4747, 4748
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 15, 'goalPointSetting': 10}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_abort', {'callOutId': calloutId}, 5),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 5),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 9),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 5),
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
        #                 {'key': ['callOutId'], 'value': calloutId},
        #                 {'key': ['userId'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_pickup_bcst', 
        #             'position': 0,
        #             'check': []
        #         },             

        #     ]
        # ),

        # ('受𨘋者卻已接受聯播,邀請者後按下取消，abort應不會成功', #4746, 4747, 4748
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 15, 'goalPointSetting': 10}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_abort', {'callOutId': calloutId}, 2),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 5),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 4),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 5),
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
        #             'check': []
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

        #     ]
        # ),

        # ('邀請方等待受𨘋方回應，雙方各有用戶進房；之後受𨘋方拒絕', #4752
        #     [
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CASUAL', 'duration': 15, 'goalPointSetting': 10}, 2),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'ping', {}, 25),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 2),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 5, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_leave', {}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 5, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_leave', {}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_unavailable', {'callOutId': calloutId}, 15),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 5),
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
        #             'index': 'master10', 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': calloutId},
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
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_abort', {'callOutId': calloutId}, 5),
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
        #                 {'key': ['callOutId'], 'value': calloutId},
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
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_hangup', {'callOutId': calloutId}, 5),
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

        # ('時間到系統自動判定輸鸁，之後再送禮也不會變更點數（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 5, 'goalPointSetting': 10}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 7, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
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
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_dismiss', {'callOutId': calloutId}, 18),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 5),
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
        #                 {'key': ['data', 'subTitle'], 'value': '居然是平局！'},
        #                 {'key': ['data', 'endBy'], 'value':  ''},
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
        #                 {'key': ['data', 'duration'], 'value': 5},
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
        #                 {'key': ['data', 'duration'], 'value': 5},
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

        # ('送禮點數到系統自動判定輸鸁，之後再送禮也不會變更點數（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 10, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 7, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_leave', {}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 15, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'gift', {'targetUserId': test_parameter['master11']['id'],
        #                     'giftId': 'cf0fc6ba-9fae-4c6a-9f34-7a17207e3d60', 'count': 2}, 2),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_leave', {}, 2),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_dismiss', {'callOutId': calloutId}, 20),
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
        #                 {'key': ['data', 'invitees', 'points'], 'value': 0},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 300000},
        #                 {'key': ['data', 'subTitle'], 'value': '恭喜 %s 獲勝！'%test_parameter['master10']['nickname']},
        #                 {'key': ['data', 'endBy'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master11', 
        #             'event': 'call_out_done', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'DONE'},
        #                 {'key': ['data', 'title'], 'value': '挑戰結束'},
        #                 {'key': ['data', 'invitees', 'points'], 'value': 0},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 300000},
        #                 {'key': ['data', 'subTitle'], 'value': '恭喜 %s 獲勝！'%test_parameter['master10']['nickname']},
        #                 {'key': ['data', 'endBy'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_dismiss_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': calloutId},
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
        #                 {'key': ['data', 'endBy'], 'value': None},
        #                 {'key': ['data', 'title'], 'value': ''},
        #                 {'key': ['data', 'subTitle'], 'value': ''},
        #                 {'key': ['data', 'duration'], 'value': 10},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 1000},
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
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'endBy'], 'value': None},
        #                 {'key': ['data', 'title'], 'value': ''},
        #                 {'key': ['data', 'subTitle'], 'value': ''},
        #                 {'key': ['data', 'duration'], 'value': 10},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 1000},
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
        #                 {'key': ['data', 'goalPointSetting'], 'value': 1000},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #                 {'key': ['data', 'invitees', 'points'], 'value': 0},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 300000},
        #                 {'key': ['data', 'subTitle'], 'value': '恭喜 %s 獲勝！'%test_parameter['master10']['nickname']},
        #                 {'key': ['data', 'endBy'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'call_out_info_bcst', 
        #             'position': 0,
        #             'check': []
        #         },             
   
        #     ]
        # ),

        # ('時間到時自動以點數判斷輸贏，包括barrage也應計入，每次送禮皆應送出call_out_info（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 15, 'goalPointSetting': 50000}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_dismiss', {'callOutId': calloutId}, 25),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 5),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0011', 'wait': 7, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'count': 1}, 2), #point 15,000
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'gift', {'targetUserId': test_parameter['master10']['id'],
        #                     'giftId': 'dd14a8e4-e8f0-4e9f-8f6b-1aebe43ddf53', 'count': 2}, 3), #point 15,000
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'barrage', {'barrageId': 1, 'content': 'barrage也視同禮物🎁'}, 4), #point 119                       
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'barrage', {'barrageId': 2, 'content': 'barrage也視同禮物🎁'}, 8), #point 399                       
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_leave', {}, 2),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0012', 'wait': 7, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'gift', {'targetUserId': test_parameter['master11']['id'],
        #                     'giftId': '56067406-53c1-4d1f-8523-2eec0fcd8359', 'count': 1}, 3), #poirnt 30,000
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_leave', {}, 10),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_dismiss', {'callOutId': calloutId}, 20),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'close_room', {'roomId': int(test_parameter['master11']['roomId'])}, 5),
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
        #                 {'key': ['data', 'inviter', 'points'], 'value': 45119},
        #                 {'key': ['data', 'subTitle'], 'value': '恭喜 %s 獲勝！'%test_parameter['master10']['nickname']},
        #                 {'key': ['data', 'endBy'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_dismiss_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': calloutId},
        #                 {'key': ['userId'], 'value': test_parameter['master11']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'master10', 
        #             'event': 'call_out_dismiss_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': calloutId},
        #                 {'key': ['userId'], 'value': test_parameter['master10']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'call_out_info', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'endBy'], 'value': None},
        #                 {'key': ['data', 'subTitle'], 'value': ''},
        #                 {'key': ['data', 'title'], 'value': ''},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 50000},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 0},
        #                 {'key': ['data', 'invitees', 'points'], 'value': 0},

        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'call_out_info', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'endBy'], 'value': None},
        #                 {'key': ['data', 'subTitle'], 'value': ''},
        #                 {'key': ['data', 'title'], 'value': ''},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 50000},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 0},
        #                 {'key': ['data', 'invitees', 'points'], 'value': 0},

        #             ]
        #         },             
        #         {
        #             'index': 'track0011', 
        #             'event': 'call_out_info_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 50000},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 45119},
        #                 {'key': ['data', 'invitees', 'points'], 'value': 30000},

        #             ]
        #         },             
        #         {
        #             'index': 'track0012', 
        #             'event': 'call_out_info_bcst', 
        #             'position': 2,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CHALLENGE'},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 50000},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 15000},
        #                 {'key': ['data', 'invitees', 'points'], 'value': 30000},

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
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 50000},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  test_parameter['master10']['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': int(test_parameter['master10']['roomId'])},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  test_parameter['master11']['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': int(test_parameter['master11']['roomId'])},
        #                 {'key': ['data', 'inviter', 'points'], 'value': 45119},
        #                 {'key': ['data', 'invitees', 'points'], 'value': 30000},
        #             ]
        #         },                
        #     ]
        # ),

        # ('挑戰過程中有人先關播（挑戰型）', #4750
        #     [ 
        #         {'user': 'master10', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 25, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_dismiss', {'callOutId': calloutId}, 5),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
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
        #                 {'key': ['callOutId'], 'value': calloutId},
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
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_dismiss', {'callOutId': calloutId}, 12),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 30),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_hangup', {'callOutId': calloutId}, 5),
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
        #                 {'key': ['callOutId'], 'value': calloutId},
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
        #                   {'invitees': [test_parameter['master11']['id']], 'type': 'CHALLENGE', 'duration': 90, 'goalPointSetting': 1000}, 3),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 35),
        #                 ('live_room:%s'% test_parameter['master10']['roomId'], 'ping', {}, 35),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'call_out_dismiss', {'callOutId': calloutId}, 30),
        #                 ('live_room:%s'%test_parameter['master10']['roomId'], 'close_room', {'roomId': int(test_parameter['master10']['roomId'])}, 5),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'master11', 'wait': 0, 'action': [
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_pickup', {'callOutId': calloutId}, 5),
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
        #                 {'key': ['callOutId'], 'value': calloutId},
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
        #                 ('live_room:%s'%test_parameter['master11']['roomId'], 'call_out_unavailable', {'callOutId': calloutId}, 5),
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
        #                 {'key': ['callOutId'], 'value': calloutId},
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
        #                 {'key': ['callOutId'], 'value': calloutId},
        #             ]
        #         },             
        #     ]
        # ),

    ]   

    return testData