from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    """
    Model representing article
    """
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    body = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
