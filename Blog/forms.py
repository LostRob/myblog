# 引入表单类
from django import forms
# 引入文章模型
from .models import Blog
from captcha.fields import CaptchaField

# 写文章的表单类
class ArticlePostForm(forms.Form):
    title = forms.CharField(label="标题", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    excerpt = forms.CharField(label="摘要", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label="内容", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # tag = forms.ChoiceField(label='标签', choices=Blog.tags)
    # category = forms.ChoiceField(label='类型', choices=Blog.category)



