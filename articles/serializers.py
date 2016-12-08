from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'publication_date', 'category', 'body', 'hero_image')


class ArticleNavigationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'hero_image', )
