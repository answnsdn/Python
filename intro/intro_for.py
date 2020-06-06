# 2. for
number =  list(range(10))
print(number)

for num in range(10):
    print(num)

# 2-1. list for
number = ['삼성','선릉','영등포','역삼']
for num in number:
    print(num)

# 2-2. idx로 접근하고 싶어요.
for i in range(len(number)):
    print(i)
    print(number[i])

# 2-3. enumerate
for idx, i in enumerate(number):
    print(idx, i)

# dictionary
mask = {
    '삼성' : 100,
    '역삼' : '50개',
    '선릉' : True
}
for i in mask:
    print(i)
    print(mask[i])
print("*"*30)
#동작은 위 코드와 동일하나, dictionary를 표현하기 위한 방법 - keys()를 붙인다.
for i in mask.keys():
    print(i) 
print("*************************************")
for i in mask.values():
    print(i)
print("*************************************")
for key, val in mask.items():
    print(key)
    print(val)
    print(mask[key])
print("*************************************")
for idx, i in enumerate(mask,3):
    #enumerate : 내가 원하는 인덱스 번호로 출력이 가능하다. 3부터 출력
    print(idx,i)