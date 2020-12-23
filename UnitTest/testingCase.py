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
        # )

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
        #                 {'key': 'err', 'value': 'you_have_no_more_points'}
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'marquee', 'position': 0, 'check': [
        #                 {'key': 'content', 'value': '恭喜無與倫比的美麗,獲得舞弊事件大家都不能接受送的烤雞全餐 ~太帥了!就是狂!'},
        #             ]
        #         },
        #         {'index': 'broadcaster010', 'event': 'gift_bcst', 'position': 0, 'check': [
        #                 {'key': 'fromUserId', 'value': test_parameter['track0019']['id']}, 
        #                 {'key': 'targetUserId', 'value': test_parameter['broadcaster010']['id']}, 
        #                 {'key': 'giftUrl', 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/e84bd3921b4411eb917342010a8c0050.webp'},
        #                 {'key': 'giftId', 'value': '9e63bbf0-3e86-4019-b3fc-e955c175569b'}, 
        #                 {'key': 'giftName', 'value': '烤雞全餐'}, 
        #                 {'key': 'multiple', 'value': False},
        #                 {'key': 'count', 'value': 1}, 
        #                 {'key': 'point', 'value': 100000}, 
        #                 {'key': 'content', 'value': '舞弊事件大家都不能接受 送了 1 個 烤雞全餐 (100,000) 給 無與倫比的美麗'}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'gift_bcst', 'position': 0, 'check': [ #這個case有問題⋯⋯需再驗一次
        #                 {'key': 'fromUserId', 'value': test_parameter['track0020']['id']}, 
        #                 {'key': 'targetUserId', 'value': test_parameter['broadcaster013']['id']}, 
        #                 {'key': 'giftUrl', 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/86a291301b4411eb917342010a8c0050.webp'},
        #                 {'key': 'giftId', 'value': 'fdbafd5c-93fe-4893-8e7b-7aa6eea209a8'}, 
        #                 {'key': 'giftName', 'value': '南瓜派'}, 
        #                 {'key': 'multiple', 'value': False},
        #                 {'key': 'count', 'value': 3}, 
        #                 {'key': 'point', 'value': 1000}, 
        #                 {'key': 'content', 'value': '快樂代儲你我他 送了 鬼怪(1000) x 3 禮物給 直播主13'}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'gift_bcst', 'position': 1, 'check': [
        #                 {'key': 'fromUserId', 'value': test_parameter['track0019']['id']}, 
        #                 {'key': 'targetUserId', 'value': test_parameter['broadcaster010']['id']}, 
        #                 {'key': 'giftUrl', 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/e84bd3921b4411eb917342010a8c0050.webp'},
        #                 {'key': 'giftId', 'value': '9e63bbf0-3e86-4019-b3fc-e955c175569b'}, 
        #                 {'key': 'giftName', 'value': '烤雞全餐'}, 
        #                 {'key': 'multiple', 'value': False},
        #                 {'key': 'count', 'value': 1}, 
        #                 {'key': 'point', 'value': 100000}, 
        #                 {'key': 'content', 'value': '舞弊事件大家都不能接受 送了 1 個 烤雞全餐(100,000) 給 無與倫比的美麗'}
        #             ]
        #         },
        #         {'index': 'broadcaster013', 'event': 'marquee', 'position': 0, 'check': [
        #                 {'key': 'content', 'value': '恭喜無與倫比的美麗,獲得舞弊事件大家都不能接受送的幸福燃點 ~太帥了!就是狂!'}
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
        #                 ('vc_room:1', 'pickup_admin', {'trueLoveId': test_parameter['broadcaster021']['trueloveId']}, 1)
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
        #             'check': [{'key': 'err', 'value': 'target_user_is_not_live_master'}]
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
        #                     test_parameter['broadcaster011']['id'],
        #                     test_parameter['broadcaster012']['id'],
        #                     test_parameter['broadcaster013']['id'],
        #                     test_parameter['broadcaster014']['id'],
        #                     test_parameter['broadcaster015']['id']
        #                 ]}
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

        # ('房主封鎖user時，該user會被踢出房間且再也不能進入，但若是管理員封鎖user僅將該user加入黑名單中；不能對官方場控做封鎖',
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
        #         {'user': 'broadcaster011', 'wait': 1, 'action': [
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
        #                 {'key': 'content', 'value': '封鎖成功'}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'audience_blocked_bcst', 'position': 1, 'check': [
        #                 {'key': 'content', 'value': '封鎖成功'}
        #             ]
        #         },
        #         {'index': 'broadcaster011', 'event': 'phx_reply', 'position': 0, 'check': [ #不可封鎖房主，但目前結果是可以的。已回bug
        #                 {'key': 'err', 'value': 'PERMISSION_DENY'}
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
        # )

    ]   
    return testData