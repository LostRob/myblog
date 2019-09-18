from django.conf.urls import url
from  Comment import views

app_name ='Comment'

urlpatterns = [
    url(r'^comment/blog-(?P<blog_id>\d+)/$',views.submit_comment,name='comment')
]