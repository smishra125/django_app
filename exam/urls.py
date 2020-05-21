from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('test', views.showTest),
    url('result', views.showResult),
    url('about', views.about),
    url('message', views.message)

]