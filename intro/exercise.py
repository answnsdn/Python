import random
# 1. 5번 반복해서 로또번호(6개) 추첨하기
#한꺼번에 하는 방법
lotto = [random.sample(range(1,46),6) for i in range(5)]
print(lotto)
#기본 방법
for i in range(5):
    print(random.sample(range(1,46),6))
# 2. 음식점 이름, 전화번호를 가지는 dictionary 만들기
food = {
    '연가' : '02-186-9845',
    '본가' : '02-485-8457',
    '김가' : '02-734-7674',
    '장가' : '02-548-9998'
}
print(food)
# 2-1. 무작위 음식점 하나 뽑아서
    #food.keys()만 뽑으면 안되기 때문에 list로 형변환을 한다.
    pick = random.choice(list(food.keys()))
    print(pick)
# 2-2. 가게이름이랑 전화번호 출력
    #기본 형태
    print('가게이름 : '+pick)
    print('전화번호 : '+food[pick])
    #파이썬스럽게
    print(f'가게이름:{pick}, 전화번호:{food[pick]}')

