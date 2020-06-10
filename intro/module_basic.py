import random
pick = random.choice([1,2,3,4,5])
print(pick)

#help(random.sample) - help를 사용해 정의를 알 수 있다. 빠져나오기 : Q

pick = random.sample(range(10), 3)
print(pick)