from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'sidebar/about', views.about, name='about'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'contacts/', views.contacts, name='contacts'),
    re_path(r'list_of_news/', views.list_of_news, name='list_of_news'),
    re_path(r'news1/', views.news1, name='news1'),
    re_path(r'news2/', views.news2, name='news2'),
    re_path(r'news3/', views.news3, name='news3'),
    re_path(r'registration/', views.registration, name='registration'),
    re_path(r'user_account/', views.user_account, name='user_account'),
    re_path(r'sidebar/', views.sidebar, name='sidebar'),
    re_path(r'policy/', views.policy, name='policy'),
    re_path(r'admin/', views.admin, name='admin'),
]