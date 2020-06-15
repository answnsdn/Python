from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'articles/index.html')

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    context={
        'title':title,
        'content':content
    }
    return render(request,'articles/create.html',context)

def introduce(request):
    return render(request, 'articles/introduce.html')
