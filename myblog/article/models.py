from django.db import models
from account.models import User
from tinymce.models import HTMLField


class Category(models.Model):
    cname = models.CharField(max_length=20, unique=True, verbose_name='分类')

    class Meta:
        db_table = 'category'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.cname


class Tag(models.Model):
    tname = models.CharField(max_length=20, verbose_name='标签', unique=True)

    class Meta:
        db_table = 'tag'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.tname


class Article(models.Model):
    uname = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    # 类别
    title = models.CharField(max_length=20, verbose_name='标题')
    content = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    read_num = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    collect_num = models.PositiveIntegerField(default=0, verbose_name='收藏量')
    img = models.ImageField(upload_to='articleimg', null=True, blank=True)
    # tag = models.ManyToManyField(Tag)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'article'
        verbose_name_plural = '博客'

    def __str__(self):
        return self.title

