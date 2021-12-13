import datetime


if __name__ == '__main__':
    for i in range(0, 6):
        keyName = 'vc_room:luckmoney_data:%s:3:%d-remainPoints'%(str(datetime.date.today()), (i+1))
        print(keyName)