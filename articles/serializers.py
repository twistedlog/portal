from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Article
        fields = ('title', 'author', 'publication_date', 'category', 'body', 'hero_image')
