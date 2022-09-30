from django.shortcuts import render
from day3pjt.settings import BASE_DIR

# Create your views here.

guestbook=[]

def index(request):
    return render(request, 'articles/index.html',{'guestbook':guestbook})

def create(request):
    content=request.GET.get('content')
    guestbook.append(content)
    return render(request, 'articles/create.html',{'content':content})