from django.shortcuts import render
# Create your views here.

def code_editor(request):
    return render(request, 'rooms/code_editor.html');



