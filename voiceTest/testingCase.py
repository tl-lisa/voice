def getTestData(test_parameter):
    #check中的資料先以第一層為主，之後再看下層資料
    testData = [
        # ('2位玩家先後進出聲聊房，在房中的人會收到系統廣播，而進房的人會收到管理者清單', 
        #     [
        #         {'user': 'track0011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 4},
        #         {'user': 'track0012', 'wait': 1, 'action': [('vc_room:1', 'phx_join', {}, 0), ('vc_room:1', 'phx_leave', {}, 1)], 'sleep': 0}
        #     ], 
        #     [
        #         {
        #             'index': 'track0011', 
        #             'event': 'voiceroom_in_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'totalCount', 'value': 2}, 
        #                 {'key': 'hot', 'value': 3*1331}, 
        #                 {'key': 'joinUserId', 'value':test_parameter['track0012']['id']}
        #             ]
        #         },
        #         {
        #             'index': 'track0011', 
        #             'event': 'voiceroom_left_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'userId', 'value': test_parameter['track0012']['id']},
        #             ]
        #         },
        #         {
        #             'index': 'track0012', 
        #             'event': 'voiceroom_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'admins', 'value': [
        #                     test_parameter['broadcaster011']['id'],
        #                     test_parameter['broadcaster012']['id'],
        #                     test_parameter['broadcaster013']['id'],
        #                     test_parameter['broadcaster014']['id']
        #                 ]}
        #             ]
        #         }
        #     ]
        # ),

        # ('直播主上下麥，已在房中的人及後來進房的人會收到系統廣播及相關訊息', 
        #     [
        #         {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 3},
        #         {'user': 'broadcaster011', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:1', 'leave_seat', {}, 5),  
        #             ], 'sleep': 1},
        #         {'user': 'broadcaster012', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 2 }, 2),
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}, 1),
        #                 ('vc_room:1', 'phx_leave', {}, 1),  
        #             ], 'sleep': 1},
        #         {'user': 'track0013', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 3},
        #         {'user': 'track0014', 'wait': 7, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 0}
        #     ], 
        #     [
        #         {'index': 'track0012', 'event': 'seat_taken', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': test_parameter['broadcaster011']['id']}, 
        #                         {'seat': 2, 'userId': test_parameter['broadcaster012']['id']},
        #                         {'seat': 3, 'userId': None},
        #                         {'seat': 4, 'userId': None},
        #                         {'seat': 5, 'userId': None},
        #                         {'seat': 6, 'userId': None},
        #                         {'seat': 7, 'userId': None},
        #                         {'seat': 8, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'seat_left', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': None}, 
        #                         {'seat': 2, 'userId': test_parameter['broadcaster012']['id']},
        #                         {'seat': 3, 'userId': None},
        #                         {'seat': 4, 'userId': None},
        #                         {'seat': 5, 'userId': None},
        #                         {'seat': 6, 'userId': None},
        #                         {'seat': 7, 'userId': None},
        #                         {'seat': 8, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'voiceroom_in', 'position': 0, 'check':[
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': test_parameter['broadcaster011']['id']}, 
        #                         {'seat': 2, 'userId': test_parameter['broadcaster012']['id']},
        #                         {'seat': 3, 'userId': None},
        #                         {'seat': 4, 'userId': None},
        #                         {'seat': 5, 'userId': None},
        #                         {'seat': 6, 'userId': None},
        #                         {'seat': 7, 'userId': None},
        #                         {'seat': 8, 'userId': None}
        #                     ]
        #                 },
        #                 {'key': 'seatsMute', 'value': [test_parameter['broadcaster012']['id']]
        #                 },
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'voiceroom_left_bcst', 'position': 0, 'check':[
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': test_parameter['broadcaster011']['id']}, 
        #                         {'seat': 2, 'userId': None},
        #                         {'seat': 3, 'userId': None},
        #                         {'seat': 4, 'userId': None},
        #                         {'seat': 5, 'userId': None},
        #                         {'seat': 6, 'userId': None},
        #                         {'seat': 7, 'userId': None},
        #                         {'seat': 8, 'userId': None}
        #                     ]
        #                 },
        #                 {'key': 'seatsMute', 'value': []},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'voiceroom_in', 'position': 0, 'check':[
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': None},  
        #                         {'seat': 2, 'userId': None},
        #                         {'seat': 3, 'userId': None},
        #                         {'seat': 4, 'userId': None},
        #                         {'seat': 5, 'userId': None},
        #                         {'seat': 6, 'userId': None},
        #                         {'seat': 7, 'userId': None},
        #                         {'seat': 8, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         }
        #     ]
        # ), 

        # ('有人申請上麥，在房中及後進房的人會收到相關資訊, 且離房後會清除上麥申請',  
        #     [ 
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1)
        #             ], 
        #             'sleep': 6
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1),
        #             ], 
        #             'sleep': 2
        #         },
        #         {'user': 'broadcaster012', 'wait': 3, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0)
        #             ], 
        #             'sleep': 1
        #         },
        #         {'user': 'broadcaster013', 'wait': 5, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0)
        #             ], 
        #             'sleep': 1
        #         }
        #     ], 
        #     [
        #         {'index': 'broadcaster011', 'event': 'seat_booked', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': [test_parameter['track0012']['id']]}
        #             ]
        #         },
        #         {'index': 'broadcaster012', 'event': 'seat_booked', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': [test_parameter['track0012']['id']]}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'seat_booked', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': [test_parameter['track0012']['id']]}
        #             ]
        #         }
        #     ]
        # ),

        # ('有人申請上麥，房主及管理員可以拒絕申請，而觀眾自己可以取消申請',  
        #     [ 
        #         {'user': 'broadcaster010', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'reject_seat', {'targetUserId': test_parameter['track0011']['id']}, 3)
        #             ], 
        #             'sleep': 2
        #         },
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:1', 'reject_seat', {'targetUserId': test_parameter['track0012']['id']}, 5)
        #             ], 
        #             'sleep': 8
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1)
        #             ], 
        #             'sleep': 4
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1)
        #             ], 
        #             'sleep': 4
        #         },
        #         {'user': 'track0013', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1),
        #                 ('vc_room:1', 'abort_seat', {}, 6)
        #             ], 
        #             'sleep': 4
        #         },
        #     ], 
        #     [
        #         {'index': 'broadcaster010', 'event': 'seat_rejected', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': [
        #                         test_parameter['track0013']['id']
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'seat_rejected', 'position': 1, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': [
        #                         test_parameter['track0013']['id'],
        #                         test_parameter['track0012']['id']
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'seat_aborted', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': []}
        #             ]
        #         }
        #     ]
        # ),

        # ('僅房主及管理員可以查詢目前上麥及排麥名單',  
        #     [ 
        #         {'user': 'broadcaster010', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'get_mics_mgm', {}, 1)
        #             ], 
        #             'sleep': 4
        #         },
        #         {'user': 'track0011', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1),
        #                 ('vc_room:1', 'get_mics_mgm', {}, 2)
        #             ], 
        #             'sleep': 4
        #         },
        #         {'user': 'broadcaster011', 'wait': 2, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:1', 'get_mics_mgm', {}, 2)
        #             ], 
        #             'sleep': 4
        #         }
        #     ], 
        #     [
        #         {'index': 'broadcaster010', 'event': 'mics_mgm_got', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': []},
        #                 {
        #                     'key': 'seats',
        #                     'value': [
        #                         {'seat': 0, 'userId': test_parameter['broadcaster010']['id']},
        #                         {'seat': 1, 'userId': None},
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'mics_mgm_got', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seatQueue', 'value': [test_parameter['track0011']['id']]},
        #                 {
        #                     'key': 'seats',
        #                     'value': [
        #                         {'seat': 0, 'userId': test_parameter['broadcaster010']['id']},
        #                         {'seat': 1, 'userId': test_parameter['broadcaster011']['id']},
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'phx_reply', 'position': 0, 'check': 
        #             [
        #                 {'key': 'err', 'value': 'permission_deny'}
        #             ]
        #         }
        #     ]
        # ),

        # ('目前房主可將管理者及一般觀眾踢下麥，而管理者可對管理者及一般觀眾進行踢下麥的動作，而一般觀眾則無此權限',
        #     [
        #         {'user': 'track0011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1)
        #             ], 'sleep': 8
        #         },
        #         {'user': 'track0012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1)
        #             ], 'sleep': 8
        #         },
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:1', 'pickup_seat', {
        #                         'targetUserId': test_parameter['track0011']['id'],
        #                         'seatType': 'vip',
        #                         'seatIndex':0
        #                     }, 1
        #                 )
        #             ], 'sleep': 8
        #         },
        #         {'user': 'broadcaster012', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['broadcaster011']['id'] }, 1),
        #                 ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['track0011']['id'] }, 1),
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 2),
        #                 ('vc_room:1', 'get_mics_mgm', {}, 1),
        #                 ('vc_room:1', 'pickup_seat', {
        #                         'targetUserId': test_parameter['track0012']['id'],
        #                         'seatType': 'host',
        #                         'seatIndex':2
        #                     }, 1
        #                 )
        #             ], 'sleep': 8
        #         },
        #         {'user': 'broadcaster010', 'wait': 5, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['broadcaster012']['id'] }, 1),
        #                 ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['track0012']['id'] }, 1),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'broadcaster013', 'wait': 6, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['broadcaster010']['id'] }, 1)
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'broadcaster012', 
        #             'event': 'mics_mgm_got', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'seatQueue', 
        #                     'value': [
        #                         test_parameter['track0012']['id']
        #                     ]
        #                 }
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster012', 
        #             'event': 'seat_kickedout', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'seats', 
        #                     'value': [
        #                         {'seat': 0, 'userId': None},
        #                         {'seat': 1, 'userId': None},
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 },
        #                 {'key': 'vips', 
        #                     'value': [
        #                         {'seat': 0, 'userId': None}
        #                     ]
        #                 },
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster012', 
        #             'event': 'seat_pickedup', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'seats', 
        #                     'value': [
        #                         {'seat': 0, 'userId': None},
        #                         {'seat': 1, 'userId': test_parameter['broadcaster012']['id']},
        #                         {'seat': 2, 'userId': test_parameter['track0012']['id']}
        #                     ]
        #                 },
        #                 {'key': 'vips', 
        #                     'value': [
        #                         {'seat': 0, 'userId': None}
        #                     ]
        #                 },
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'seat_kickedout', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'seats', 
        #                     'value': [
        #                         {'seat': 0, 'userId': test_parameter['broadcaster010']['id']},
        #                         {'seat': 1, 'userId': None},
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 },
        #                 {'key': 'vips', 
        #                     'value': [
        #                         {'seat': 0, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster013', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': [{'key': 'err', 'value': 'permission_deny'}]
        #         },
        #     ]
        # ),

        # ('房主一進房即自動上麥，且可以拉任何角色上麥，只是觀眾要先排麥才能上麥。 管理員可以拉管理員及一般觀眾上麥，除房主外其餘人皆可自動下麥, 且離開房間會自動下麥，且除房主位外，所有位置皆可任意坐', 
        #     [
        #         {
        #             'user': 'track0011', 'wait': 0, 
        #             'action': 
        #                 [
        #                     ('vc_room:1', 'phx_join', {}, 0), 
        #                     ('vc_room:1', 'book_seat', {}, 0),
        #                     ('vc_room:1', 'leave_seat', {},5)
        #                 ], 'sleep': 5
        #         },
        #         {
        #             'user': 'track0012', 'wait': 1, 
        #             'action': 
        #                 [
        #                     ('vc_room:1', 'phx_join', {}, 0), 
        #                     ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'vips', 'seatIndex': 0}, 1),
        #                     ('vc_room:1', 'book_seat', {}, 6)
        #                 ], 'sleep': 2
        #         },
        #         {
        #             'user': 'broadcaster011', 'wait': 2, 
        #             'action': 
        #                 [
        #                     ('vc_room:1', 'phx_join', {}, 0), 
        #                     ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 0),
        #                     ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'host', 'seatIndex': 0}, 1),
        #                     ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'host', 'seatIndex': 2}, 1),
        #                     ('vc_room:1', 'leave_seat', {}, 0)
        #                 ], 'sleep': 2
        #         },
        #         {
        #             'user': 'broadcaster012', 'wait': 5, 
        #             'action': 
        #                 [
        #                     ('vc_room:1', 'phx_join', {}, 0)
        #                 ], 'sleep': 2
        #         },
        #         {
        #             'user': 'broadcaster010', 'wait': 6, 
        #             'action': 
        #                 [
        #                     ('vc_room:1', 'phx_join', {}, 0), 
        #                     ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['broadcaster012']['id'], 'seatType': 'host', 'seatIndex': 1}, 1),
        #                     ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}, 1),
        #                     ('vc_room:1', 'leave_seat', {}, 1)
        #                 ], 'sleep': 2
        #         }
        #     ],
        #     [
        #         {
        #             'index': 'track0012', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': [{'key': 'err', 'value': 'PERMISSION_DENY'}]
        #         },
        #         {
        #             'index': 'broadcaster011', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': [{'key': 'err', 'value': 'ONLY_OWNER_CAN_CHANGE_SEAT_ZERO'}]
        #         },
        #         {
        #             'index': 'broadcaster011', 
        #             'event': 'seat_taken', 
        #             'position': 1,
        #             'check': [
        #                 {'key': 'seats', 'value': [
        #                     {'seat': 0, 'userId': None},
        #                     {'seat': 1, 'userId': test_parameter['broadcaster011']['id']},
        #                     {'seat': 2, 'userId': None}]
        #                 }
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster011', 
        #             'event': 'seat_pickedup', 
        #             'position': 1,
        #             'check': [
        #                 {'key': 'seats', 
        #                     'value': [
        #                         {'seat': 0, 'userId': None},
        #                         {'seat': 1, 'userId': test_parameter['broadcaster011']['id']},
        #                         {'seat': 2, 'userId': test_parameter['track0011']['id']}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'voiceroom_left_bcst', 
        #             'position': 0,
        #             'check': [
        #                 {'key': 'seats', 
        #                     'value': [
        #                         {'seat': 0, 'userId': test_parameter['broadcaster010']['id']},
        #                         {'seat': 1, 'userId': None},
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 },
        #                 {'key': 'vips', 
        #                     'value': [
        #                         {'seat': 0, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'seat_pickedup', 
        #             'position': 0,
        #             'check': [
        #                 {'key': 'seats', 
        #                     'value': [
        #                         {'seat': 0, 'userId': test_parameter['broadcaster010']['id']},
        #                         {'seat': 1, 'userId': test_parameter['broadcaster012']['id']},
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 },
        #                 {'key': 'vips', 
        #                     'value': [
        #                         {'seat': 0, 'userId': test_parameter['track0012']['id']}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'seat_booked', 
        #             'position': 0,
        #             'check': [{'key': 'seatQueue', 'value': [test_parameter['track0012']['id']]}]
        #         },
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #         'check': [{'key': 'err', 'value': 'OWNER_CAN_NOT_LEAVE_SEAT'}]
        #         }
        #     ]
        # ),

        # ('房主可對管理員及Vip位做禁音及解除禁音；管理員可對管理員(包括自己)及觀眾做禁音及解除禁音；而觀眾可以解除自己的禁音',
        #     [
        #         {'user': 'broadcaster012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1}, 0),
        #                 ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}, 4)
        #             ], 'sleep': 8
        #         }, 
        #         {'user': 'track0012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),  
        #                 ('vc_room:1', 'book_seat', {}, 0),
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}, 2),
        #                 ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['track0012']['id']}, 3)
        #             ], 'sleep': 8
        #         }, 
        #         {'user': 'broadcaster011', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 2}, 0),
        #                 ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}, 1),
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}, 1),
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['track0012']['id']}, 1),
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['track0012']['id']}, 4),
        #                 ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['track0012']['id']}, 1)
        #             ], 'sleep': 12
        #         }, 
        #         {'user': 'track0011', 'wait': 7, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),  
        #                 ('vc_room:1', 'book_seat', {}, 0)
        #             ], 'sleep': 4
        #         }, 
        #         {'user': 'broadcaster010', 'wait': 8, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['track0012']['id']}, 1),
        #                 ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'vips', 'seatIndex': 0}, 1),
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster011']['id']}, 1),
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['track0011']['id']}, 1),
        #                 ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster011']['id']}, 1),
        #                 ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['track0011']['id']}, 1)
        #             ], 'sleep': 1
        #         }
        #     ],
        #     [
        #         {
        #             'index': 'broadcaster010', 'event': 'seat_muted_bcst', 'position': 0, 'check': [
        #                 {'key': 'seatsMute', 'value': [test_parameter['track0011']['id'], test_parameter['broadcaster011']['id']]}
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster010', 'event': 'seat_unmuted_bcst', 'position': 0, 'check': []
        #         },
        #         {
        #             'index': 'broadcaster011', 'event': 'seat_muted_bcst', 'position': 3, 'check': [
        #                 {'key': 'seatsMute', 'value': [test_parameter['track0012']['id'], test_parameter['broadcaster012']['id']]}
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster011', 'event': 'seat_unmuted_bcst', 'position': 2, 'check': [
        #                 {'key': 'seatsMute', 'value': []}
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster012', 'event': 'seat_unmuted_bcst', 'position': 4, 'check': [
        #                 {'key': 'seatsMute', 'value': [test_parameter['track0012']['id']]}
        #             ]
        #         },
        #         {
        #             'index': 'track0012', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': 'err', 'value': 'permission_deny'}
        #             ]
        #         },
        #         {
        #             'index': 'track0011', 'event': 'voiceroom_in', 'position': 0, 'check': [
        #                 {'key': 'seatsMute', 'value': []}
        #             ]
        #         }
        #     ]
        # ),

        # ('訊息或暱稱包括禁詞除自己外，其他人不會收到訊息',
        #     [
        #         {'user': 'broadcaster012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {},0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1}, 1)
        #             ], 
        #             'sleep': 7
        #         }, 
        #         {'user': 'broadcaster011', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}, 1)
        #             ], 
        #             'sleep': 6
        #         },
        #         {'user': 'broadcaster013', 'wait': 2, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'message', {'content': 'broadcaster13 發送訊息'}, 1)
        #             ], 
        #             'sleep': 5
        #         },
        #         {'user': 'track0020', 'wait': 2, 'action': [
        #                     ('vc_room:1', 'phx_join', {}, 0), 
        #                     ('vc_room:1', 'message', {'content': '我的nickname有禁詞'}, 1)
        #                 ], 
        #                 'sleep': 3
        #         },
        #         {'user': 'track0011', 'wait': 2, 'action': [
        #                     ('vc_room:1', 'phx_join', {}, 0), 
        #                     ('vc_room:1', 'message', {'content': '我發的訊息有代儲值'},1)
        #                 ], 
        #                 'sleep': 1
        #         }
        #     ],
        #     [
        #         {'index': 'broadcaster012', 'event': 'message_bcst',  'position': 0, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['broadcaster013']['id']}, 
        #                 {'key': 'content', 'value': '@直播主13 broadcaster13 發送訊息'}
        #             ]
        #         },
        #         {'index': 'broadcaster012', 'event': 'message_bcst', 'position': 1, 'check': []},
        #         {'index': 'track0020', 'event': 'message',  'position': 0, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['track0020']['id']}, 
        #                 {'key': 'content', 'value': '@快樂代儲你我他 我的nickname有禁詞'}
        #             ]
        #         },
        #         {'index': 'track0020', 'event': 'message_bcst', 'position': 0, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['broadcaster013']['id']}, 
        #                 {'key': 'content', 'value': '@直播主13 broadcaster13 發送訊息'}
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'message_bcst', 'position': 0, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['broadcaster013']['id']}, 
        #                 {'key': 'content', 'value': '@直播主13 broadcaster13 發送訊息'}
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'message', 'position': 0, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['track0011']['id']}, 
        #                 {'key': 'content', 'value': '@我是小QA的迷妹 我發的訊息有代儲值'}
        #             ]
        #         }
        #     ]
        # ), 

        # ('送禮訊息在聲聊房中皆會收到,且超過10萬點的禮物會有跑馬燈, 若是暱稱含禁詞，則送禮訊息不會廣播, 若點數不足會回錯誤',  
        #     [       
        #         {'user': 'broadcaster010', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'ping', {}, 5),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'broadcaster013', 'wait': 2, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:1', 'ping', {}, 5),
        #             ], 'sleep': 3
        #         }, 
        #         {'user': 'track0019', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster010']['id'], 'count': 1}, 1),
        #                 ('vc_room:1', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster010']['id'], 'count': 1}, 1)
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0020', 'wait': 2, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'gift', {'giftId': 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 3}, 1)
        #             ], 'sleep': 2
        #         }
        #     ],  
        #     [
        #         {'index': 'track0019', 'event': 'gift_bcst', 'position': 2, 'check': []},              
        #         {'index': 'track0019', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': ['err'], 'value': 'you_have_no_more_points'}
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'marquee', 'position': 0, 'check': [
        #                 {'key': ['content'], 'value': '恭喜無與倫比的美麗,獲得舞弊事件大家都不能接受送的烤雞全餐 ~太帥了!就是狂!'},
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'gift_bcst', 'position': 0, 'check': [
        #                 {'key': ['fromUserId'], 'value': test_parameter['track0019']['id']}, 
        #                 {'key': ['targetUserId'], 'value': test_parameter['broadcaster010']['id']}, 
        #                 {'key': ['giftUrl'], 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/e84bd3921b4411eb917342010a8c0050.webp'},
        #                 {'key': ['giftId'], 'value': '9e63bbf0-3e86-4019-b3fc-e955c175569b'}, 
        #                 {'key': ['giftName'], 'value': '烤雞全餐'}, 
        #                 {'key': ['multiple'], 'value': False},
        #                 {'key': ['count'], 'value': 1}, 
        #                 {'key': ['point'], 'value': 100000}, 
        #                 {'key': ['content'], 'value': '舞弊事件大家都不能接受 送了 1 個 烤雞全餐 (100,000) 給 無與倫比的美麗'}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'gift_bcst', 'position': 0, 'check': [ #這個case有問題⋯⋯需再驗一次
        #                 {'key': ['fromUserId'], 'value': test_parameter['track0020']['id']}, 
        #                 {'key': ['targetUserId'], 'value': test_parameter['broadcaster013']['id']}, 
        #                 {'key': ['giftUrl'], 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/86a291301b4411eb917342010a8c0050.webp'},
        #                 {'key': ['giftId'], 'value': 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8'}, 
        #                 {'key': ['giftName'], 'value': '南瓜派'}, 
        #                 {'key': ['multiple'], 'value': False},
        #                 {'key': ['count'], 'value': 3}, 
        #                 {'key': ['point'], 'value': 1000}, 
        #                 {'key': ['content'], 'value': '快樂代儲你我他 送了 鬼怪(1000) x 3 禮物給 直播主13'}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'gift_bcst', 'position': 1, 'check': [
        #                 {'key': ['fromUserId'], 'value': test_parameter['track0019']['id']}, 
        #                 {'key': ['targetUserId'], 'value': test_parameter['broadcaster010']['id']}, 
        #                 {'key': ['giftUrl'], 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/e84bd3921b4411eb917342010a8c0050.webp'},
        #                 {'key': ['giftId'], 'value': '9e63bbf0-3e86-4019-b3fc-e955c175569b'}, 
        #                 {'key': ['giftName'], 'value': '烤雞全餐'}, 
        #                 {'key': ['multiple'], 'value': False},
        #                 {'key': ['count'], 'value': 1}, 
        #                 {'key': ['point'], 'value': 100000}, 
        #                 {'key': ['content'], 'value': '舞弊事件大家都不能接受 送了 1 個 烤雞全餐(100,000) 給 無與倫比的美麗'}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'marquee', 'position': 0, 'check': [
        #                 {'key': ['content'], 'value': '恭喜無與倫比的美麗,獲得舞弊事件大家都不能接受送的幸福燃點 ~太帥了!就是狂!'}
        #             ]
        #         }
        #     ]
        # ),

        # ('觀眾若被禁言，在發送訊息時不會廣播給聲聊廳的人；觀眾被禁言時房主及管理員會收到通知，解除禁言時也不會發通知；相關行為會同時更新禁言清單（註：禁言一定時間後系統會自動解除）', #QA環境怪怪的，但testing OK
        #     [
        #         {'user': 'track0011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'message', {'content': 'track0011被禁言第一次發送訊息'}, 4),
        #                 ('vc_room:1', 'message', {'content': 'track0011系統解除禁言後發送訊息'}, 35)
        #             ], 'sleep': 0
        #         },
        #         {'user': 'track0012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'message', {'content': 'track0012被禁言第一次發送訊息'}, 4),
        #                 ('vc_room:1', 'message', {'content': 'track0012管理員解除禁言後發送訊息'}, 9)
        #             ], 'sleep': 5
        #         },
        #         {'user': 'track0013', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0)
        #             ], 'sleep': 7
        #         },
        #         {'user': 'broadcaster010', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'mute_audience', {'targetUserId': test_parameter['track0011']['id']}, 1),
        #                 ('vc_room:1', 'mute_audience', {'targetUserId': test_parameter['track0013']['id']}, 3),
        #                 ('vc_room:1', 'unmute_audience', {'targetUserId': test_parameter['track0012']['id']}, 7),
        #                 ('vc_room:1', 'get_violation', {}, 25),
        #                 ('vc_room:1', 'get_violation', {}, 13),
        #             ], 'sleep': 5
        #         },
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'mute_audience', {'targetUserId': test_parameter['track0012']['id']}, 2),
        #                 ('vc_room:1', 'unmute_audience', {'targetUserId': test_parameter['track0013']['id']}, 3),
        #                 ('vc_room:1', 'get_violation', {}, 1),
        #                 ('vc_room:1', 'ping', {}, 10),
        #                 ('vc_room:1', 'ping', {}, 10),
        #                 ('vc_room:1', 'ping', {}, 10),
        #                 ('vc_room:1', 'ping', {}, 10),
        #             ], 'sleep': 3
        #         }
        #     ],
        #     [
        #         {'index': 'broadcaster011', 'event': 'audience_muted_bcst', 'position': 0, 'check': [
        #                 {'key': 'content', 'value': 'track0013 已被 無與倫比的美麗 禁言成功'}, 
        #                 {'key': 'muteAudiences', 'value': [test_parameter['track0011']['id'], test_parameter['track0012']['id'], test_parameter['track0013']['id']]}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'violation_got', 'position': 0, 'check': [
        #                 {'key': 'muteAudience', 'value': [test_parameter['track0012']['id'], test_parameter['track0012']['id'], test_parameter['track0011']['id']]}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'message_bcst', 'position': 0, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['track0011']['id']}, 
        #                 {'key': 'content', 'value': '@我是小QA的迷妹 track0011系統自動解除禁言後發送訊息'}
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'message_bcst', 'position': 1, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['track0012']['id']}, 
        #                 {'key': 'content', 'value': '@track0012 track0012管理員解除禁言後發送訊息'}
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'message', 'position': 1, 'check': [
        #                 {'key': 'userId', 'value': test_parameter['track0011']['id']}, 
        #                 {'key': 'content', 'value': '@我是小QA的迷妹 track0011被禁言第一次發送訊息'}
        #             ]
        #         }
        #     ]
        # ),

        # ('踢出的觀眾皆無法再進入此聲聊房，不能踢出官方場控，且被踢出的觀眾會加到違規列表中',  
        #     [
        #         {'user': 'track0011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0), ('vc_room:1', 'book_seat', {}, 1)], 'sleep': 3},
        #         {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0), ('vc_room:1', 'book_seat', {}, 1)], 'sleep': 3},
        #         {'user': 'track0013', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 3},
        #         {'user': 'lv000', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 3},
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'vip', 'seatIndex':0}, 1),
        #                 ('vc_room:1', 'ban_audience', {'targetUserId': test_parameter['track0011']['id'], 'reasonId': 8}, 1)
        #             ], 'sleep': 0
        #         },
        #         {'user': 'broadcaster012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'unban_audience', {'targetUserId': test_parameter['track0011']['id']}, 7),
        #                 ('vc_room:1', 'get_violation', {}, 1)
        #             ], 'sleep': 2
        #         },
        #         {'user': 'broadcaster010', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'ban_audience', {'targetUserId': test_parameter['lv000']['id'], 'reasonId': 10}, 1),
        #                 ('vc_room:1', 'ban_audience', {'targetUserId': test_parameter['broadcaster013']['id'], 'reasonId': 9}, 1),
        #                 ('vc_room:1', 'unban_audience', {'targetUserId': test_parameter['broadcaster013']['id']}, 3),
        #                 ('vc_room:1', 'get_violation', {}, 1)
        #             ], 'sleep': 7
        #         },
        #         {'user': 'broadcaster013', 'wait': 5, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 2}, 1)
        #             ], 'sleep': 1
        #         }
        #     ],
        #     [
        #         {'index': 'track0011', 'event': 'audience_banned', 'position': 0, 'check': [
        #                 {'key': 'targetUserId', 'value': test_parameter['track0011']['id']}, 
        #                 {'key': 'content', 'value': '因違反 惡意謾罵，被踢出房間'}
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': 'err', 'value': 'TARGET_USER_IS_LIVE_CONTROLLER'}
        #             ]
        #         },
        #         {'index': 'broadcaster012', 'event': 'audience_unbanned_bcst', 'position': 1, 'check': [
        #                 {'key': 'banAudiences', 'value': [test_parameter['track0011']['id']]}
        #             ]
        #         },
        #         {'index': 'broadcaster012', 'event': 'violation_got', 'position': 0, 'check': [
        #                 {'key': 'muteAudience', 'value': []},
        #                 {'key': 'banAudience', 'value': []}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'voiceroom_in', 'position': 0, 'check': [
        #                 {'key': 'joinUserId', 'value': [test_parameter['broadcaster013']['id']]},
        #             ]
        #         }
        #     ]
        # ),    

        # ('房主可以取得目前管理員清單，一般管理員及觀眾則無權限取得', 
        #     [
        #         {'user': 'broadcaster010', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0), ('vc_room:1', 'get_admins', {}, 1)], 'sleep': 2},
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0), ('vc_room:1', 'get_admins', {}, 1)], 'sleep': 2},
        #         {'user': 'track0011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0), ('vc_room:1', 'get_admins', {}, 1)], 'sleep': 0}
        #     ], 
        #     [
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'admins_got', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'admins', 'value': [
        #                     test_parameter['broadcaster011']['id'],
        #                     test_parameter['broadcaster012']['id'],
        #                     test_parameter['broadcaster013']['id'],
        #                     test_parameter['broadcaster014']['id']
        #                 ]}
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster011', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': [{'key': 'err', 'value': 'permission_deny'}]
        #         },
        #         {
        #             'index': 'track0011', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': [{'key': 'err', 'value': 'permission_deny'}]
        #         }
        #     ]
        # ),

        # ('房主可以在房內新增刪除管理員，在房及新入房的人員會收到正確的資訊', 
        #     [
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 5},
        #         {'user': 'broadcaster010', 'wait': 1,'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'pickup_admin', {'trueLoveId': test_parameter['broadcaster015']['trueloveId']}, 1),
        #                 ('vc_room:1', 'kickout_admin', {'targetUserId': test_parameter['broadcaster015']['id']}, 5),
        #                 ('vc_room:1', 'pickup_admin', {'trueLoveId': test_parameter['broadcaster021']['trueloveId']}, 1),
        #                 ('vc_room:1', 'pickup_admin', {'trueLoveId': test_parameter['broadcaster011']['trueloveId']}, 1)
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0011', 'wait': 3,'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 1},
        #         {'user': 'track0012', 'wait': 7,'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 0}
        #     ], 
        #     [
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'phx_reply', 
        #             'position': 0,
        #             'check': [{'key': 'err', 'value': 'TARGET_USER_ALREADY_IN_ADMIN_LIST'}]
        #         },
        #         {
        #             'index': 'broadcaster010', 
        #             'event': 'phx_reply', 
        #             'position': 1,
        #             'check': [{'key': 'err', 'value': 'TARGET_USER_IS_NOT_VOICE_MASTER'}]
        #         },
        #         {
        #             'index': 'broadcaster011', 
        #             'event': 'admin_kickedout_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'admins', 'value': [
        #                     test_parameter['broadcaster011']['id'],
        #                     test_parameter['broadcaster012']['id'],
        #                     test_parameter['broadcaster013']['id'],
        #                     test_parameter['broadcaster014']['id']
        #                 ]}
        #             ]
        #         },
        #         {
        #             'index': 'broadcaster011', 
        #             'event': 'admin_pickedup_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'admins', 'value': [
        #                         test_parameter['broadcaster011']['id'],
        #                         test_parameter['broadcaster012']['id'],
        #                         test_parameter['broadcaster013']['id'],
        #                         test_parameter['broadcaster014']['id'],
        #                         test_parameter['broadcaster015']['id']
        #                     ]
        #                 }
        #             ]
        #         },
        #         {
        #             'index': 'track0011', 
        #             'event': 'voiceroom_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'admins', 'value': [
        #                     test_parameter['broadcaster011']['id'],
        #                     test_parameter['broadcaster012']['id'],
        #                     test_parameter['broadcaster013']['id'],
        #                     test_parameter['broadcaster014']['id'],
        #                     test_parameter['broadcaster015']['id']
        #                 ]}
        #             ]
        #         },
        #         {
        #             'index': 'track0012', 
        #             'event': 'voiceroom_in', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'admins', 'value': [
        #                     test_parameter['broadcaster011']['id'],
        #                     test_parameter['broadcaster012']['id'],
        #                     test_parameter['broadcaster013']['id'],
        #                     test_parameter['broadcaster014']['id']
        #                 ]}
        #             ]
        #         },
        #     ]
        # ),

        # ('麥位上的房主、管理員及一般user可以發送sticker(sticker group 1, 2, 3應皆可正常',
        #     [
        #         {'user': 'track0011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 0),
        #                 ('vc_room:1', 'send_sticker', {'stickerId': 11}, 2)
        #             ], 'sleep': 5
        #         },
        #         {'user': 'broadcaster010', 'wait': 1, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'vips', 'seatIndex':0}, 0),
        #                 ('vc_room:1', 'send_sticker', {'stickerId': 47}, 3)
        #             ], 'sleep': 0
        #         },
        #         {'user': 'broadcaster011', 'wait': 3, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:1', 'send_sticker', {'stickerId': 28}, 2)
        #             ], 'sleep': 5
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'track0011', 
        #             'event': 'sticker_sent_bcst', 
        #             'position': 2,
        #             'check': 
        #             [
        #                 {'key': 'sender', 'value': test_parameter['track0011']['id']},
        #                 {'key': 'stickerId', 'value': 11},
        #                 {'key': 'stickerAnimationUrl', 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/backend/photo/e4e229fa385311ebaea742010a8c007a.webp'}
        #             ]
        #         },
        #         {
        #             'index': 'track0011', 
        #             'event': 'sticker_sent_bcst', 
        #             'position': 1,
        #             'check': 
        #             [
        #                 {'key': 'sender', 'value': test_parameter['broadcaster010']['id']},
        #                 {'key': 'stickerId', 'value': 47},
        #                 {'key': 'stickerAnimationUrl', 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/backend/photo/70662b5c385e11ebaea742010a8c007a.png'}
        #             ]
        #         },
        #         {
        #             'index': 'track0011', 
        #             'event': 'sticker_sent_bcst', 
        #             'position': 0,
        #             'check': 
        #             [
        #                 {'key': 'sender', 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': 'stickerId', 'value': 28},
        #                 {'key': 'stickerAnimationUrl', 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/backend/photo/88bf1c86385411ebaea742010a8c007a.webp'}
        #             ]
        #         },
        #     ]
        # ),

        # ('房主封鎖user時，該user會被踢出房間且再也不能進入，但若是管理員封鎖user僅將該user加入黑名單中也可封鎖房主；不能對官方場控做封鎖',
        #     [
        #         {'user': 'track0011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),  
        #                 ('vc_room:1', 'book_seat', {}, 1),
        #                 ('vc_room:1', 'message', {'content': 'track0011封鎖後發送訊息'}, 4),
        #             ], 'sleep': 10
        #         },
        #         {'user': 'track0012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'book_seat', {}, 1)
        #             ], 'sleep': 10
        #         },
        #         {'user': 'lv000', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 3},
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0), 
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'vips', 'seatIndex':0}, 1),
        #                 ('vc_room:1', 'block_audience', {'targetUserId': test_parameter['track0011']['id']}, 1),
        #                 ('vc_room:1', 'block_audience', {'targetUserId': test_parameter['track0014']['id']}, 1),
        #                 ('vc_room:1', 'block_audience', {'targetUserId': test_parameter['broadcaster010']['id']}, 3)
        #             ], 'sleep': 7
        #         },
        #         {'user': 'broadcaster010', 'wait': 3, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'block_audience', {'targetUserId': test_parameter['lv000']['id']}, 1),
        #                 ('vc_room:1', 'block_audience', {'targetUserId': test_parameter['track0012']['id']}, 1),
        #                 ('vc_room:1', 'block_audience', {'targetUserId': test_parameter['track0013']['id']}, 1),
        #                 ('vc_room:1', 'get_violation', {}, 1)
        #             ], 'sleep': 7
        #         },
        #         {'user': 'track0013', 'wait': 7, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 0},
        #         {'user': 'track0014', 'wait': 7, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 0},
        #     ],
        #     [
        #         {'index': 'track0012', 'event': 'audience_blocked', 'position': 0, 'check': [
        #                 {'key': 'targetUserId', 'value': test_parameter['track0012']['id']}, 
        #                 {'key': 'content', 'value': '違反規定，被踢出房間'}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'audience_blocked_bcst', 'position': 0, 'check': [
        #                 {'key': 'content', 'value': '無與倫比的美麗 已被 broadcaster011 封鎖成功'}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'audience_blocked_bcst', 'position': 1, 'check': [
        #                 {'key': 'content', 'value': 'track0013 已被 無與倫比的美麗 封鎖成功'}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'audience_blocked_bcst', 'position': 2, 'check': [
        #                 {'key': 'content', 'value': 'track0012 已被 無與倫比的美麗 封鎖成功'}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'audience_blocked_bcst', 'position': 3, 'check': [ 
        #                 {'key': 'content', 'value': 'track0014 已被 broadcaster011 封鎖成功'}
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'voiceroom_in', 'position': 0, 'check': [
        #                 {'key': 'seatsMute', 'value': []}
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': 'err', 'value': 'USER_BLOCKED'}
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'phx_reply', 'position': 0, 'check': [
        #                 {'key': 'err', 'value': 'TARGET_USER_IS_LIVE_CONTROLLER'}
        #             ]
        #         },
        #     ]
        # ),

        # ('玩家可以追蹤房主及管理者，但不能追一般user',
        #     [
        #         {'user': 'track0011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),  
        #                 ('vc_room:1', 'book_seat', {}, 1),
        #                 ('vc_room:1', 'ping', {}, 5),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),  
        #                 ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0011']['id'], 'seatType': 'vips', 'seatIndex':0}, 1),
        #                 ('vc_room:1', 'ping', {}, 6),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0012', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),  
        #                 ('vc_room:1', 'track', {'liveMasterId': test_parameter['broadcaster011']['id']}, 1),
        #                 ('vc_room:1', 'phx_leave', {}, 1),
        #                 ('vc_room:1', 'phx_join', {}, 1),  
        #                 ('vc_room:1', 'track', {'liveMasterId': test_parameter['broadcaster010']['id']}, 1),
        #                 ('vc_room:1', 'track', {'liveMasterId': test_parameter['track0011']['id']}, 1),
        #                 ('vc_room:1', 'phx_leave', {}, 1),
        #                 ('vc_room:1', 'phx_join', {}, 1),  
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {'index': 'track0012', 'event': 'voiceroom_in', 'position': 0, 'check': [
        #                 {'key': 'tracked', 'value': True}
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'voiceroom_in', 'position': 1, 'check': [
        #                 {'key': 'tracked', 'value': False}
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'phx_reply', 'position': 1, 'check': [
        #                 {'key': 'err', 'value': 'TARGET_USER_IS_LIVE_MASTER'}
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'tracked_bcst', 'position': 1, 'check': [
        #                 {'key': 'roomId', 'value': 1},
        #                 {'key': 'liveMasterId', 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': 'fansId', 'value': test_parameter['track0012']['id']},
        #                 {'key': 'content', 'value': '@track0012 追蹤了 @broadcaster011！'},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'tracked_bcst', 'position': 0, 'check': [
        #                 {'key': 'roomId', 'value': 1},
        #                 {'key': 'liveMasterId', 'value': test_parameter['broadcaster010']['id']},
        #                 {'key': 'fansId', 'value': test_parameter['track0012']['id']},
        #                 {'key': 'content', 'value': '@track0012 追蹤了 @無與倫比的美麗！'},
        #             ]
        #         },
        #     ]
        # ),

        # ('用戶首次分享會增加熱度，但之後再分享即不會增加熱度。每日00：00清除記錄 #3369',
        #     [
        #         {'user': 'track0013', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'share', {}, 1),
        #                 ('vc_room:1', 'phx_leave', {}, 2),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0014', 'wait': 4, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'share', {}, 3),
        #                 ('vc_room:1', 'share', {}, 3),
        #                 ('vc_room:1', 'phx_leave', {}, 3),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0020', 'wait': 5, 'action': [
        #                 ('vc_room:1', 'phx_join', {'code': ''}, 0),
        #                 ('vc_room:1', 'share', {}, 3),
        #                 ('vc_room:1', 'phx_leave', {'code': ''}, 1),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {
        #             'index': 'track0013', 
        #             'event': 'shared_bcst', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster010']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0014', 
        #             'event': 'shared_bcst', 
        #             'position': 1,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0014']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster010']['id']},
        #             ]
        #         },             
        #         {
        #             'index': 'track0014', 
        #             'event': 'shared_bcst', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name} ！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name} ！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name} ！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0014']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster010']['id']},
        #             ]
        #         },                           
        #         {
        #             'index': 'track0020', 
        #             'event': 'shared', 
        #             'position': 0,
        #             'check': [
        #                 {'key': ['content', 'en'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['content', 'zh'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['content', 'ja'], 'value': '{fromUser.name} 分享了 {targetUser.name}，提升了聲聊廳熱度！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0020']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster010']['id']},
        #             ]
        #         },             

        #     ]

        # ),

        # ('用戶reconnect不應造成hot激增 ', #4383
        #     [
        #         {'user': 'track0013', 'wait': 0, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'ping', {}, 20),
        #                 ('vc_room:1', 'phx_leave', {}, 2),
        #             ], 'sleep': 1 
        #         },
        #         {'user': 'track0014', 'wait': 2, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'phx_join', {'action': 'reconnect'}, 3),
        #                 ('vc_room:1', 'phx_join', {'action': 'reconnect'}, 3),
        #                 ('vc_room:1', 'phx_join', {'action': 'reconnect'}, 3),
        #                 ('vc_room:1', 'phx_leave', {}, 3),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0015', 'wait': 12, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 0),
        #                 ('vc_room:1', 'ping', {}, 10),
        #                 ('vc_room:1', 'phx_leave', {}, 2),
        #             ], 'sleep': 1 
        #         },
        #     ],
        #     [
        #     ]
        # ),

        # ('觸發track event的用戶，其數到track的回覆，會依暱稱中是否包含禁詞而不同', #4585 
        #     [
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:8', 'phx_join', {}, 0),  
        #                 ('vc_room:8', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:8', 'phx_leave', {}, 10),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('vc_room:8', 'phx_join', {}, 0),  
        #                 ('vc_room:8', 'track', {'liveMasterId': test_parameter['broadcaster011']['id']}, 1),
        #                 ('vc_room:8', 'phx_leave', {}, 5),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0020', 'wait': 1, 'action': [
        #                 ('vc_room:8', 'phx_join', {}, 0),  
        #                 ('vc_room:8', 'track', {'liveMasterId': test_parameter['broadcaster011']['id']}, 2),
        #                 ('vc_room:8', 'phx_leave', {}, 5),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {'index': 'track0020', 'event': 'tracked_bcst', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['liveMasterId'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['fansId'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['roles'], 'value': ["ROLE_USER"]},
        #                 {'key': ['content'], 'value': '@%s 追蹤了 %s！'%(test_parameter['track0012']['nickname'], test_parameter['broadcaster011']['nickname'])},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'tracked_bcst', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['liveMasterId'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['fansId'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['roles'], 'value': ["ROLE_USER"]},
        #                 {'key': ['content'], 'value': '@%s 追蹤了 %s！'%(test_parameter['track0012']['nickname'], test_parameter['broadcaster011']['nickname'])},
        #             ]
        #         },
        #         {'index': 'track0020', 'event': 'tracked', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['liveMasterId'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['fansId'], 'value': test_parameter['track0020']['id']},
        #                 {'key': ['roles'], 'value': ["ROLE_USER"]},
        #                 {'key': ['content'], 'value': '@%s 追蹤了 %s！'%(test_parameter['track0020']['nickname'], test_parameter['broadcaster011']['nickname'])},
        #             ]
        #         },
        #     ]
        # ),

        # ('推拉流 id 使用方法更新', #4552
        #     [
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:8', 'phx_join', {}, 0),  
        #                 ('vc_room:8', 'take_seat', {'seatIndex': 1 }, 1),
        #                 ('vc_room:8', 'pickup_seat', {'seatIndex': 2, 'targetUserId': test_parameter['track0012']['id'], 'seatType': 'host'}, 2),
        #                 ('vc_room:8', 'pickup_seat', {'seatIndex': 2, 'targetUserId': test_parameter['track0011']['id'], 'seatType': 'host'}, 2),
        #                 ('vc_room:8', 'kickout_seat', {'targetUserId': test_parameter['track0011']['id']}, 2),
        #                 ('vc_room:8', 'phx_leave', {}, 20),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0012', 'wait': 1, 'action': [
        #                 ('vc_room:8', 'phx_join', {}, 0),  
        #                 ('vc_room:8', 'book_seat', {}, 1),
        #                 ('vc_room:8', 'leave_seat', {}, 3),
        #                 ('vc_room:8', 'phx_leave', {}, 1),
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0011', 'wait': 6, 'action': [
        #                 ('vc_room:8', 'phx_join', {}, 0),  
        #                 ('vc_room:8', 'book_seat', {}, 1),
        #                 ('vc_room:8', 'phx_leave', {}, 4),
        #             ], 'sleep': 1
        #         },
        #     ],
        #     [
        #         {'index': 'broadcaster011', 'event': 'seat_taken', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['seats', 'streamId'], 'index': 1, 'value': test_parameter['broadcaster011']['id']},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'voiceroom_in', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['seats', 'streamId'], 'index': 1, 'value': test_parameter['broadcaster011']['id']},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'seat_pickedup', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['seats', 'streamId'], 'index': 2, 'value': test_parameter['track0012']['id']},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'seat_left', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['seats', 'streamId'], 'index': 1, 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['seats', 'streamId'], 'index': 2, 'value': None},
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'seat_kickedout', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['seats', 'streamId'], 'index': 1, 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['seats', 'streamId'], 'index': 2, 'value': None},
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'voiceroom_left_bcst', 'position': 0, 'check': [
        #                 {'key': ['roomId'], 'value': 8},
        #                 {'key': ['seats', 'streamId'], 'index': 1, 'value': None},
        #                 {'key': ['seats', 'streamId'], 'index': 2, 'value': None},
        #             ]
        #         },
        #     ],
        # ),

        # ('過年紅包活動，暖場、抽奬', #4629~4634  不同階段進房及抽奬
        #     [       
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 0), 
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'broadcaster013', 'wait': 1, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         }, 
        #         {'user': 'track0011', 'wait': 3, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #8500
        #                 ('vc_room:3', 'gift', {'giftId': '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 4}, 7), #1700
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 7}, 7), #100
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0012', 'wait': 40, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 30),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 120, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 10), 
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0014', 'wait': 10, 'action': [
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'ping', {}, 30),
        #                 ('vc_room:1', 'ping', {}, 30), 
        #                 ('vc_room:1', 'phx_leave', {}, 10),
        #                 ('vc_room:3', 'phx_join', {}, 10), 
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },

        #     ],  
        #     [
        #         {'index': 'track0013', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 50000},
        #                 {'key': ['targetPoints'], 'value': 100000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 50000},
        #                 {'key': ['targetPoints'], 'value': 100000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 2, 'check': [
        #                 {'key': ['progress'], 'value': 'WARM_UP'},
        #                 {'key': ['gatherPoints'],  'value': 50000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'READY'},
        #                 {'key': ['gatherPoints'],  'value': 50000},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': True},
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包！'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },

        #     ]
        # ),

        # ('過年紅包活動，暖場、抽奬', #4629~4634  都不抽奬，等30秒抽奬時間過後就回到一般狀態
        #     [       
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 0), 
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'broadcaster013', 'wait': 1, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         }, 
        #         {'user': 'track0011', 'wait': 3, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #8500
        #                 ('vc_room:3', 'gift', {'giftId': '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 4}, 7), #1700
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 7}, 7), #100
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 120, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 10), 
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },

        #     ],  
        #     [
        #         {'index': 'track0013', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 50000},
        #                 {'key': ['targetPoints'], 'value': 100000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #     ]
        # ),

        # ('過年紅包活動，暖場、抽奬', #4629~4634 
        #     [       
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 0), 
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'broadcaster013', 'wait': 1, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         }, 
        #         {'user': 'track0011', 'wait': 3, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #8500
        #                 ('vc_room:3', 'gift', {'giftId': '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 4}, 7), #1700
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 7}, 7), #100
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 120, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 10), 
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },

        #     ],  
        #     [
        #         {'index': 'track0013', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 50000},
        #                 {'key': ['targetPoints'], 'value': 100000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #     ]
        # ),

        # ('過年紅包活動，暖場、抽奬', #4629~4634 基本流程
        #     [       
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 0), 
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'broadcaster013', 'wait': 1, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         }, 
        #         {'user': 'track0011', 'wait': 3, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #8500
        #                 ('vc_room:3', 'gift', {'giftId': '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 4}, 7), #1700
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 7}, 7), #100
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 5),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #     ],  
        #     [
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'WARM_UP'},
        #                 {'key': ['gatherPoints'],  'value': 50000},
        #                 {'key': ['targetPoints'], 'value': 100000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 1, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 49300},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 2, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 42500},
        #                 {'key': ['targetPoints'], 'value': 50000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
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
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'phx_reply', 'position': 0, 'check': [
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

        # ('過年紅包活動，暖場、抽奬', #4629~4634 第一輸已抽過的，第二輪應可參加；包括跨多個目標
        #     [       
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 0), 
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'broadcaster013', 'wait': 1, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         }, 
        #         {'user': 'track0011', 'wait': 3, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #8500
        #                 ('vc_room:3', 'gift', {'giftId': '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 4}, 7), #1700
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 7}, 7), #100
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'phx_leave', {}, 20),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 120, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 5), 
        #                 ('vc_room:3', 'gift', {'giftId': '49853090-e4cd-47da-826e-1131388bd6c4', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #50000
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #     ],  
        #     [
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 300000},
        #                 {'key': ['targetPoints'], 'value': 500000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 1, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 2, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 3, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },

        #     ]
        # ),

        # ('過年紅包活動，暖場、抽奬', #4629~4634 第一輸已抽過的，第二輪應可參加；包括跨多個目標
        #     [       
        #         {'user': 'broadcaster011', 'wait': 0, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 0), 
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'phx_leave', {}, 30),
        #             ], 'sleep': 7
        #         }, 
        #         {'user': 'broadcaster013', 'wait': 1, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'take_seat', {'seatIndex': 1}, 1),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 15),
        #                 ('vc_room:3', 'phx_join', {}, 25),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'phx_leave', {}, 30),
        #             ], 'sleep': 3
        #         }, 
        #         {'user': 'track0011', 'wait': 3, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 1), 
        #                 ('vc_room:3', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #8500
        #                 ('vc_room:3', 'gift', {'giftId': '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 4}, 7), #1700
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 7}, 7), #100
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 1}, 0), #100
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 1}, 0), #100
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
        #                 ('vc_room:3', 'phx_leave', {}, 2),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0013', 'wait': 120, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 5), 
        #                 ('vc_room:3', 'gift', {'giftId': '49853090-e4cd-47da-826e-1131388bd6c4', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #50000
        #                 ('vc_room:3', 'ping', {}, 30),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'phx_leave', {}, 3),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0012', 'wait': 390, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 5), 
        #                 ('vc_room:3', 'gift', {'giftId': 'a700b291-362a-42fa-9db4-6d29d4541273', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 2}, 1), #500000
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'ping', {}, 40),
        #                 ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
        #                 ('vc_room:3', 'phx_leave', {}, 30),
        #             ], 'sleep': 3
        #         },
        #         {'user': 'track0014', 'wait': 610, 'action': [
        #                 ('vc_room:3', 'phx_join', {}, 5), 
        #                 ('vc_room:3', 'gift', {'giftId': '49853090-e4cd-47da-826e-1131388bd6c4', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 1}, 1), #50000
        #                 ('vc_room:3', 'phx_leave', {}, 10),
        #             ], 'sleep': 3
        #         },
        #     ],  
        #     [
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 1, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0012']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 2, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 3, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 4, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 5, 'check': [
        #                 {'key': ['level'], 'value': 1},
        #                 {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
        #                 {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください！'},
        #                 {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
        #                 {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
        #                 {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
        #                 {'key': ['url'], 'value': 'xtars://voiceChat/3'},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': [
        #                 {'key': ['progress'], 'value': 'GATHER'},
        #                 {'key': ['gatherPoints'],  'value': 1300200},
        #                 {'key': ['targetPoints'], 'value': 1000000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'luckymoney_finish_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': False},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'luckymoney_finish_bcst', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': False},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },
        #         {
        #             'index': 'track0014', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': []
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 0, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 1, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 2, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 3, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 4, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'track0011', 'event': 'luckymoney_lottery', 'position': 5, 'check': [
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'],  'value': False},
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'luckymoney_data_changed_bcst', 'position': 9, 'check': [
        #                 {'key': ['progress'], 'value': 'WARM_UP'},
        #                 {'key': ['gatherPoints'],  'value': 300000},
        #                 {'key': ['targetPoints'], 'value': 100000},
        #                 {'key': ['displayed'], 'value': True},
        #                 {'key': ['clicked'], 'value': False},
        #             ]
        #         },

        #     ]
        # ),        

        ('過年紅包活動，暖場、抽奬', #4629~4634 第一輸已抽過的，第二輪應可參加；包括跨多個目標
            [       
                {'user': 'broadcaster011', 'wait': 0, 'action': [
                        ('vc_room:3', 'phx_join', {}, 0), 
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'phx_leave', {}, 10),
                    ], 'sleep': 7
                }, 
                {'user': 'broadcaster013', 'wait': 1, 'action': [
                        ('vc_room:3', 'phx_join', {}, 1), 
                        ('vc_room:3', 'take_seat', {'seatIndex': 1}, 1),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
                        ('vc_room:3', 'phx_leave', {}, 15),
                        ('vc_room:3', 'phx_join', {}, 25),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'phx_leave', {}, 10),
                    ], 'sleep': 3
                }, 
                {'user': 'track0011', 'wait': 3, 'action': [
                        ('vc_room:3', 'phx_join', {}, 1), 
                        ('vc_room:3', 'gift', {'giftId': '9e63bbf0-3e86-4019-b3fc-e955c175569b', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #8500
                        ('vc_room:3', 'gift', {'giftId': '9024cddc-b9be-40d1-92a3-7e78cb5de592', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 4}, 7), #1700
                        ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 7}, 7), #100
                        ('vc_room:3', 'ping', {}, 30),
                        ('vc_room:3', 'ping', {}, 30),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 15),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 1}, 0), #100
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'gift', {'giftId': 'e1e828ca-8bcf-4066-8a00-531ea75fdbb2', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 1}, 0), #100
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 20),
                        ('vc_room:3', 'phx_leave', {}, 30),
                    ], 'sleep': 3
                },
                {'user': 'track0013', 'wait': 120, 'action': [
                        ('vc_room:3', 'phx_join', {}, 5), 
                        ('vc_room:3', 'gift', {'giftId': '49853090-e4cd-47da-826e-1131388bd6c4', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 5}, 1), #50000
                        ('vc_room:3', 'ping', {}, 30),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'ping', {}, 40),
                        ('vc_room:3', 'luckymoney_lottery', {"type": "2022CN.Lottery"}, 10),
                        ('vc_room:3', 'phx_leave', {}, 10),
                    ], 'sleep': 3
                },
                {'user': 'track0012', 'wait': 370, 'action': [
                        ('vc_room:3', 'phx_join', {}, 5), 
                        ('vc_room:3', 'gift', {'giftId': 'a700b291-362a-42fa-9db4-6d29d4541273', 'targetUserId': test_parameter['broadcaster011']['id'], 'count': 2}, 1), #500000
                        ('vc_room:3', 'phx_leave', {}, 10),
                    ], 'sleep': 3
                },
            ],  
            [
                {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 0, 'check': [
                        {'key': ['level'], 'value': 1},
                        {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                        {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください!'},
                        {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
                        {'key': ['url'], 'value': 'xtars://voiceChat/3'},
                    ]
                },
                {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 1, 'check': [
                        {'key': ['level'], 'value': 1},
                        {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                        {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください!'},
                        {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
                        {'key': ['url'], 'value': 'xtars://voiceChat/3'},
                    ]
                },
                {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 2, 'check': [
                        {'key': ['level'], 'value': 1},
                        {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                        {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください!'},
                        {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0013']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
                        {'key': ['url'], 'value': 'xtars://voiceChat/3'},
                    ]
                },
                {'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 3, 'check': [
                        {'key': ['level'], 'value': 1},
                        {'key': ['content', 'zh'],  'value': '{targetUser.name} 準備送紅包了~大家快來搶紅包!'},
                        {'key': ['content', 'ja'],  'value': '{targetUser.name} 赤い封筒を渡す準備ができました〜みんな、赤い封筒を持ってきてください!'},
                        {'key': ['content', 'en'],  'value': '{targetUser.name} Ready to give lucky points~ everyone, come and grab it!'},
                        {'key': ['fromUser', 'id'], 'value': test_parameter['track0011']['id']},
                        {'key': ['targetUser', 'id'], 'value': test_parameter['broadcaster011']['id']},
                        {'key': ['url'], 'value': 'xtars://voiceChat/3'},
                    ]
                },
                {
                    'index': 'track0011', 'event': 'luckymoney_marquee', 'position': 4, 'check': []
                },
                {
                    'index': 'track0012', 'event': 'luckymoney_data_changed_bcst', 'position': 0, 'check': []
                },


            ]
        ),        

    ]   
    return testData