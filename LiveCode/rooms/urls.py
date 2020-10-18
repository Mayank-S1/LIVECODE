
from django.conf.urls import include, url
from . import views

urlpatterns = [
  # ex: /
  url(r'^$', views.code_editor, name='python'),
 url(r'^/$', views.code_editor2, name='java'),
 url(r'^/$', views.code_editor3, name='c++14'),
  # ex: /compile/
 url(r'^compile/$', views.compileCode, name='compile'),
  # ex: /run/
 url(r'^run/$', views.runCode, name='run'),

  # ex: /code=ajSkHb/

]
