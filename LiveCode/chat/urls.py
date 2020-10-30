from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('python/room/', views.room, name='room'),
    path('compile/', views.compileCode, name='compile'),
    # ex: /run/
    path('run/', views.runCode, name='run'),

    path('python/room/',views.python,name="python"),
path('cpp/room/',views.cpp,name="cpp"),
path('java/room/',views.java,name="java"),

]