# views.py
from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def home(request):
    news = News.objects.all()
    return render(request, 'base.html', {'home': home})

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})


def news_update(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_form.html', {'form': form})

def news_delete(request, pk):
    News.objects.get(pk=pk).delete()
    return redirect('news_list')
