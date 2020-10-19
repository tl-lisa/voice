import time
import json
import pytest
import threading
import random
import types
import traceback
from pprint import pprint
from . import voicelib
from . import dbConnect
from . import misc
from . import testingCase

env = 'QA'
env = 'QA'
DB = '35.234.17.150'
test_parameter = {}
idlist = []
header = {'Connection': 'Keep-alive', 'X-Auth-Token': '', 'X-Auth-Nonce': ''}

misc.get_test_data(env, test_parameter)  
def createVoiceRoom(account):
    sqlStr   = "insert into sticker_group set name = 'smile', status = 1, created_at = '2020-06-30 19:21:32', "
    sqlStr  += "updated_at = '2020-06-30 19:21:32', create_user_id = 'lisa', update_user_id = 'lisa'"
    sqlStr1  = "insert into voice_chat_type set name = 'qa_test', background_image_url = 'http://yahoo.com.tw', "
    sqlStr1 += "sticker_group_id = 1, max_seats = 3, max_vip_seats = 1"  
    sqlList = [sqlStr, sqlStr1]
    dbConnect.dbSetting(DB, sqlList)
    header['X-Auth-Token'] = test_parameter['tl-lisa']['token']
    header['X-Auth-Nonce'] = test_parameter['tl-lisa']['nonce']
    apiName = '/api/v2/backend/voiceChat'
    body = {
        'typeId':1,
        'masterId': test_parameter[account]['id'],
        'title': account+'的直播間',
        'description': '快來加入'+account+'的直播間吧！',
        'password': '',
        'streamId':[
            'voiceChat_1_1',
            'voiceChat_1_2',
            'voiceChat_1_3'
        ]
    }
    misc.apiFunction(test_parameter['prefix'], header, apiName, 'post', body)
    return 
      

@pytest.fixture(scope="class")
def editInit():
    sqlStr  = "update remain_points set remain_points = 15000, ratio = 3 where identity_id in ('" + test_parameter['track0019']['id'] + "', '"
    sqlStr += test_parameter['track0020']['id'] + "')"
    dbConnect.dbSetting(test_parameter['db'], [sqlStr])
    # 建立聲聊房資訊。若已建立則不需再call
    # misc.clearVoice(test_parameter['db'])
    # misc.clearCache(test_parameter['db'])
    # createVoiceRoom('broadcaster010')
    # header['X-Auth-Token'] = test_parameter['broadcaster010']['token']
    # header['X-Auth-Nonce'] = test_parameter['broadcaster010']['nonce']
    # for i in range(11, 15):
    #     admin = 'broadcaster0' + str(i)
    #     apiName = '/api/v2/liveMaster/voiceChat/admin'
    #     body = {
    #         'roomId': 1,
    #         'userId': test_parameter[admin]['id']
    #     }
    #     misc.apiFunction(test_parameter['prefix'], header, apiName, 'post', body)
    # header['X-Auth-Token'] = test_parameter['tl-lisa']['token']
    # header['X-Auth-Nonce'] = test_parameter['tl-lisa']['nonce']
    # misc.changeRole(test_parameter['prefix'], test_parameter['tl-lisa']['token'], test_parameter['tl-lisa']['nonce'], [test_parameter['broadcaster014']['id']], 4)
    
#check中的資料先以第一層為主，之後再看下層資料
testData = [
    # ('觀眾若未上麥申請就取消上麥，應有錯誤', [
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'track0013', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'abort_seat', {})], 'sleep': 0}],
    # [{'index': 'track0013', 'event': 'seat_aborted', 'check': [{'key': 'seatQueue', 'value': [test_parameter['track0012']['id']]}]}])
    # ('房主可拉觀眾上麥', [
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster010', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_pickedup', 'check': [{'key': 'seatQueue', 'value': []}, {'key': 'vips', 'value': [{'seat': 0, 'userId': test_parameter['track0012']['id']}]}]}]),
    # ('若管理員未申請上麥，房主可拉管理員上麥?', [ 
    # {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 6}, 
    # {'user': 'broadcaster010', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['broadcaster011']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_pickedup', 'check': [{'key': 'seatQueue', 'value': []}, {'key': 'vips', 'value': [{'seat': 0, 'userId': test_parameter['broadcaster011']['id']}]}]}])
    # ('房主可拉管理員上麥', [ 
    # {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster010', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['broadcaster011']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_pickedup', 'check': [{'key': 'seatQueue', 'value': []}, {'key': 'vips', 'value': [{'seat': 0, 'userId': test_parameter['broadcaster011']['id']}]}]}]),
    # ('房主可拉觀眾上麥', [  
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster010', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_pickedup', 'check': [{'key': 'seatQueue', 'value': []}, {'key': 'vips', 'value': [{'seat': 0, 'userId': test_parameter['track0012']['id']}]}]}]),
    # ('管理員可拉管理員上麥', [ 
    # {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster012', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['broadcaster011']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'broadcaster012', 'event': 'seat_pickedup', 'check': [{'key': 'seatQueue', 'value': []}, {'key': 'vips', 'value': [{'seat': 0, 'userId': test_parameter['broadcaster011']['id']}]}]}]),
    # ('管理員可拉觀眾上麥', [  
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster011', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'broadcaster011', 'event': 'seat_pickedup', 'check': [{'key': 'seatQueue', 'value': []}, {'key': 'vips', 'value': [{'seat': 0, 'userId': test_parameter['track0012']['id']}]}]}]),
    # ('觀眾不可拉觀眾上麥', [  
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'track0013', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'track0013', 'event': 'phx_reply', 'check': [{'key': 'err', 'value': 'permission_deny'}]}]),
    # ('官方場控不可拉觀眾上麥', [  
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'lv000', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0})], 'sleep': 0}], 
    # [{'index': 'lv000', 'event': 'phx_reply', 'check': [{'key': 'err', 'value': 'permission_deny'}]}]),
    # ('房主可請管理員下麥', [  
    # {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster010', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['broadcaster011']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_kickedout', 'check': [{'key': 'seats', 'value': [{'seat': 0, 'userId': test_parameter['broadcaster010']['id']},
    # {'seat': 1, 'userId': None}, {'seat': 2, 'userId': None}]}]}]),
    # ('房主可請觀眾下麥', [  
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster010', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}),
    # ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['track0012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_kickedout', 'check': [{'key': 'vips', 'value': [{'seat': 0, 'userId': None}]}]}]),
    # ('管理員可請管理員下麥', [  
    # {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster012', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['broadcaster011']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster012', 'event': 'seat_kickedout', 'check': [{'key': 'seats', 'value': [{'seat': 0, 'userId': None}, {'seat': 1, 'userId': None}, {'seat': 2, 'userId': None}]}]}]),
    # ('管理員可請觀眾下麥', [   
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster011', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}),
    # ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['track0012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster011', 'event': 'seat_kickedout', 'check': [{'key': 'vips', 'value': [{'seat': 0, 'userId': None}]}]}]),
    # ('管理員不可請房主下麥', [    
    # {'user': 'broadcaster010', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 6}, 
    # {'user': 'broadcaster011', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['broadcaster010']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster011', 'event': 'phx_reply', 'check': [{'key': 'err', 'value': 'permission_deny'}]}]),
    # ('觀眾不可請管理員下麥', [     
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'track0012', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), 
    # ('vc_room:1', 'kickout_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 0}], 
    # [{'index': 'track0012', 'event': 'phx_reply', 'check': [{'key': 'err', 'value': 'permission_deny'}]}]),
    # ('房主如在房不能自動下麥', [   
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster010', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'leave_seat', {})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'phx_reply', 'check': [{'key': 'err', 'value': 'owner_can_not_leave_seat'}]}]),
    # ('管理員自動下麥應正常', [     
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster011', 'wait': 3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 2}),   ('vc_room:1', 'leave_seat', {})], 'sleep': 0}], 
    # [{'index': 'broadcaster012', 'event': 'seat_left', 'check': [{'key': 'seats', 'value': [{'seat': 0, 'userId': None}, {'seat': 1, 'userId': test_parameter['broadcaster012']['id']}, {'seat': 2, 'userId': None}]}]}]),
    # ('房主可對觀眾及管理員禁音', [      
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 12}, 
    # {'user': 'track0012', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {}),  ('vc_room:1', 'book_seat', {})], 'sleep': 9}, 
    # {'user': 'broadcaster010', 'wait': 5, 'action': [('vc_room:1', 'phx_join', {}),
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}),
    # ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['track0012']['id']}), ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}),
    # ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['track0012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_muted', 'check': [{'key': 'seatsMute', 'value': [test_parameter['track0012']['id'], test_parameter['broadcaster012']['id']]}]}]),
    # ('管理員可對觀眾禁音', [      
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}),  ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster012', 'wait':3, 'action': [('vc_room:1', 'phx_join', {}),
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}),
    # ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['track0012']['id']}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['track0012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster012', 'event': 'seat_muted', 'check': [{'key': 'seatsMute', 'value': [test_parameter['track0012']['id']]}]}]),
    # ('房主可對觀眾及管理員取消禁音', [      
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 12}, 
    # {'user': 'track0012', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {}),  ('vc_room:1', 'book_seat', {})], 'sleep': 9}, 
    # {'user': 'broadcaster010', 'wait': 5, 'action': [('vc_room:1', 'phx_join', {}),
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}),
    # ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['track0012']['id']}), ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}),
    # ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['track0012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster010', 'event': 'seat_unmuted', 'check': [{'key': 'seatsMute', 'value': []}]}]),
    # ('管理員可對觀眾取消禁音', [      
    # {'user': 'track0012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}),  ('vc_room:1', 'book_seat', {})], 'sleep': 6}, 
    # {'user': 'broadcaster012', 'wait':3, 'action': [('vc_room:1', 'phx_join', {}),
    # ('vc_room:1', 'pickup_seat', {'targetUserId': test_parameter['track0012']['id'], 'seatType': 'vips', 'seatIndex': 0}),
    # ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['track0012']['id']}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['track0012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster012', 'event': 'seat_unmuted', 'check': [{'key': 'seatsMute', 'value': []}]}])
    # ('管理員可對管理員禁音', [       
    # {'user': 'broadcaster011', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster012', 'wait':3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 2}), 
    # ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster011']['id']})], 'sleep': 3},
    # {'user': 'broadcaster010', 'wait': 5, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster011']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster012', 'event': 'phx_reply', 'check':  [{'key': 'seatsMute', 'value': []}]}]),
    # ('一般身份的直播主不可對管理員禁音', [       
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster018', 'wait':3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 3},
    # {'user': 'broadcaster010', 'wait': 5, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster018', 'event': 'phx_reply', 'check': [{'key': 'err', 'value': 'permission_deny'}]}]),
    # ('觀眾不可對管理員禁音', [       
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'track0012', 'wait':3, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 3},
    # {'user': 'broadcaster010', 'wait': 5, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 0}], 
    # [{'index': 'track0012', 'event': 'phx_reply', 'check': [{'key': 'err', 'value': 'permission_deny'}]}]),
    # ('管理員可對管理員取消禁音', [       
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster011', 'wait': 5, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']}),
    # ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster011', 'event': 'phx_reply', 'check': [{'key': 'seatsMute', 'value': []}]}])
    # ('被禁音的管理員也可以正常收到訊息廣播', [      
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 10}, 
    # {'user': 'broadcaster011', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'mute_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 2},
    # {'user': 'broadcaster013', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'message', {'content': 'broadcaster13 發送訊息'})], 'sleep': 4},
    # {'user': 'broadcaster010', 'wait': 7, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'unmute_seat', {'targetUserId': test_parameter['broadcaster012']['id']})], 'sleep': 0}], 
    # [{'index': 'broadcaster012', 'event': 'message_bcst', 'check': [{'key': 'userId', 'value': test_parameter['broadcaster013']['id']}, {'key': 'content', 'value': '@直播主13 broadcaster13 發送訊息'}]}]),
    # ('訊息包含文字嶽的就不發送', [      
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 6}, 
    # {'user': 'broadcaster013', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'message', {'content': 'broad點數代儲caster13請call'})], 'sleep': 1}], 
    # [{'index': 'broadcaster012', 'event': 'message_bcst', 'check': []}]),
    # ('暱稱包含文字嶽的就不發送', [      
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 7}, 
    # {'user': 'broadcaster013', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 5}, 
    # {'user': 'track0020', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'message', {'content': '歡迎大家搜尋找碴'})], 'sleep': 4}], 
    # [{'index': 'broadcaster013', 'event': 'message_bcst', 'check': []}]), 
    # ('暱稱包含文字嶽的就不發送,但自己會看到', [      
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 7}, 
    # {'user': 'broadcaster013', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 5}, 
    # {'user': 'track0020', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'message', {'content': '歡迎大家搜尋找碴'})], 'sleep': 4}], 
    # [{'index': 'track0020', 'event': 'message', 'check': [{'key': 'userId', 'value': test_parameter['track0020']['id']}, {'key': 'content', 'value': '@快樂代儲你我他 歡迎大家搜尋找碴'}]}]),
    # ('暱稱包含文字嶽的就不發送,但自己會看到', [      
    # {'user': 'broadcaster012', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 7}, 
    # {'user': 'broadcaster013', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 5}, 
    # {'user': 'track0020', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'message', {'content': '歡迎大家搜尋找碴'})], 'sleep': 4}], 
    # [{'index': 'track0020', 'event': 'message', 'check': [{'key': 'userId', 'value': test_parameter['track0020']['id']}, {'key': 'content', 'value': '@快樂代儲你我他 歡迎大家搜尋找碴'}]}]),
    # ('暱稱有包含文字嶽的訊息，送禮訊息只有收禮者跟送禮者會收到', [      #此case尚未實做⋯⋯
    # {'user': 'broadcaster010', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 7}, 
    # {'user': 'broadcaster013', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 5}, 
    # {'user': 'track0020', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'message', {'content': '歡迎大家搜尋找碴'})], 'sleep': 1}], 
    # [{'index': 'track0020', 'event': 'message', 'check': [{'key': 'userId', 'value': test_parameter['track0020']['id']}, {'key': 'content', 'value': '@快樂代儲你我他 歡迎大家搜尋找碴'}]},
    # {'index': 'broadcaster010', 'event': 'message', 'check': [{'key': 'userId', 'value': test_parameter['track0020']['id']}, {'key': 'content', 'value': '@快樂代儲你我他 歡迎大家搜尋找碴'}]},
    # {'index': 'broadcaster013', 'event': 'message', 'check': [{'key': 'userId', 'value': test_parameter['track0020']['id']}, {'key': 'content', 'value': '@快樂代儲你我他 歡迎大家搜尋找碴'}]}]),
    # ('送禮訊息在聲聊房中皆會收到', [       
    # {'user': 'broadcaster010', 'wait': 0, 'action': [('vc_room:1', 'phx_join', {})], 'sleep': 7}, 
    # {'user': 'broadcaster013', 'wait': 2, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'take_seat', {'seatIndex': 1})], 'sleep': 5}, 
    # {'user': 'track0019', 'wait': 4, 'action': [('vc_room:1', 'phx_join', {}), ('vc_room:1', 'gift', 
    # {'giftId': '04310750-994e-41d3-8b2c-62674df24db2', 'targetUserId': test_parameter['broadcaster013']['id'], 'count': 3})], 'sleep': 1}], 
    # [{'index': 'track0019', 'event': 'gift_bcst', 'check': [{'key': 'fromUserId', 'value': test_parameter['track0019']['id']}, 
    # {'key': 'targetUserId', 'value': test_parameter['broadcaster013']['id']}, {'key': 'giftUrl', 'value': 'https://d3eq1e23ftm9f0.cloudfront.net/gift/animation/5f5101e86ce911ea83b942010a8c0017.jpeg'}]},
    # {'index': 'broadcaster010', 'event': 'gift_bcst', 'check': [{'key': 'giftId', 'value': '04310750-994e-41d3-8b2c-62674df24db2'}, {'key': 'giftName', 'value': '鬼怪'}, {'key': 'multiple', 'value': True}]},
    # {'index': 'broadcaster013', 'event': 'gift_bcst', 'check': [{'key': 'count', 'value': 3}, {'key': 'point', 'value': 1500}, {'key': 'content', 'value': '@舞弊事件大家都不能接受 送了 鬼怪(500) x 3 禮物給 直播主13'}]}]),

   
]   
 
class TestVoiceScoket(): 
    wsDic = {}
    def wsJob(self, data, id):
        #print('%d start at %d'%(id, int(time.time())))
        eventList = []
        for j in data['action']:
            ref1 = str(int(time.time()*1000))
            body = {
                'ref': ref1,
                'join_ref': ref1,
                'topic': j[0],
                'event': j[1],
                'payload': j[2],
                'sleep': j[3]
            }
            eventList.append(body)
        account = data['user']
        info  = 'ws://'+test_parameter['db']+'/socket/websocket?token='+test_parameter[account]['token'] + '&nonce=' + test_parameter[account]['nonce']
        voice = voicelib.voiceUser(info, eventList, data['sleep'], data['wait'], id)
        try:
            self.wsDic[account] = voice.messageList
        except Exception as err:
            print('get Error: ', err)
        finally:
            del voice

    def verifyResult(self, data, verifyInfo):
        isGetEvent = False 
        position = 0
        event = None
        for i in data:
            # print('data event=', i['event'],' verify event=',verifyInfo['event'], ' position=', position,' verify position=',verifyInfo['position'])
            if i['event'] == verifyInfo['event']:
                if verifyInfo['position'] == position:
                    isGetEvent = True
                    event = i
                    break
                else:
                    position += 1
        if verifyInfo['check']:
            assert isGetEvent
        else:
            assert not isGetEvent
        if isGetEvent:
            for j in verifyInfo['check']:
                count = 0
                tmp = event
                isGetKey = False
                while not isGetKey:
                    if tmp:
                        for key, value in tmp.items():
                            if key == j['key']:
                                if j['value'] and type(j['value']) == list:
                                    isGetValue = False
                                    for vv in j['value']:
                                        isGetValue = True if vv in value else False
                                    assert isGetValue
                                else:
                                    assert j['value'] == value
                                isGetKey = True
                                break
                            else:
                                if type(value) == dict:
                                    tmp = tmp[key]
                                    break
                    else:
                        break
                    if count > 8:
                        break
                    else:
                        count += 1                   
                assert isGetKey, "Cannot get key("+j['key']+ ")"
                        
    @pytest.mark.parametrize("scenario, data, verifyInfo", testingCase.getTestData(test_parameter))
    def testVoice(self, editInit, scenario, data, verifyInfo):   
        threadList = []
        self.wsDic.clear()
        for i in range(len(data)):
            threadList.append(threading.Thread(target = self.wsJob, args = (data[i], i, )))
            threadList[i].start()
        for i in reversed(threadList):
            i.join()
        pprint(self.wsDic)   
        for k in verifyInfo:
            if self.wsDic[k['index']]:
                self.verifyResult(self.wsDic[k['index']], k) 
            else:
                print('無資料比對')
                
           