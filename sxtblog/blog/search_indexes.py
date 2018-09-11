from haystack import indexes
from .models import Post


# 搜索引擎模板指定的文件  文件名必须为要索引的类名_text.txt
# 指定对于某个类的某些数据建立索引
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 给title,content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all().order_by('-created')
