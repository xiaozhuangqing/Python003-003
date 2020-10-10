from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from .models import MovieShort
from django.contrib import messages

def movie_short(request):
    shorts = MovieShort.objects.filter(starts__gt =3)
    return render(request, 'movie_short.html', locals())

def search(request):
    q = request.GET.get('q')
    error_msg = '请输入关键词'

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'search_error.html', {'error_msg': error_msg})

    shorts = MovieShort.objects.filter(short__contains=q)
    return render(request, 'search_results.html', {'error_msg': error_msg, 'shorts':shorts})