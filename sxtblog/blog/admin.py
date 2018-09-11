from django.contrib import admin
from .models import *


class ModelPost(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']


admin.site.register(Post,ModelPost)
admin.site.register(Tag)
admin.site.register(Category)
