from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
#from .models import codes
import urllib.parse
import urllib.request
import requests, json, os

COMPILE_URL = "https://api.hackerearth.com/v3/code/compile/"
RUN_URL = "https://api.hackerearth.com/v3/code/run/"
CLIENT_SECRET = '3185f9039c18e37035493d92bfddba7ca7e0d691'


permitted_languages = ["C", "CPP", "CSHARP", "CLOJURE", "CSS", "HASKELL", "JAVA", "JAVASCRIPT", "OBJECTIVEC", "PERL", "PHP", "PYTHON", "R", "RUBY", "RUST", "SCALA"]

def code_editor(request):
    return render(request,'rooms/code_editor-python.html');

def code_editor2(request):
    return render(request,'rooms/code_editor-java.html');

def code_editor3(request):
    return render(request,'rooms/code_editor-c++.html');








def runCode(request):
     source = request.GET['fulltext']
     lang = request.GET['lang']
     data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source,
    'lang': lang,
    'time_limit': 5,
    'memory_limit': 262144,
     }
     r = requests.post(RUN_URL, data=data)
     d = r.json()
     return render(request,'rooms/output.html',{'op':d['run_status']['output']});

def compileCode(request):
          source = request.GET['fulltext']
          lang = request.GET['lang']
          data = {
              'client_secret': CLIENT_SECRET,
              'async': 0,
              'source': source,
              'lang': lang,
              'time_limit': 5,
              'memory_limit': 262144,
          }
          r = requests.post(COMPILE_URL, data=data)
          d = r.json()
          return render(request,'rooms/output.html',{'op':d['compile_status']});

