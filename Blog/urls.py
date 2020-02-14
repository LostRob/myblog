from django.conf.urls import url
from  . import views
from django.contrib import admin
from django.urls import path,include,re_path
from login import views as loginviews

app_name = 'Blog'   # 这里是为了url反向解析用

urlpatterns = [
    url(r'^$', views.index2, name="index2"),
    url(r'index', views.index2, name="index2"),
    # url(r'index2.html', views.index2, name="index2"),
    url(r'examples.html', views.examples),
    url(r'one-column.html', views.onecolumn),
    url(r'text.html', views.text),
    url(r'three-column.html', views.threecolumn),
    url(r'^detail/detail-(?P<blog_id>\d+)/$',views.detail,name='detail'),
    url(r'^blogging',views.blogging,name='blogging'),
    # 分类
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tag, name='tag'),
    url(r'admin',admin.site.urls),
    url(r'^login/', loginviews.login),
    url(r'^register/', loginviews.register),
    url(r'^logout/', loginviews.logout),
    url(r'^captcha', include('captcha.urls'))
]