from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
]