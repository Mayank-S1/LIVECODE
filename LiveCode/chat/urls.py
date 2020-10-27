from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('compile/', views.compileCode, name='compile'),
    # ex: /run/
    path('run/', views.runCode, name='run'),
]