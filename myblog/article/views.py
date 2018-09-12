from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from account.models import User
# import random
# from django.contrib.auth.models import User
# from django.contrib.auth.views import

# 全局用户名, 登录成功到主页时会自动设置为当前用户名 缺点：每次重启服务器得从主页进 否则会为None
uname = None


def handle():
    # 获取当前用户及其所有的文章
    user = User.objects.get(uname=uname)
    articles = user.article_set.all().order_by('id')
    return user,articles


def warp(func):
    def in_warp(request, *args, **kwargs):
        if request.session.has_key('uname'):
            global uname
            uname = request.session['uname']
            return func(request, *args, **kwargs)
        else:
            return redirect('/')
    return in_warp

@warp
def index(request):
    user, articles = handle()
    # 点击排行
    # order = articles.order_by('read_num')[:3]
    # 推荐文章
    # tuijian = articles[1:4]
    # articles = articles.order_by('creation_time')
    return render(request, 'index.html', {'articles': articles, 'user': user})


@warp
def life(request):
    user, articles = handle()
    pg = Paginator(articles, 7)
    num = request.GET.get('num', '1')
    page = pg.page(int(num))
    return render(request, 'life.html', {'articles': articles, 'user': user, 'page':page})

@warp
def info(request):
    user, articles = handle()
    # 根据用户名来找每一个用户的博客
    id = request.GET.get('id', '1')
    if request.session.has_key('search'):
        id = request.session['search']
        del request.session['search']
    if id == '1':
        article = user.article_set.first()
    else:
        article = user.article_set.get(pk=id)
    previou = user.article_set.filter(pk__lt=id).last()
    next = user.article_set.filter(pk__gt=id).first()
    return render(request, 'info.html', {'article': article, 'user': user, 'previou': previou, 'next': next, 'articles':articles })

@warp
def time(request):
    articles = Article.objects.filter(uname__uname=uname)
    return render(request, 'time.html', {'articles': articles})

@warp
def about(request):
    user, articles = handle()
    return render(request, 'about.html', {'user': user})


def search(request):
    from haystack.query import SearchQuerySet
    from haystack.query import SQ

    # 获取请求参数
    keywords = request.GET.get('q','')
    search_posts = SearchQuerySet().filter(SQ(title=keywords)|SQ(content=keywords))
    s_posts = []
    for s_p in search_posts:
        s_posts.append(s_p.object)
    return render(request,'archive.html',{'archive_posts':s_posts})


def login(request):
    if request.method == 'GET':
        if request.session.has_key('uname'):
            del request.session['uname']
        return render(request, 'login.html')
    else:
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        if len(uname) >= 2 and len(pwd) >= 6:
            if User.objects.filter(uname=uname):
                if User.objects.get(uname=uname).pwd == pwd:
                    request.session['uname'] = uname
                    # request.session.set_expiry(0) #代表着关闭浏览器session过期
                    return redirect('/index/')
            else:
                    return redirect('/')
        return redirect('/')


# def register(request):
#     if request.method == 'GET':
#         return render(request, 'account/register.html')
#     else:
#         uname = request.POST.get('username', '')
#         pwd = request.POST.get('pwd', '')
#         if len(uname) >= 2 and len(pwd)>= 6:
#             if User.objects.filter(uname=uname):
#                 if User.objects.get(uname=uname).pwd == pwd:
#                     return redirect('/account/')
#             else:
#                 User.objects.create(uname=uname, pwd=pwd)
#                 return HttpResponse('注册成功')
#         return HttpResponse('注册失败')

@warp
def add(request):
    # 文本格式会导致布局紊乱
    # 要么修改文本格式 要么去index里调整显示方式
    if request.method == "GET":
        return render(request, 'add.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('hcontent')
        read = request.POST.get('read')
        collect = request.POST.get('collect')
        img = request.FILES.get('img')
        types = request.POST.get('type')
        Article.objects.create(
            uname=User.objects.get(uname=uname),
            title=title, content=content,
            read_num = read,
            collect_num=collect,
            category = Category.objects.get(cname=types),
            img = img
        )
        return redirect('/index/')


def category(request):
    category_name = request.GET.get('category')
    print(category_name)
    cate = Category.objects.get(cname=category_name)
    cates = cate.article_set.all()
    return render(request, 'category.html', {'cates': cates, 'cate': cate, 'articles':cates})