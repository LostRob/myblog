from django import template
from ..models import Category,Tag
from Comment.models import Comment
register = template.Library()

@register.simple_tag
def get_categories():
    """
    目录分类
    :return:
    """
    return Category.objects.all()

@register.simple_tag
def get_tags():
    """
    目录标签
    :return:
    """
    return Tag.objects.all()



@register.simple_tag()
def get_latest_comment():
    """
    获取最新评论
    :return:
    """
    comment_list = Comment.objects.all()[:5].only('blog', 'text')   # 只获取特定字段
    return comment_list
