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
        #                 {'key': 'hot', 'value': 2*1331}
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
        #         {'user': 'track0013', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 0},
        #         {'user': 'track0014', 'wait': 7, 'action': [('vc_room:1', 'phx_join', {}, 0)], 'sleep': 0}
        #     ], 
        #     [
        #         {'index': 'track0012', 'event': 'seat_taken', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': test_parameter['broadcaster011']['id']}, 
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'track0012', 'event': 'seat_left', 'position': 0, 'check': 
        #             [
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': None}, 
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'track0013', 'event': 'voiceroom_in', 'position': 0, 'check':[
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': test_parameter['broadcaster011']['id']}, 
        #                         {'seat': 2, 'userId': None}
        #                     ]
        #                 }
        #             ]
        #         },
        #         {'index': 'track0014', 'event': 'voiceroom_in', 'position': 0, 'check':[
        #                 {'key': 'seats', 'value': [
        #                         {'seat': 0, 'userId': None}, 
        #                         {'seat': 1, 'userId': None},  
        #                         {'seat': 2, 'userId': None}]
        #                 }
        #             ]
        #         }
        #     ]
        # ), 
        # ('有人申請上麥，在房中及後進房的人會收到相關資訊, 且離房後會清除上麥申請',  #目前後進房的人，若無麥位申請刪除則無法得到該queue的資訊，此狀況待補
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
        # )
        ('有人申請上麥，房主、管理員及自己可以取消申請',  
            [ 
                {'user': 'broadcaster010', 'wait': 0, 'action': [
                        ('vc_room:1', 'phx_join', {}, 0),
                        ('vc_room:1', 'reject_seat', {'targetUserId': test_parameter['track0011']['id']}, 3)
                    ], 
                    'sleep': 2
                },
                {'user': 'broadcaster011', 'wait': 0, 'action': [
                        ('vc_room:1', 'phx_join', {}, 0), 
                        ('vc_room:1', 'take_seat', {'seatIndex': 1 }, 1),
                        ('vc_room:1', 'reject_seat', {'targetUserId': test_parameter['track0012']['id']}, 5)
                    ], 
                    'sleep': 8
                },
                {'user': 'track0011', 'wait': 1, 'action': [
                        ('vc_room:1', 'phx_join', {}, 0), 
                        ('vc_room:1', 'book_seat', {}, 1)
                    ], 
                    'sleep': 4
                },
                {'user': 'track0012', 'wait': 1, 'action': [
                        ('vc_room:1', 'phx_join', {}, 0), 
                        ('vc_room:1', 'book_seat', {}, 1)
                    ], 
                    'sleep': 4
                },
                {'user': 'track0013', 'wait': 1, 'action': [
                        ('vc_room:1', 'phx_join', {}, 0), 
                        ('vc_room:1', 'book_seat', {}, 1),
                        ('vc_room:1', 'abort_seat', {}, 6)
                    ], 
                    'sleep': 4
                },
            ], 
            [
                {'index': 'broadcaster010', 'event': 'seat_rejected', 'position': 0, 'check': 
                    [
                        {'key': 'seatQueue', 'value': [
                                test_parameter['track0013']['id']
                            ]
                        }
                    ]
                },
                {'index': 'broadcaster010', 'event': 'seat_rejected', 'position': 1, 'check': 
                    [
                        {'key': 'seatQueue', 'value': [
                                test_parameter['track0013']['id'],
                                test_parameter['track0012']['id']
                            ]
                        }
                    ]
                },
                {'index': 'broadcaster010', 'event': 'seat_aborted', 'position': 0, 'check': 
                    [
                        {'key': 'seatQueue', 'value': []}
                    ]
                }
            ]
        )


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
        #             'index': 'broadcaster010', 
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
        #                 ('vc_room:1', 'phx_join', {}, 1), 
        #                 ('vc_room:1', 'pickup_admin', {'targetUserId': test_parameter['broadcaster015']['id']}, 1),
        #                 ('vc_room:1', 'kickout_admin', {'targetUserId': test_parameter['broadcaster015']['id']}, 1)
        #             ], 'sleep': 1
        #         },
        #         {'user': 'track0011', 'wait': 4,'action': [('vc_room:1', 'phx_join', {}, 1)], 'sleep': 1},
        #         {'user': 'track0012', 'wait': 6,'action': [('vc_room:1', 'phx_join', {}, 1)], 'sleep': 0}
        #     ], 
        #     [
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
        # )
        
    ]   
    return testData