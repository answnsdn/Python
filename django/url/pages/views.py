from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request):
    return render(request,'pages/index.html')


#1. 사용자가 url 경로에 이름을 입력하면
#2. 그 이름과 무작위 음식 하나 보여주는 페이지 작성
#2-1. random.choice(menu)
#3. url -> view-> template
def lunch(request,name):
    menu = ['zzazang', 'jjambbong', 'sushi']
    pick = random.choice(menu)
    context = {
        'name':name,
        'pick':pick
    }
    return render(request,'pages/lunch.html',context)

def throw(request):
    return render(request,'pages/throw.html')

def catch(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context ={
        'name':name,
        'age': age
    }
    return render(request,'pages/catch.html',context)

# 1. 사용자가 숫자 입력
# 2. 입력받은 횟수 만큼 반복해서
# 3. 리스트에 로또 번호 담는다
# 3-1. random.sample(range(1,46),6) 를 리스트에 append
# 4. 사용자가 입력한 숫자와 로또번호가 담긴 리스트를 출력
# 5. ul 태그를 사용하여 각 번호들을 한줄 씩 출력 

def lotto(request):
    return render(request,'pages/lotto.html')

def getlotto(request):
    count = request.GET.get('count')
    lottolist = []
    for i in range(0,int(count)):
        lottolist.append(random.sample(range(1,46),6))
        lottos = lottolist.sort()
    context = {
        'count' : count,
        'lottos':lottos
        
    }    
    return render(request,'pages/getlotto.html',context)

def artii(request):
    return render(request,'pages/artii.html')

def result(request):
    message = request.GET.get('message')
    result = requests.get(f'http://artii.herokuapp.com/make?text={message}').text
    context = {
        'result' : result
    }
    return render(request,'pages/result.html',context)

