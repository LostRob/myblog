from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def index(request):
    """
    主页
    :param request:
    :return:
    """

    post = Post.objects.all()

    limit = 3
    paginator = Paginator(post, limit)
    page = request.GET.get('page', 1)

    result = paginator.page(page)
    context = {
        "post_list": result,
        "page": page
    }
    return render(request=request, template_name='index.html')
