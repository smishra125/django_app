from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('about', views.about),
    url('contact', views.showContact),
    url('^$', views.greeting),
    url('employee', views.employee_info_view),

]