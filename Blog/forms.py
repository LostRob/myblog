# 引入表单类
from django import forms
# 引入文章模型
from . import models
from login.models import User
from captcha.fields import CaptchaField

# 写文章的表单类
class ArticlePostForm(forms.Form):
    title = forms.CharField(label="标题", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    excerpt = forms.CharField(label="摘要", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label="内容", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label='类型',queryset=models.Category.objects)
    tags = forms.ModelMultipleChoiceField(label='标签',queryset=models.Tag.objects)
    author = forms.ModelChoiceField(label='作者',queryset=User.objects)
    views = forms.FloatField(label='浏览量')
    created_time = forms.DateTimeField(label='创建时间')
    modified_time = forms.DateTimeField(label='修改时间')



