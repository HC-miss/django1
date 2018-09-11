from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# 种类
class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cname = models.CharField(max_length=20)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = "t_category"
        verbose_name_plural = '类别'


# 标签
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=20)

    def __str__(self):
        return self.tname

    class Meta:
        db_table = "t_tag"
        verbose_name_plural = '标签'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, verbose_name='标题')
    desc = models.TextField(verbose_name='简介')
    content = RichTextUploadingField(null=True, blank=True, verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "t_post"
        verbose_name_plural = '帖子'
