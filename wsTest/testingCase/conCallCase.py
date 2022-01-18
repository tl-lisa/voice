from . import misc
from . import dbConnect
import json

def clearDBInfo(dbAddress):
    sqlList = []
    for i in ['call_out', 'call_out_identity']:
        sqlList.append('TRUNCATE TABLE %s'%i)
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
    return 

def getTestData(test_parameter, masterList):
    misc.get_test_data('QA', test_parameter, 'master', 5, 10, 30, 2)  
    clearDBInfo(test_parameter['db'])
    getRoomId(test_parameter, masterList)
    testData = [
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
                    ], 'sleep': 2
                },
            ],
            [
                {
                    'index': masterList[0], 
                    'event': 'call_out_unavailable_bcst', 
                    'position': 0,
                    'check': 
                    [
                        {'key': ['callOutId'], 'value': 1}
                    ]
                },             
                {
                    'index': masterList[2], 
                    'event': 'call_out_unavailable_bcst', 
                    'position': 0,
                    'check': 
                    [
                        {'key': ['callOutId'], 'value': 2}
                    ]
                },             

            ]
        ),

        # ('受𨘋者正在通話中', #4747
        #     [
        #         {'user': masterList[0], 'wait': 0, 'action': [
        #                 ('live_room:%d'% test_parameter[masterList[0]]['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%d'% test_parameter[masterList[0]]['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter[masterList[1]]['id']], 'type': 'CASUAL', 'duration': 15, 'goalPointSetting': 10}, 0),
        #                 ('live_room:%d'% test_parameter[masterList[0]]['roomId'], 'close_room', {'roomId': test_parameter[masterList[0]]['roomId']}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': masterList[1], 'wait': 0, 'action': [
        #                 ('live_room:' + test_parameter[masterList[1]]['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:' + test_parameter[masterList[1]]['roomId'], 'call_out_pickup', {'callOutId': 1}, 3),
        #                 ('live_room:' + test_parameter[masterList[1]]['roomId'], 'close_room', {'roomId': int(test_parameter[masterList[1]]['roomId'])}, 20),
        #             ], 'sleep': 2
        #         },
        #         {'user': masterList[2], 'wait': 3, 'action': [
        #                 ('live_room:' + test_parameter[masterList[2]]['roomId'], 'phx_join', {'code': ''}, 0),
        #                 ('live_room:%d'% test_parameter[masterList[0]]['roomId'], 'call_out', 
        #                   {'invitees': [test_parameter[masterList[1]]['id']], 'type': 'CASUAL', 'duration': 300, 'goalPointSetting': 10}, 0),
        #                 ('live_room:' + test_parameter[masterList[2]]['roomId'], 'close_room', {'roomId': int(test_parameter[masterList[2]]['roomId'])}, 10),
        #             ], 'sleep': 2
        #         },
        #     ],
        #     [
        #         {
        #             'index': masterList[1], 
        #             'event': 'call_out_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'CREATED'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  [test_parameter[masterList[0]]['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': [test_parameter[masterList[0]]['roomId']},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  [test_parameter[masterList[1]]['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': [test_parameter[masterList[1]]['roomId']},
        #             ]
        #         },             
        #         {
        #             'index': masterList[0], 
        #             'event': 'call_out_pickup_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['data', 'type'], 'value': 'CASUAL'},
        #                 {'key': ['data', 'status'], 'value': 'RUNNING'},
        #                 {'key': ['data', 'duration'], 'value': 15},
        #                 {'key': ['data', 'goalPointSetting'], 'value': 10},
        #                 {'key': ['data', 'inviter', 'id'], 'value':  [test_parameter[masterList[0]]['id']},
        #                 {'key': ['data', 'inviter', 'room', 'id'], 'value': [test_parameter[masterList[0]]['roomId']},
        #                 {'key': ['data', 'invitees', 'id'], 'value':  [test_parameter[masterList[1]]['id']},
        #                 {'key': ['data', 'invitees', 'room', 'id'], 'value': [test_parameter[masterList[1]]['roomId']},
        #             ]
        #         },             
        #         {
        #             'index': masterList[2], 
        #             'event': 'call_out_unavailable_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['callOutId'], 'value': 2}
        #             ]
        #         },             

        #     ]
        # ),

    ]   

    return testData