from django.contrib import admin

from .models import Article, Category
# Register your models here.


@admin.register(Article, Category)
class ArticleAdmin(admin.ModelAdmin):
    pass
