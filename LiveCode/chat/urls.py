from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('create_room/',views.create_room ,name='create_room'),
    path('login/',views.index,name='login'),
    path('python/room/', views.room, name='room'),
    path('compile/', views.compileCode, name='compile'),
    # ex: /run/
    path('run/', views.runCode, name='run'),
    path('register/',views.register, name='register'),
    path('python/room/',views.python,name="python"),
    path('cpp/room/',views.cpp,name="cpp"),
    path('java/room/',views.java,name="java"),
    path('check/',views.check,name='check'),
]