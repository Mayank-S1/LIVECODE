
from django.conf.urls import include, url
from . import views

urlpatterns = [
  # ex: /
    url(r'^$', views.code_editor_python, name='python'),
    url(r'^java/$', views.code_editor_java, name='java'),
    url(r'^cpp$', views.code_editor_cpp, name='c++'),



   url(r'^compile/$', views.compileCode, name='compile'),
   # ex: /run/
   url(r'^run/$', views.runCode, name='run'),

  # ex: /code=ajSkHb/

]
