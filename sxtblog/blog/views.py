from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def get_page(num, size):
    num = int(num)
    paginator = Paginator(Post.objects.all().order_by('-created'), size)
    if num < 1:
        num = 1
    if num > paginator.num_pages:
        num = paginator.num_pages

    # 每次展示的链接数
    a_size = 3
    start = ((num-1)//a_size)*10+1
    end = start + a_size

    # if start < 1:
    #     start = 1
    if end > paginator.num_pages:
        end = paginator.num_pages + 1


    return paginator.page(num), range(start, end)


def index(request, num='1'):
    # 避免不带参数时发生的错误
    if not num:
        num = '1'
    # 每页展示的内容数量
    size = '3'
    posts, page_range = get_page(num, size)
    return render(request, 'index.html', {'posts': posts, 'page_range': page_range})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post': post})


def about(request):
    return HttpResponse('暂时没有')


def category(request, category_id):
    # 找出当前分类的所有博客
    post = Post.objects.filter(category__id=category_id)
    return render(request, 'category.html', {'post': post})


def archive(request, year, month):
    # 方法1 找出当前参数所在时间的所有博客
    post = Post.objects.filter(created__year=year, created__month=month)
    # 方法2
    # post = Post.objects.filter(Q(created__year=year)&Q(created__month=month))
    # 方法3
    # post = Post.objects.filter(created__year=year).filter(created__month=month)
    return render(request, 'archive.html', {'post': post})


# 全文搜索功能
def search(request):
    from haystack.query import SearchQuerySet
    from haystack.query import SQ

    # 获取请求参数
    keywords = request.GET.get('q', '')

    search_posts = SearchQuerySet().filter(SQ(title=keywords)|SQ(content=keywords))

    s_posts = []

    for s_p in search_posts:
        s_posts.append(s_p.object)

    return render(request, 'search.html', {'archive_posts': s_posts})
