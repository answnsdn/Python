from django.shortcuts import render

# Create your views here.

def loop(request):
    nums = []
    for data in range(10):
        nums.append(data)
    context={
        'nums': nums
    }
    return render(request,'loop.html',context)

def throw(request):
    return render(request,'throw.html')

def catch(request):
    # request.GET은 dict 형태
    # 대괄호 접근은 키 값이 없을 때 오류 발생, 서버 내려감
    print(request.GET['message'])
    # .get으로 접근하면 키 값이 없을 때 none으로 접근 -> 활용도 높음
    data = request.GET.get('message')
    
    context = {
        'data':data
    }
    return render(request,'catch.html',context)