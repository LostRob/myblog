from django.shortcuts import render, redirect
from Comment.models import Comment
from Blog.models import Blog
from django.urls import reverse
# from .tasks import async_send_mail

def submit_comment(request, blog_id):
    """
    处理提交的评论
    :param request:
    :return:
    """
    blog = request.POST
    comment = Comment()
    # 评论
    comment.name = blog.get("comment-name",'Alien')
    comment.email = blog.get('comment-email')
    # comment.website = blog.get('website')
    comment.text = blog.get('comment')
    comment.blog = Blog.objects.get(id=blog_id)
    # 回复
    comment.reply_to = blog.get('reply_to', 0)
    comment.reply_email = blog.get('reply_email', 'mail@chuxiaoyi.cn')
    comment.root_to = blog.get('root_to', 0)
    comment.reply_name = blog.get('reply_name', '外星人')
    comment.save()

    # async_send_mail.delay(comment.reply_email, comment.text, pk)

    return redirect(reverse('Blog:detail', kwargs={"blog_id": blog_id}))

