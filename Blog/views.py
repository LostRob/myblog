from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from Blog.models import Blog,Tag,Category
from Comment.models import Comment
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import get_object_or_404
import markdown


def index2(request):
    """
    主页
    :param request:
    :return:
    """
    blog = Blog.objects.all()

    order = request.GET.get('order','')

    # 排序方式有一些混乱

    # 按照浏览量最高
    if order == 'views':
        blog = blog.order_by('-views')
        order = 'views'
    # 按照修改时间最新
    elif order == 'modified_time':
        blog = blog.order_by('-modified_time')
        order = 'modified_time'
    # 按照随机排序
    else:
        blog = blog.order_by('?')
        order = 'normal'

    limit = 5
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

def blogging(request):
    return render(request=request, template_name='blogging.html')

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


