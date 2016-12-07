from django.test import TestCase

from .models import Article
# Create your tests here.


class TestArticles(TestCase):
    """
    Test class to test Article model
    """

    def setUp(TestCase):
        Article.objects.create(title='test')

    def test_article_sets_title(self):
        article = Article.objects.get()
        self.assertEqual(article.title, 'test')
