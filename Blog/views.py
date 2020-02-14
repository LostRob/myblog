# 引入redirect重定向模块
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from Blog.models import Blog,Tag,Category
from Comment.models import Comment
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import get_object_or_404
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
from login.models import User
import markdown


def index2(request):
    """
    主页
    :param request:
    :return:
    """
    blog = Blog.objects.all()
    # orderalg = blog.order_by()
    order = request.GET.get('order','')

    # 排序方式有一些混乱

    # 按照浏览量最高
    if order == 'views':
        blog = blog.order_by('-views')
        order = 'views'
    # 按照修改时间最新
    elif order == 'created_time':
        blog = blog.order_by('-created_time')
        order = 'created_time'
    # 按照算法排序
    else:
        # orderalg
        blog = blog.order_by('?')
        order = 'normal'

    limit = 6
    paginator = Paginator(blog, limit)
    page = request.GET.get('page')
    '''
    result = paginator.page(page)
    '''
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    context = {
        "blog_list": result,
        "page": page,
        "order": order
    }
    return render(request=request, template_name='index2.html', context=context)


def examples(request):
    return render(request=request, template_name='examples.html')


def onecolumn(request):
    return render(request=request, template_name="one-column.html")


def text(request):
    return render(request=request, template_name='text.html')


def threecolumn(request):
    return render(request=request, template_name='three-column.html')

# def blogging(request):
#     return render(request=request, template_name='blogging.html')

# 写文章的视图
def blogging(request):
     # 判断用户是否登录
    if not request.session.get('is_login', None):
        return redirect('/index')
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            title = article_post_form.cleaned_data['title']
            excerpt = article_post_form.cleaned_data['excerpt']
            body = article_post_form.cleaned_data['body']
            # tag = article_post_form.cleaned_data['tag']
            # category = article_post_form.cleaned_data['category']
            new_blog = Blog.objects.create(title=title,excerpt=excerpt,body=body)
            # 保存数据，但暂时不提交到数据库中
            # new_blog = article_post_form.save(commit=False)
            # new_blog.title = title
            # new_blog.excerpt = excerpt
            # new_blog.body = body
            # new_blog.tag = tag
            # new_blog.category = category
            # 指定数据库中 id=1 的用户为作者
            # new_blog.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            # new_blog.save()
            # 完成后返回到文章列表
            # return redirect("Blog:detail")
            return render(request, 'blogging.html', locals())
        # 如果数据不合法，返回错误信息
        else:
            message = "两次输入的密码不同！"
            return render(request, 'blogging.html',locals())
    # 如果用户请求获取数据
    # 创建表单类实例
    article_post_form = ArticlePostForm()
    # 返回模板
    message = "两次输入的密码相同！"
    return render(request, 'blogging.html', locals())


# 分类视图
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    blog_list = Blog.objects.filter(category=cate).order_by('-created_time')
    return render(request,'catview.html',context={'blog_list':blog_list})

def tag(request,pk):
    tag = get_object_or_404(Tag,pk=pk)
    blog_list = Blog.objects.filter(tags=tag).order_by('-created_time')
    return render(request,'tagsview.html',context={'blog_list':blog_list})



def detail(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.add_views()

    # markdown 生成目录 markdown 高亮
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    blog.body = md.convert(blog.body)
    '''
    context = {
        'blog': blog,
        'toc': md.toc,
        'comment_list': comment_list
    }
    '''
    # context = {
    #     'blog': blog
    # }
    # limit = 1
    # paginator = Paginator(blog, limit)
    # page = request.GET.get('page', 1)
    #
    # result = paginator.page(page)
    # 评论详情
    comment_list = Comment.objects.filter(blog_id=blog_id).filter(root_to=0)
    for comment in comment_list:
        comment.text = markdown.markdown(
            comment.text,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.fenced_code',
            ]
        )
        comment.replies = Comment.objects.filter(blog_id=blog_id).filter(root_to=comment.id)

    context = {
        'blog':blog,
        'toc': md.toc,
        'comment_list':comment_list
    }

    return render(request=request, template_name='detail.html',context=context)


