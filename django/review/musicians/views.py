from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

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
    context={
        'musician': musician
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
