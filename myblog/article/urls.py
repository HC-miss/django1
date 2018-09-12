from django.conf.urls import url
from article import views

app_name = 'article'
urlpatterns = [
    url('^$', views.login, name='login'),
    url('^index/', views.index, name='index'),
    url('^about/', views.about, name='about'),
    url('^time/', views.time, name='time'),
    url('^info/', views.info, name='info'),
    url('^life/', views.life, name='life'),
    url(r'^search/$', views.search, name='search'),
    url('^add/', views.add, name='add'),
    url('^category/', views.category, name='category'),
]
