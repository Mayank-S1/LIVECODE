from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from .models import codes

import urllib.parse
import urllib.request
import requests, json, os
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatingUserForm
from .models import User

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from django.contrib.auth.hashers import  check_password


COMPILE_URL = "https://api.hackerearth.com/v3/code/compile/"
RUN_URL = "https://api.hackerearth.com/v3/code/run/"
CLIENT_SECRET = '3185f9039c18e37035493d92bfddba7ca7e0d691'


def homepage(request):
    return render(request,'chat/homepage.html',{});

def index(request):
    return render(request, 'chat/index.html')


def room(request):
    room_name = request.GET['room_name']
    user = request.GET['User']
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/python/python.min.js"

    return render(request, 'chat/room.html', {'room_name': room_name,'user':user ,'mode': "text/x-python",'lg': "PYTHON3",'file': u});

def python(request):
    room_name = request.GET['room_name']
    user = request.GET['User']
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/python/python.min.js"
    return render(request, 'chat/room.html',{'room_name': room_name, 'user': user, 'mode': "text/x-python", 'lg': "PYTHON3", 'file': u});


def cpp(request):
    room_name = request.GET['room_name']
    user = request.GET['User']
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/clike/clike.min.js"
    return render(request, 'chat/room.html',{'room_name': room_name, 'user': user,'mode': "text/x-c++src",'lg': "CPP14",'file': u });



def java(request):
    room_name = request.GET['room_name']
    user = request.GET['User']
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/clike/clike.min.js"
    return render(request, 'chat/room.html',{'room_name': room_name, 'user': user,'mode': "text/x-java",'lg': "JAVA" ,'file' :u});

def runCode(request):
    source = request.POST['source']
    lang = request.POST['lang']
    data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': lang,
    }
    r = requests.post(RUN_URL, data=data)
    return JsonResponse(r.json(), safe=False)

def compileCode(request):
      source = request.POST['source']
      lang = request.POST['lang']
      compile_data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': lang,
      }
      r = requests.post(COMPILE_URL, data=compile_data)
      return JsonResponse(r.json(), safe=False)

def create_room(request):
    return render(request, 'chat/create_room.html')



def register(request):
    postData = request.POST
    room_name = postData.get('room-name')
    password = postData.get('Password')
    user = User(room_name=room_name, password=password)
    user.password = make_password(user.password)
    user.register()
    link = 'http://127.0.0.1:8000/login'
    return HttpResponse('LINK :'+' '+link)


def check(request):
    room_name = request.GET['room_name']
    password = request.GET['password']
    user_type = request.GET['user_type']
    user = User.get_user_by_roomname(room_name)

    error_message = None
    if user:
        flag = check_password(password,user.password)
        if flag:
            return render(request,'chat/room.html',{'room_name':room_name,'user': user_type});
        else:
            error_message= 'Roomname or Password is incorrect!!'
    else:
        error_message = 'Roomname or Password is incorrect!!'
    return render(request,'chat/index.html',{'error':error_message});





