from . import misc
from pprint import pprint

def getTestData(test_parameter):
    misc.get_test_data('QA', test_parameter, 'private', 2, 1, 30, 2)      
    #check中的資料先以第一層為主，之後再看下層資料
    testData = [
        # ('僅房主與核准的用戶可以成功進入，在accept時session即應建立，若房主先離房則應close session及清redis', #4581
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 1),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 4),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 2),
        #                 ('private_vc_room:54', 'ping', {}, 10),
        #             ], 'sleep': 2
        #         },
        #     ], 
        #     [
        #         {
        #             'index': 'private001', 
        #             'event': 'private_vc_enter_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'roomId'], 'value': 54}, 
        #                 {'key': ['data', 'ownerUserId'], 'value': test_parameter['private001']['id']}, 
        #                 {'key': ['data', 'joinUserId'], 'value': test_parameter['track0001']['id']}, 
        #                 {'key': ['data', 'seatsMute'], 'value': []}, 
        #                 {'key': ['data', 'seats'], 'index':0, 'value':{'seat': 0, 'streamId': 'privateVc_54_69_b0659b54-09ce-4b03-aff5-56d2d92b584a', 'userId':test_parameter['private001']['id']}},
        #                 {'key': ['data', 'seats'], 'index':1, 'value':{'seat': 1, 'streamId': 'privateVc_54_69_e785b6f6-beb3-4ed7-bb75-672197e01746', 'userId':test_parameter['track0001']['id']}}
        #             ]
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'private_vc_enter_bcst', 
        #             'position': 0,
        #             'keyList': 
        #             [
        #                 'data','roomId', 'ownerUserId', 'joinUserId', 'seats', 'seat', 'userId', 'streamId', 'seatsMute',
        #                 'tracked', 'hot', 'title', 'description', 'userLevel', 'levelId', 'levelNum', 'userName', 'sendTime'
        #             ]
        #         },

        #     ]
        # ),

        # ('移除非私密聲聊房所需的event', #4598
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0002']['id'],"result": "refuse"}, 7),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 4),
        #                 ('private_vc_room:54', 'private_vc_goodbye', {"userId": test_parameter['track0001']['id']}, 4),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 8),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_abort', {}, 2),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 4),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 6),
        #                 ('private_vc_room:54', 'ping', {}, 6),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0002', 'wait': 5, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'ping', {}, 3),
        #             ], 'sleep': 2
        #         },
        #     ], 
        #     [
        #         {
        #             'index': 'private001', 
        #             'event': 'private_voiceroom_join', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'isAllowed'], 'value': False}, 
        #                 {'key': ['data', 'isOwner'], 'value': True}, 
        #             ]
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'voiceroom_in', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'voiceroom_in_bcst', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'take_seat', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'seat_taken', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'leave_seat', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'seat_left', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'book_seat', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'seat_booked', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'abort_seat', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'seat_aborted', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'seat_pickedup', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'pickup_seat', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'seat_kickedout', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'kickout_seat', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'track0002', 
        #             'event': 'seat_rejected', 
        #             'position': 0,
        #             'check': []
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'reject_seat', 
        #             'position': 0,
        #             'check': []
        #         },

        #     ]
        # ),


        # ('房主若修改了房間資訊，應在房內公告room_data_changed_bcst ', #4567
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 1),
        #                 ('api',{
        #                     'apiName': '/api/v2/app/privateVoiceChat/54',
        #                     'prefix': test_parameter['prefix'],
        #                     'header': {'Connection': 'Keep-alive', 'X-Auth-Token': test_parameter['private001']['token'], 'X-Auth-Nonce': test_parameter['private001']['nonce']},
        #                     'method': 'patch',
        #                     'body': {'title': '房內變更標題1', 'description': '房內變更說明1', 'ownerStatus': 'busy'}}, 5),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 4),
        #             ], 'sleep': 2
        #         },
        #         {'user': 'track0001', 'wait': 4, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 2),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 10),
        #             ], 'sleep': 2
        #         },
        #     ], 
        #     [
        #         {
        #             'index': 'private001', 
        #             'event': 'room_data_changed_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'roomId'], 'value': 54}, 
        #                 {'key': ['data', 'title'], 'value': '房內變更標題1'}, 
        #                 {'key': ['data', 'description'], 'value': '房內變更說明1'}, 
        #             ]
        #         },
        #     ]
        # ),

        # ('除房主外，在phx_join時應確認是否已綁定',  #4549
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 5),
        #                 ('private_vc_room:54', 'phx_leave', {}, 20),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'private002', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #             ], 'sleep': 4
        #         },
        #         {'user': 'lv000', 'wait': 2, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #             ], 'sleep': 4
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_abort', {}, 2),
        #             ], 'sleep': 4
        #         },
        #         {'user': 'track0002', 'wait': 2, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_abort', {}, 1),
        #             ], 'sleep': 4
        #         },
        #     ], 
        #     [
        #         {
        #             'index': 'lv000', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['response', 'err'], 'value': 'HAS_NOT_BOUND'}, 
        #             ]
        #         },
        #         {
        #             'index': 'private002', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['response', 'err'], 'value': 'HAS_NOT_BOUND'}, 
        #             ]
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'private_vc_apply_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['track0002']['id']}, 
        #                 {
        #                     'key': ['data', 'waitQueue'], 
        #                     'value': [
        #                         test_parameter['track0001']['id'],
        #                         test_parameter['track0002']['id'],
        #                     ]
        #                 }, 
        #             ]
        #         },

        #     ]
        # ),

        # ('房主進房、官方場控，私密主，一般使用者皆可申請及取消申請，且超過30秒會逾時，若房主同意A上麥，則B會收到拒絕的指令，一旦accept後，該房即應為busy的狀態且應建立session', 
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'ping', {}, 30),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 20),
        #                 ('private_vc_room:54', 'ping', {}, 30),
        #                 ('private_vc_room:54', 'phx_leave', {}, 30),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'private002', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_abort', {}, 5),
        #             ], 'sleep': 4
        #         },
        #         {'user': 'lv000', 'wait': 7, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'ping', {}, 30),
        #             ], 'sleep': 4
        #         },
        #         {'user': 'track0003', 'wait': 35, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 5),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 5),
        #             ], 'sleep': 4
        #         },
        #         {'user': 'track0001', 'wait': 35, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 7),
        #             ], 'sleep': 4
        #         },
        #         {'user': 'track0002', 'wait': 50, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 2),
        #             ], 'sleep': 4
        #         },
        #     ], 
        #     [
        #         {
        #             'index': 'private001', 
        #             'event': 'private_vc_apply_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['track0003']['id']}, 
        #                 {
        #                     'key': ['data', 'waitQueue'], 
        #                     'value': [
        #                         test_parameter['track0001']['id'],
        #                         test_parameter['track0003']['id'],
        #                     ]
        #                 }, 
        #             ]
        #         },
        #         {
        #             'index': 'track0002', 
        #             'event': 'phx_reply', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['response', 'err'], 'value': 'JOIN_ERROR'}, 
        #                 {'key': ['status'], 'value': 'error'}, 
        #             ]
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'private_vc_apply_bcst', 
        #             'position': 2,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['track0003']['id']}, 
        #                 {
        #                     'key': ['data', 'waitQueue'], 
        #                     'value': [
        #                         test_parameter['track0003']['id'],
        #                     ]
        #                 }, 
        #             ]
        #         },
        #         {
        #             'index': 'private001', 
        #             'event': 'private_vc_abort_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['private002']['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'private002', 
        #             'event': 'private_vc_abort_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['private002']['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'lv000', 
        #             'event': 'private_vc_apply_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['lv000']['id']}, 
        #                 {
        #                     'key': ['data', 'waitQueue'], 
        #                     'value': [
        #                         test_parameter['lv000']['id'],
        #                     ]
        #                 }, 
        #             ]
        #         },
        #         {
        #             'index': 'lv000', 
        #             'event': 'private_vc_review_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['lv000']['id']}, 
        #                 {'key': ['data', 'result'], 'value': 'timeout'}, 
        #             ]
        #         },
        #         {
        #             'index': 'track0003', 
        #             'event': 'private_vc_review_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['track0003']['id']}, 
        #                 {'key': ['data', 'result'], 'value': 'refuse'}, 
        #             ]
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'private_vc_review_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['track0001']['id']}, 
        #                 {'key': ['data', 'result'], 'value': 'accept'}, 
        #             ]
        #         },
        #     ]
        # ),

        # ('房主審核通過後用戶可立即上麥，用戶離開或被請出房後，即不可再上麥，需重新申請。', 
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['private002']['id'],"result": "accept"}, 2),
        #                 ('private_vc_room:54', 'private_vc_goodbye', {"userId": test_parameter['private002']['id']}, 4),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['lv000']['id'],"result": "accept"}, 3),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 9),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 7)
        #             ], 'sleep': 5
        #         },
        #         {'user': 'private002', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 2),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'lv000', 'wait': 7, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 5),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 2),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0001', 'wait': 15, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 4),
        #             ], 'sleep': 5
        #         },
        #     ], 
        #     [
        #         {
        #             'index': 'private001', 
        #             'event': 'private_vc_leave_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['lv000']['id']}, 
        #             ]
        #         },
        #         { 
        #             'index': 'private001', 
        #             'event': 'private_vc_goodbye_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['private002']['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'lv000', 
        #             'event': 'private_vc_leave_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['lv000']['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'private002', 
        #             'event': 'private_vc_goodbye_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['private002']['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'private_vc_leave_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['private001']['id']}, 
        #             ]
        #         },
        #     ]
        # ),

        # ('房主審核通過後用戶可立即上麥，用戶被請出房後， DB應結束該場session且記錄為goodbye。', 
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 2),
        #                 ('private_vc_room:54', 'private_vc_goodbye', {"userId": test_parameter['track0001']['id']}, 4),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 7)
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 2),
        #                 ('private_vc_room:54', 'ping', {}, 7),
        #             ], 'sleep': 5
        #         },
        #     ], 
        #     [
        #         { 
        #             'index': 'private001', 
        #             'event': 'private_vc_goodbye_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['track0001']['id']}, 
        #             ]
        #         },
        #         {
        #             'index': 'track0001', 
        #             'event': 'private_vc_goodbye_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': ['data', 'userId'], 'value': test_parameter['track0001']['id']}, 
        #             ]
        #         },
        #     ]
        # ),

        # ('房主及用戶在麥位，但房主發生上斷線，該房應轉成offline且結束該場session(disconnect)', # 4452
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 3),
        #             ], 'sleep': 0
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 5),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #             ], 'sleep': 5
        #         },
        #     ], 
        #     [
        #     ]
        # ),

        # ('房主及用戶在麥位，但用戶發生上斷線，該房應轉成online且結束該場session(disconnect)', # 4452
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 3),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 5),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 5),
        #             ], 'sleep': 1
        #         },
        #     ], 
        #     [
        #     ]
        # ),

        # ('房主已接受用戶上麥申請，但用戶發生上斷線未執行enter，該房應轉成online且結束該場session(disconnect)', # 4452
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 3),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'phx_leave', {}, 15),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #             ], 'sleep': 1
        #         },
        #     ], 
        #     [
        #     ]
        # ),

        # ('房主已接受用戶上麥申請，但用戶發生上斷線未執行enter，該房應轉成online且結束該場session(disconnect)', # 4452
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 3),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'ping', {}, 35),
        #                 ('private_vc_room:54', 'phx_leave', {}, 15),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0001', 'wait': 1, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 50),
        #             ], 'sleep': 1
        #         },
        #     ], 
        #     [
        #     ]
        # ),

        # ('房主及用戶在麥位，但房主發生斷線，70秒未連回，則應結束該session且房應轉成offline', # 4452
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #             ], 'sleep': 1
        #         },
        #     ], 
        #     [
        #     ]
        # ),

        # ('房主審核通過後用戶可立即上麥，用戶離開或被請出房後，即不可再上麥，需重新申請。', 
        #     [
        #         {'user': 'private001', 'wait': 0, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 0),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 4),
        #                 ('private_vc_room:54', 'private_vc_leave', {}, 20)
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0001', 'wait': 2, 'action': [
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 3),
        #                 ('private_vc_room:54', 'phx_leave', {}, 2)
        #                 ('private_vc_room:54', 'phx_join', {}, 1),
        #                 ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #             ], 'sleep': 5
        #         },
        #     ], 
        #     [
        #     ]
        # ),

        # ('用戶只要join後即可被ban或block，但在UI操作上需上麥後才能執行。請出房時需要記錄原因，且中斷錄影', #4492
        #     [
        #             {'user': 'private001', 'wait': 0, 'action': [
        #                     ('private_vc_room:54', 'phx_join', {}, 0),
        #                     ('private_vc_room:54', 'private_vc_enter', {}, 1),
        #                     ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 2),
        #                     ('private_vc_room:54', 'ban_audience', {"targetUserId": test_parameter['track0001']['id'], "reasonId": 8}, 5),
        #                     ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0002']['id'],"result": "accept"}, 3),
        #                     ('private_vc_room:54', 'block_audience', {"targetUserId": test_parameter['track0002']['id']}, 5),
        #                     ('private_vc_room:54', 'phx_leave', {}, 1),
        #                 ], 'sleep': 5
        #             },
        #             {'user': 'track0001', 'wait': 1, 'action': [
        #                     ('private_vc_room:54', 'phx_join', {}, 0),
        #                     ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                     ('private_vc_room:54', 'private_vc_enter', {}, 3),
        #                     ('private_vc_room:54', 'ping', {}, 10),
        #                 ], 'sleep': 4
        #             },
        #             {'user': 'track0002', 'wait': 8, 'action': [
        #                     ('private_vc_room:54', 'phx_join', {}, 1),
        #                     ('private_vc_room:54', 'private_vc_apply', {}, 1),
        #                     ('private_vc_room:54', 'private_vc_enter', {}, 3),
        #                     ('private_vc_room:54', 'ping', {}, 10),
        #                 ], 'sleep': 4
        #             },
        #     ],
        #     [
        #             {
        #                 'index': 'track0001', 
        #                 'event': 'audience_banned', 
        #                 'position': 0,
        #                 'check': 
        #                 [
        #                     {'key': ['data', 'roomId'], 'value': 54}, 
        #                     {'key': ['data', 'targetUserId'], 'value': test_parameter['track0001']['id']}, 
        #                     {'key': ['data', 'content'], 'value': '惡意謾罵，被踢出房間'}, 
        #                 ]
        #             },
        #             {
        #                 'index': 'private001', 
        #                 'event': 'audience_banned_bcst', 
        #                 'position': 0,
        #                 'check': 
        #                 [
        #                     {'key': ['data', 'roomId'], 'value': 54}, 
        #                     {'key': ['data', 'banAudiences'], 'value': [test_parameter['track0001']['id']]}, 
        #                     {'key': ['data', 'content'], 'value':  '%s 已被 %s 踢出成功'%(test_parameter['track0001']['nickname'], test_parameter['private001']['nickname'])}, 
        #                 ]
        #             },
        #             {
        #                 'index': 'track0002', 
        #                 'event': 'audience_blocked', 
        #                 'position': 0,
        #                 'check': 
        #                 [
        #                     {'key': ['data', 'roomId'], 'value': 54}, 
        #                     {'key': ['data', 'targetUserId'], 'value': test_parameter['track0002']['id']}, 
        #                     {'key': ['data', 'content'], 'value': '違反規定，被踢出房間'}, 
        #                 ]
        #             },
        #             {
        #                 'index': 'private001', 
        #                 'event': 'audience_blocked_bcst', 
        #                 'position': 0,
        #                 'check': 
        #                 [
        #                     {'key': ['data', 'roomId'], 'value': 54}, 
        #                     {'key': ['data', 'content'], 'value': '%s 已被 %s 封鎖成功'%(test_parameter['track0002']['nickname'], test_parameter['private001']['nickname'])}, 
        #                 ]
        #             },

        #     ]
        # )

        ('gift_bcst需加入gift_category type來判斷',   #4993
            [       
                {'user': 'private02', 'wait': 0, 'action': [
                        ('private_vc_room:54', 'phx_join', {}, 0),
                        ('private_vc_room:54', 'private_vc_enter', {}, 1),
                        ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0001']['id'],"result": "accept"}, 2),
                        ('private_vc_room:54', 'private_vc_review', {"userId": test_parameter['track0020']['id'],"result": "accept"}, 10),
                        ('private_vc_room:54', 'phx_leave', {}, 10),
                    ], 'sleep': 5
                },
                {'user': 'track0001', 'wait': 1, 'action': [
                        ('private_vc_room:54', 'phx_join', {}, 0),
                        ('private_vc_room:54', 'private_vc_apply', {}, 1),
                        ('private_vc_room:54', 'private_vc_enter', {}, 5),
                        ('private_vc_room:54', 'gift', {'giftId': 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8', 'targetUserId': test_parameter['private02']['id'], 'count': 1}, 1),
                        ('private_vc_room:54', 'phx_leave', {}, 1),
                    ], 'sleep': 1
                },
                {'user': 'track0020', 'wait': 10, 'action': [
                        ('private_vc_room:54', 'phx_join', {}, 1),
                        ('private_vc_room:54', 'private_vc_apply', {}, 1),
                        ('private_vc_room:54', 'private_vc_enter', {}, 5),
                        ('private_vc_room:54', 'gift', {'giftId': 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8', 'targetUserId': test_parameter['private02']['id'], 'count': 1}, 1),
                        ('private_vc_room:54', 'phx_leave', {}, 4),
                    ], 'sleep': 1
                },
            ],  
            [
                {'index': 'private02', 'event': 'gift_bcst', 'position': 0, 'check': [ 
                        {'key': ['data', 'fromUserId'], 'value': test_parameter['track0001']['id']}, 
                        {'key': ['data', 'targetUserId'], 'value': test_parameter['private02']['id']}, 
                        {'key': ['data', 'gift', 'url'], 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/50db4a76450e11eba49142010a8c008c.webp'},
                        {'key': ['data', 'gift', 'id'], 'value': 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8'}, 
                        {'key': ['data', 'gift', 'name', 'zh'], 'value': '心型圈'}, 
                        {'key': ['data', 'gift', 'multiple'], 'value': False},
                        {'key': ['data', 'gift', 'count'], 'value': 1}, 
                        {'key': ['data', 'gift', 'points'], 'value': 1700}, 
                        {'key': ['data', 'gift', 'duration'], 'value': 1},                         
                        {'key': ['data', 'content'], 
                            'value': '%s 送了 1 個 心型圈 (1,700) 給 %s'%(test_parameter['track0001']['nickname'], test_parameter['private02']['nickname'])},
                        {'key': ['data', 'gift', 'categoryId'], 'value': 5},
                    ]
                },
                {'index': 'private02', 'event': 'gift_bcst', 'position': 1, 'check': []},
                {'index': 'track0020', 'event': 'gift', 'position': 0, 'check': [ 
                        {'key': ['data', 'fromUserId'], 'value': test_parameter['track0020']['id']}, 
                        {'key': ['data', 'targetUserId'], 'value': test_parameter['private02']['id']}, 
                        {'key': ['data', 'gift', 'giftUrl'], 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/50db4a76450e11eba49142010a8c008c.webp'},
                        {'key': ['data', 'gift', 'id'], 'value': 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8'}, 
                        {'key': ['data', 'gift', 'name'], 'value': '心型圈'}, 
                        {'key': ['data', 'gift', 'multiple'], 'value': False},
                        {'key': ['data', 'gift', 'count'], 'value': 1}, 
                        {'key': ['data', 'gift', 'duration'], 'value': 1},                         
                        {'key': ['data', 'gift', 'point'], 'value': 1700}, 
                        {'key': ['data', 'content'], 
                            'value': '%s 送了 1 個 心型圈 (1,700) 給 %s'%(test_parameter['track0020']['nickname'], test_parameter['private02']['nickname'])},
                        {'key': ['data', 'gift', 'categoryId'], 'value': 5},
                    ]
                },
            ]
        ),

    ]   
    return testData