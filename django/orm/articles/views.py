from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    #전체 데이터 가져오기
    articles = Article.objects.all()[::-1]
    #데이터 템플릿에게 넘겨주기
    context = {
        'articles':articles
    }
    #템플릿에서 반복문으로 각각의 게시글의 pk, title 보여주기
    return render(request,'articles/index.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    # GET 방식 사용하기
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # context={
    #     'title':title,
    #     'content':content
    # }
    # return render(request,'articles/create.html',context)

    #POST 방식 사용하기
    title = request.POST.get('title')
    content = request.POST.get('content')
    #데이터 생성을 위한 ORM 활용
    # 1. 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. 두번째 방법
    # article = Article(title=title, content=content)
    # article.save()

    # 3. 세번째 방법
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')

def introduce(request):
    return render(request, 'articles/introduce.html')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html',context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context={
        'article':article,
    }
    return render(request,'articles/edit.html',context)


