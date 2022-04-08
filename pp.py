import datetime


if __name__ == '__main__':
    test ={
            'sqlStr': "select %s, %s, %s from %s where sender_id = '%s' order by id desc limit 1", 
            'parameters': ('gift_type', 'point', 'count', 'point_consumption_history', 'upiweqr-jasdpi-11212'),
            'check':[
                {'fieldIndex': 0, 'value': 'backpack_gift'},
                {'fieldIndex': 1, 'value': 0},
                {'fieldIndex': 2, 'value': 1}
            ]
        }
    # for i in range(0, 6):
    #     keyName = 'vc_room:luckmoney_data:%s:3:%d-remainPoints'%(str(datetime.date.today()), (i+1))
    #     print(keyName)
    sqlStr = test['sqlStr']%test['parameters']
    print(sqlStr)