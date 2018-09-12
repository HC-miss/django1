from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'creation_time','uname','category']
    list_filter = ['title',]
    list_per_page = 10
    date_hierarchy = 'creation_time'
    search_fields = ['title', 'content']
    raw_id_fields = ['uname',]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
