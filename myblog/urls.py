"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from login import views as loginviews
from Blog import views as Blogviews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'',include('Post.urls')),
    path(r'',include('Blog.urls',namespace='Blog')),
    path(r'',include('Comment.urls',namespace='Comment')),
    # path(r'',include('login.urls',namespace='login')),
    re_path(r'^search/', include('haystack.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/', loginviews.login),
    url(r'^register/', loginviews.register),
    url(r'^logout/', loginviews.logout),
    url(r'^captcha', include('captcha.urls')),
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)




