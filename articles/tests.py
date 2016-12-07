from django.test import TestCase

from .models import Article
# Create your tests here.


class TestArticle(TestCase):
    """
    Test class to test Article model
    """

    def setUp(TestCase):
        Article.objects.create(title='test', author='admin')

    def test_article_sets_title(self):
        article = Article.objects.get()
        self.assertEqual(article.title, 'test')

    def test_article_sets_author(self):
        article = Article.objects.get()
        self.assertEqual(article.author, 'admin')
