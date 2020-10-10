from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'movie_short'

urlpatterns = [
    path('', views.movie_short),
    path('search/', views.search, name='search'),
]