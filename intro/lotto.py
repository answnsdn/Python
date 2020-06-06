import random
#print(dir(random))
#dir : 함수가 가지고 있는 기능을 나열해줌

#random 함수 안의 choice를 써보기
number = random.choice(range(10))
print(number)

#list에서 무작위로 뽑기
arr = ['100', '50', '30', '20']
pick = random.choice(arr)
print(pick)

#dict에도 써보기
mask = {
    '100' : '삼성',
    '50' : '역삼',
    '30' : '선릉',
    '20' : '영등포'
}
print(mask[pick])

# sample
lotto = random.sample(range(1, 46), 6)
print(sorted(lotto)) #sorted : 정렬
