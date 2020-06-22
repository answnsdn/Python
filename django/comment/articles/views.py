from django.shortcuts import render, redirect
#DVDH
#django가 주는 views에서 쓸 decorators http를 위한
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
        return redirect('articles:detail',article.pk)
    else:


    return render(request,'articles/form.html',context)


@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # comment.article_id = article.pk
        comment.save()
        return redirect('articles:detail',article.pk)
    else:
        context = {
            'comment_form': comment_form
            'article': article
        }
    return redirect('articles:detail', context)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)



