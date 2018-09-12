from  haystack import indexes
from article.models import *


#注意格式
class ArticleIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #给title,content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-creation_time')