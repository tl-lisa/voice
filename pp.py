import random


if __name__ == '__main__':
    dd =  {'event': 'room_in',
                 'payload': {'data': {'fromUser': {'id': '9af1d7d9-14b0-4853-8793-9791b1e19d39',
                                                   'name': 'master0010',
                                                   'roles': ['ROLE_MASTER'],
                                                   'userLevel': {'levelId': 'bronze',
                                                                 'levelNum': '1'}},
                                      'joinTime': 1616490398360,
                                      'room': {'description': 'master0010開播，歡迎入群',
                                               'events': [],
                                               'hot': 1530,
                                               'id': 33,
                                               'liveRanking': 0,
                                               'liveRankingPoints': 0,
                                               'streamId': 33,
                                               'title': 'master0010開播囉',
                                               'totalCount': 0,
                                               'totalGiftPoints': 0,
                                               'tracked': False,
                                               'userGiftPoints': 0},
                                    'targetUser': {'id': 'aaaaaaaab-14b0-4853-8793-9791b1e19d39',
                                                   'name': 'track0010',
                                                   'roles': ['ROLE_USER'],
                                                   'userLevel': {'levelId': 'bronze',
                                                                 'levelNum': '32'}},
                 }}}

    kk = dd['payload']['data']
    findKey = ['targetUser', 'userLevel', 'levelNum1']
    itmeName = findKey.pop(0)
    for key, value in kk.items():
        if key == itmeName:
            print('get key(', itmeName, ')')
            yy = kk[itmeName]     
            itmeName = findKey.pop(0)
            k = 0
            isContinue = True
            while isContinue:
                print ('k=', k)
                print(yy)
                print(itmeName)
                for k1, v1 in yy.items():
                    if all([k1 == itmeName, len(findKey) == 0]):
                        print(itmeName, ' = ', v1)
                        isContinue = False
                        break
                    elif all([k1 == itmeName, len(findKey) > 0]):
                        print('find key and need next')
                        yy = yy[itmeName]     
                        itmeName = findKey.pop(0)
                        break
                    else:
                        isContinue = False
                        isNotFind = True
                k += 1
            break