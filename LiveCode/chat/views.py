from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from .models import codes
import urllib.parse
import urllib.request
import requests, json, os

COMPILE_URL = "https://api.hackerearth.com/v3/code/compile/"
RUN_URL = "https://api.hackerearth.com/v3/code/run/"
CLIENT_SECRET = '3185f9039c18e37035493d92bfddba7ca7e0d691'

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


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

