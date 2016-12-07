from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return u'Name: {0}'.format(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'


class Article(models.Model):
    """
    Model representing article
    """
    title = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    body = models.TextField()
    category = models.ForeignKey(Category)
    hero_image = models.ImageField()
    optional_image = models.ImageField(blank=True)

    def __str__(self):
        return u'Title: {0}, Author: {1}'.format(self.title, self.author)

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = 'Articles'
