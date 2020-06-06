import requests
from pprint import pprint #pprint안의 pprint 함수를 import한다
def pmi(params):
    url = f'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address={params}'
    response = requests.get(url).json()
    remain = ['plenty', 'some', 'few', 'empty', 'break']
    mask_info = {}
    for data in response['stores'][:10]:
        if(data['remain_stat'] == remain[0]):
            mask_info[data['name']] = '100개 이상'
        elif data['remain_stat'] == remain[1]:
            mask_info[data['name']] = '30개 이상'
        elif data['remain_stat'] == remain[2]:
            mask_info[data['name']] = '2개 이상'
        elif data['remain_stat'] == remain[3]:
            mask_info[data['name']] = '1개 이하'
        else : 
            mask_info[data['name']] = '판매 중지'
    return mask_info
    
#input : 사용자가 데이터를 입력할 때 쓴다
params = input('주소를 시 구 동으로 입력해 주세요 : ')
mask = pmi(params)
# pprint(mask)

for key, value in mask.items():
    # print(key, '판매처에 마스크가', value, ' 있습니다.')
    print(f'{key} 판매처에 마스크가 {value} 있습니다')
