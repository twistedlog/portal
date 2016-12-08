from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer, ArticleNavigationSerializer
# Create your views here.


class ArticleListView(generics.ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListNavigationView(generics.ListAPIView):

    queryset = Article.objects.all()[:4]
    serializer_class = ArticleNavigationSerializer
