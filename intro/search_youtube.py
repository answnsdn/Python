import requests
from pprint import pprint
key = 'AIzaSyBRqTQM8YsLRrtYqjPxoMHd93LGgucDBWs'

#string interpolation
search = input("검색어를 입력해 주세요 :")
q = f'q={search}'
my_type = 'type=video'
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}'
#print(url)

response = requests.get(url)
datas = response.json() 
#pprint(datas)

#채널명, 영상 제목
for data in datas['items']:
    print(data['snippet']['title'], end='')#end를 사용하여 print 두 개를 엮을 수 있다.
    print(data['snippet']['channelTitle'])
