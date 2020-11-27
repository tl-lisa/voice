import json
import time
import sys
import requests
import paramiko
from pprint import pprint
from . import dbConnect



def get_test_data(env, test_parameter):    
    if env == 'QA':
        test_parameter['prefix'] = 'http://35.234.17.150'
        test_parameter['db'] = '35.234.17.150'
    elif env == 'test':
        test_parameter['prefix'] = 'http://testing-api.truelovelive.com.tw'
        test_parameter['db'] = 'testing-api.truelovelive.com.tw'
    test_parameter['errAccount'] = {'token': 'aa24385', 'nonce': 'noceiw'}
    sqlStr  = "select login_id, id, token, nonce from identity "
    sqlStr += "where login_id in ('tl-lisa', 'lv000', 'lv001', 'lv002', '"
    for i in range(10, 30):
        account = 'track00' + str(i)
        sqlStr += account + "', '" if i < 29 else account + "')"
        if i < 20:
            account = 'broadcaster0' + str(i)
            sqlStr += account + "', '"
    result = dbConnect.dbQuery(test_parameter['db'], sqlStr)
    for i in result:
        test_parameter[i[0]] = {
            'id': i[1],
            'token': i[2],
            'nonce': i[3]
        }
    #pprint(test_parameter)
    sqlStr  = "INSERT INTO remain_points(remain_points, ratio, identity_id) VALUES ("
    sqlStr += "20000, 4, '" + test_parameter['track0020']['id'] + "') ON DUPLICATE KEY "
    sqlStr += "UPDATE remain_points = 20000, ratio = 4"
    sqlStr1  = "UPDATE remain_points SET remain_points = 200000 WHERE identity_id = '"
    sqlStr1 += test_parameter['track0019']['id'] + "'"
    sqlStr2 = "TRUNCATE TABLE user_blocks"
    dbConnect.dbSetting(test_parameter['db'], [sqlStr, sqlStr1, sqlStr2])
    return

def clearVoice(db):
    sqlList = []
    tableList = ['sticker', 'voice_chat_admin', 'voice_chat_history', 'voice_chat_stream']
    for i in tableList:
        sqlStr = "TRUNCATE TABLE " + i
        sqlList.append(sqlStr)   
    deleteList = ['voice_chat_room', 'voice_chat_type', 'sticker_group'] 
    for tableName in deleteList:
        sqlList.append("delete from " + tableName)
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def clearSticker(db):
    sqlList = []
    tableList = ['sticker']
    for i in tableList:
        sqlStr = "TRUNCATE TABLE " + i
        sqlList.append(sqlStr)   
    deleteList = ['sticker_group'] 
    for tableName in deleteList:
        sqlList.append("delete from " + tableName)
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def clearAD(db):
    sqlList = []
    tableList = ['ad_banner']
    for i in tableList:
        sqlStr = "TRUNCATE TABLE " + i
        sqlList.append(sqlStr)   
    dbConnect.dbSetting(db, sqlList)

def clearAnnouncement(db):
    sqlList = []
    tableList = ['announcement_v2_identity_association', 'announcement_v2_user_level', 'announcement_v2_last_login_period', 'announcement_v2_register_time_period', 'quota_log']
    for i in tableList:
        sqlStr = "TRUNCATE TABLE " + i
        sqlList.append(sqlStr)   
    deleteList = ['announcement_v2'] 
    for tableName in deleteList:
        sqlList.append("delete from " + tableName)
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def initIdList(prefix, token, nonce, accountList, idList):
    header  = {}
    header['X-Auth-Token'] = token
    header['X-Auth-Nonce'] = nonce
    for i in accountList:
        idList.append(search_user(prefix, i, header))
    return 
    
def clearOrder(db):
    sqlList = []
    tableList = ['remain_points_history', 'purchase_order']
    for i in tableList:
        sqlList.append("TRUNCATE TABLE " + i)
    dbConnect.dbSetting(db, sqlList)

def clearChatBot(db):
    sqlList = []
    tableList = ['chatbot_switch', 'chatbot_target_user']
    for i in tableList:
        sqlList.append("TRUNCATE TABLE " + i)
    dbConnect.dbSetting(db, sqlList)

def clearNotiySetting(db):
    sqlList = []
    tableList = ['user_notification_settings', 'notification_v2_identity_association']
    deleteList = ['notification_v2']
    for i in tableList:
        sqlList.append("TRUNCATE TABLE " + i)
    dbConnect.dbSetting(db, sqlList)
    for tableName in deleteList:
        sqlList.append("delete from " + tableName)
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def clearLiveData(db):
    sqlList = []
    tableList = ['liveshow_gift_history', 'liveshow_guest', 'liveshow_streaming', 'live_banner', 'live_controller', 'live_banner_v2',
    'live_room_gift', 'zego_master', 'play_event_log', 'live_master_statistics', 'live_room_log', 'top_sort']
    deleteList = ['liveshow_team', 'liveshow', 'live_room']
    for i in tableList:
        sqlList.append("TRUNCATE TABLE " + i)
    dbConnect.dbSetting(db, sqlList)
    for tableName in deleteList:
        sqlList.append("delete from " + tableName)
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def clearIdentityData(dbInfo):
    sqlList = []
    result = []
    sqlStr = "select identity_id from identity_third_party union select identity_id from identity_profile"
    result = dbConnect.dbQuery(dbInfo, sqlStr)
    tableList = ['identity_email_register_history', 'identity_message', 'identity_email_bind_history', 'identity_third_party', 'identity_line', 'identity_profile', 'nickname_reset'] 
    for i in tableList:
        sqlStr = "TRUNCATE TABLE " + i
        sqlList.append(sqlStr)    
    sqlList.append("delete from user_settings where email = 'lisa@truelovelive.dev'")   
    dbConnect.dbSetting(dbInfo, sqlList)
    delList = ['identity_role', 'remain_points', 'user_settings', 'user_experience', 'announcement_v2_identity_association', 'identity']
    for k in delList:
        for i in range(len(result)):
            for j in range(len(result[i])):
                if j == 0:
                    if k == 'identity':
                        sqlStr = "delete from " + k + " where id in ('"
                    elif k == 'announcement_v2_identity_association':
                        sqlStr = "delete from " + k + " where receiver in ('"
                    else:
                        sqlStr = "delete from " + k + " where identity_id in ('"
                sqlStr += result[i][j] 
                if len(result[i]) - j == 1:
                    sqlStr += "')"
                else:
                    sqlStr += "', '"
            sqlList.append(sqlStr)
    sqlList.append('delete from message')
    sqlList.append("alter table " + tableList[0] + " auto_increment = 1") 
    dbConnect.dbSetting(dbInfo, sqlList)

def clearFansInfo(db):
    sqlList = []       
    truncateList = ['user_follows', 'fans', 'user_blocks', 'fans_history', 'photo_report', 'post_gift_history','photo_comment', 'photo_like', 'notification_v2_identity_association', 'zego_master']
    for i in truncateList:
        sqlList.append("TRUNCATE TABLE " + i)
    sqlList.append('delete from notification_v2')
    sqlList.append('delete from photo_post')
    dbConnect.dbSetting(db, sqlList)    

def clearProfile(db):
    sqlList = []
    sqlList.append('TRUNCATE TABLE live_master_name_card')
    sqlList.append('TRUNCATE TABLE profile_like')
    sqlList.append('Delete from live_master_profile')
    sqlList.append("alter table live_master_profile auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def clearIMInfo(db):
    sqlList = []
    truncateList = ['instant_message_point_history', 'instant_message_video', 'instant_message_image', 'instant_message_text', 'zego_master']
    deleteList = ['instant_message', 'dialog_member', 'dialog', 'quota_log', 'point_consumption_history']
    for i in truncateList:
        sqlList.append("TRUNCATE TABLE " + i)
    dbConnect.dbSetting(db, sqlList)
    for tableName in deleteList:
        sqlList.append("delete from " + tableName)
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)
    

def clearPhoto(db):
    sqlList = []
    truncateList = ['post_gift_history', 'photo_report', 'photo_comment', 'photo_like']
    deleteList = ['quota_log', 'photo_post']
    for i in truncateList:
        sqlList.append("TRUNCATE TABLE " + i)
    dbConnect.dbSetting(db, sqlList)
    for tableName in deleteList:
        sqlList.append('delete from ' + tableName)       
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)


def clearConsumption(db):
    sqlList = []
    truncateList = ['game_point_history', 'liveshow_gift_history', 'live_room_gift','instant_message_point_history', 'post_gift_history']
    deleteList = ['game_room', 'quota_log', 'point_consumption_history']
    for i in truncateList:
        sqlList.append("TRUNCATE TABLE " + i)
    dbConnect.dbSetting(db, sqlList)
    for tableName in deleteList:
        sqlList.append('delete from ' + tableName)       
        sqlList.append("alter table " + tableName + " auto_increment = 1")
    dbConnect.dbSetting(db, sqlList)

def apiFunction(prefix, head, apiName, way, body):
    resquestDic = {
        'post':requests.post,
        'put':requests.put,
        'patch':requests.patch, 
        'get':requests.get, 
        'delete':requests.delete
    }
    url = prefix + apiName  
    if body:
        head['Content-Type'] = 'application/json'
        res1 = resquestDic[way](url, headers=head, json=body)
    else: 
        if head.get('Content-Type'):
            del head['Content-Type']          
        res1 = resquestDic[way](url, headers=head)
    print(head)
    print('url = %s, method= %s'% (url, way))  
    print(body) if body else print('no body')
    pprint('status code = %d'%res1.status_code)
    pprint(json.loads(res1.text))
    return res1 