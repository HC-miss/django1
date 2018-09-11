from django.conf.urls import url, include
from blog import views


app_name = 'blog'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^blog/(\d*)', views.index),
    url(r'^post/(\d+)', views.post, name='post'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(\d+)', views.category, name='category'),
    url(r'^archive/(\d+)/(\d+)', views.archive, name='archive'),
    url(r'^search/$', views.search),
]