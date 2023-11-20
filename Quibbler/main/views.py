from django.shortcuts import render, HttpResponse
from .models import News, User
# Create your views here.


def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def contacts(request):
    return render(request,'main/contacts.html')

def list_of_news(request):
    return render(request,'main/list_of_news.html')

def news1(request):
    return render(request,'main/news1.html')

def news2(request):
    return render(request,'main/news2.html')
def news3(request):
    return render(request,'main/news3.html')
def registration(request):
    if request.method == 'POST':
        print('Received POST-request')
        print(request.POST)
        usrname = request.POST.get('usrname')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        user = User(usrname, email, telephone, password)
        print('Зарегистрирован новый пользователь: ', user.usrname)
    else:
        print('Received GET-request')
    return render(request,'main/registration.html')

def user_account(request):
    if request.method == 'POST':
        print('Received POST-request')
        print(request.POST)
        newshead = request.POST.get('newshead')
        newssummary = request.POST.get('newssummary')
        newstext = request.POST.get('newstext')
        news1 = News(newshead, newssummary, newstext)
        print('Создана новость: ', news1.newshead)
    else:
        print('Received GET-request')
    return render(request,'main/user_account.html')

def sidebar(request):
    return render(request,'main/sidebar.html')

def policy(request):
    return render(request,'main/policy.html')

def admin(request):
    return render(request,'main/admin.html')