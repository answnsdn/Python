#Spring Framework의 Controller의 역할
from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
#request는 requests와 다름
def index(request):
    return render(request,'index.html')

def hello(request):
    menu = ['닭갈비','탕수육','초밥']
    pick = random.choice(menu)
    #render 함수 안에 넘겨줄 html 파일과 데이터(dict 형태)로 넘겨준다.
    return render(request,'hello.html',{'pick':pick})

def name(request):
    my_name = '문준우'
    return render(request,'name.html',{'my_name':my_name})

def introduce(request):
    # my_info=['문준우','26','남']
    # return render(request,'info.html',{'name':my_info[0],'old':my_info[1],'sex':my_info[2]})
    name='문준우'
    age=26
    sex='남'
    hobby_list=['프로그래밍','식사','운동']
    hobby=random.choice(hobby_list)
    career='노답'
    future='노답'
    life='노답'
    context={
        'name':name,
        'age':age,
        'sex':sex,
        'hobby':hobby,
        'career':career,
        'future':future,
        'life':life
    }
    return render(request,'info.html',context)

def raname(request):
    name_list=['이정윤','황제윤','박누리','곽혜란','김현정']
    name=random.choice(name_list)
    context={
        'name':name
    }
    return render(request,'raname.html',context)

def yourname(request, name):
    context={
        'name':name
    }
    return render(request,'yourname.html',context)

def exam200610(request, name, age):
    context={
        'name':name,
        'age':age
    }
    return render(request, 'exam200610.html',context)

def multiple(request, num1, num2):
    result = num1*num2
    context={
        'num1':num1,
        'num2':num2,
        'result':result
    }
    return render(request, 'multiple.html',context)

def googoo(request, big, small):
    result=[]
    #big과 small을 비교해서 실제 큰값과 작은값을 넣어준다.
    if big<small:
        big, small = small, big
    #반복문을 사용하여 큰 값의 배수를 작은값만큼 반복한다.
    for data in range(1, small+1):
        result.append(big*data)
    context={
        'result':result
    }
    return render(request,'googoo.html',context)

def dtl(request):
    my_list=['간짜장','해물짬뽕','꿔바로우','콩국수']
    empty_list=[]
    my_string = 'Life is short, You need enjoy'
    today = datetime.now()
    context={
        'my_list':my_list,
        'empty_list':empty_list,
        'my_string':my_string,
        'today':today
    }
    return render(request,'dtl.html',context)

def forif(request):
    my_list = [100, 50, 30 ,20 ,10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list':my_list,
        'my_string':my_string,
        'data_a':data_a,
        'data_b':data_b
    } 
    return render(request,'forif.html',context)