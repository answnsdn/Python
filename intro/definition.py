def hello():
    return "Hello, World!"

def add(num, number):
    return num + number

nums = add(10,3)

def ran(num,number=10):
    return num + number
#number의 기본값이 지정되어 있기 때문에 nums가 호출될 수 있다.
nums = ran(3)
print(nums) 

def m_num(a,b):
    return
a=3
b=4
minus = m_num(b,a)
print(minus)
