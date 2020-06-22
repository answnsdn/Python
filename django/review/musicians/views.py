from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicianForm, AlbumForm
from django.views.decorators.http import require_POST
from .models import Musician, Album

# Create your views here.
def index(request):
    musicians = Musician.objects.all()
    context = {
        'musicians': musicians
    }
    return render(request, 'musicians/index.html',context)

def create(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save()
            return redirect('musicians:index')
    else:
        # MusicianForm 불러오기
        # form은 MusicianForm 인스턴스
        # MusicianForm이 가진 정보를 가짐
        # template에서 보여줄 tag들
        form = MusicianForm()
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'musicians/create.html',context)

def detail(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    album_form = AlbumForm()
    albums = musician.album_set.all()
    context={
        'musician': musician,
        'album_form': album_form,
        'albums': albums
    }
    return render(request, 'musicians/detail.html',context)

def update(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musicians:detail', musician.pk)
    else:
        form = MusicianForm(instance=musician)
    context = {
        'form': form
    }
    return render(request, 'musicians/create.html', context)

def delete(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    if request.method == "POST":
        musician.delete()
        return redirect('musicians:index')
    return redirect('musicians:detail',musician.pk)

@require_POST
def album_create(request, musician_pk):
    musician = get_object_or_404(Musician,pk=musician_pk)
    album_form = AlbumForm(request.POST)
    if album_form.is_valid():
        album = album_form.save(commit=False)
        album.musician = musician
        album.save()
        return redirect('musicians:detail',musician.pk)
    else:
        context={
            'album_form': album_form,
            'musician': musician
        }
        return redirect('musicians:detail',context)
    
