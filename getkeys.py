from pprint import pprint
from typing import Dict, List

# def getKeys(dd):
#     keyList = []
#     calltimes = 0
#     def getDicKeys(dd1, keyList, calltimes):
#         calltimes += 1
#         print('call getDickeys %d times'%calltimes)
#         for keys1, values1 in dd1.items():
#             keyList.append(keys1)
#             print(keys1, str(values1))
#             if type(values1) == dict:
#                 getDicKeys(values1, keyList, calltimes)
#             elif all([type(values1) == list, values1]):
#                 if type(values1[0]) == dict:getDicKeys(values1[0], keyList, calltimes)
#             else:
#                 continue
        
#     for keys, values in dd.items():
#         keyList.append(keys)
#         print(keys, str(values))
#         # print('values type is: %s'%str(type(values)))
#         if type(values) == dict:
#             getDicKeys(values, keyList, calltimes)
#         elif all([type(values) == list, values]):
#             if type(values[0]) == dict:getDicKeys(values[0], keyList, calltimes)
#         else:
#             continue
            
#     return keyList

def getDicKeys(dd, keyList):  
    keyList.append(dd.keys())  
    for keys, values in dd.items():
        keyList.append(keys)
        if type(values) == dict:
            getDicKeys(values, keyList)
        elif all([type(values) == list, values]):
            if type(values[0]) == dict:getDicKeys(values[0], keyList)
        else:
            continue          
    return 

if __name__ == '__main__':
    keyList = []
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
                            'userInfo':[
                                {'nickname': '123', 'age': 5, 'address': '32453'},
                                {'nickname': '456', 'age': 13, 'address': '12313'}
                            ]
    }}}
    getDicKeys(dd, keyList)
    pprint(type(keyList[4]))