from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import ArticleListView, ArticleListNavigationView


urlpatterns = [
    url(r'list/$', ArticleListView.as_view(), name='article-list'),
    url(r'list/html/$', TemplateView.as_view(template_name='article_list.html')),
    url(r'navigation/$', ArticleListNavigationView.as_view(), name='article-list-navigation'),
]
