from django.conf.urls import url
from login import views
from django.urls import path
from django.contrib import admin

app_name = 'login'   # 这里是为了url反向解析用



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index', views.index2, name="index2"),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
]

