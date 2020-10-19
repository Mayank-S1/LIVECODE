from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
#from .models import codes
import urllib.parse
import urllib.request
import requests, json, os

COMPILE_URL = "https://api.hackerearth.com/v3/code/compile/"
RUN_URL = "https://api.hackerearth.com/v3/code/run/"
CLIENT_SECRET = '3185f9039c18e37035493d92bfddba7ca7e0d691'


permitted_languages = ["PYTHON", "CPP", "JAVA", "CLOJURE", "C", "HASKELL", "JAVA", "JAVASCRIPT", "OBJECTIVEC", "PERL", "PHP", "PYTHON", "R", "RUBY", "RUST", "SCALA"]

def code_editor_python(request):
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/python/python.min.js"
    return render(request, 'rooms/code_editor.html', {'mode': "text/x-python",'lg': "PYTHON3",'file': u });

def code_editor_cpp(request):
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/clike/clike.min.js"
    return render(request, 'rooms/code_editor.html',{'mode': "text/x-c++src",'lg': "CPP14",'file': u });

def code_editor_java(request):
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/clike/clike.min.js"
    return render(request, 'rooms/code_editor.html',{'mode': "text/x-java",'lg': "JAVA" ,'file' :u });

def code_editor_c(request):
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/clike/clike.min.js"
    return render(request, 'rooms/code_editor.html',{'mode': "text/x-csrc ", 'lg': "C", 'file': u });

def code_editor_javascript(request):
    u = "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.1/mode/javascript/javascript.min.js"
    return render(request, 'rooms/code_editor.html', {'mode': "text/javascript",'lg': "	JAVASCRIPT",'file': u });








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
          return render(request,'rooms/output.html', {'op': d['compile_status'] });

