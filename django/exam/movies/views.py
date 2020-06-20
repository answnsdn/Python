from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        # 1. 폼을 받아온다
        form = MovieForm(request.POST)
        # 2. 검증한다
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/form.html', context)


def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)
    context={
        'form': form
    }
    return render(request, 'movies/form.html', context)

def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()    
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk)