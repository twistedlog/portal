from django.conf.urls import url
from .views import ArticleListView


urlpatterns = [
    url(r'list/$', ArticleListView.as_view(), name='article-list')
]
