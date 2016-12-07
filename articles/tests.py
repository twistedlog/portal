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

    def test_article_sets_publication_date(self):
        article = Article.objects.get()
        self.assertEqual(article.publication_date, '')

    def test_article_sets_category(self):
        article = Article.objects.get()
        self.assertEqual(article.category, '')

    def test_article_sets_body(self):
        article = Article.objects.get()
        self.assertEqual(article.body, '')

    def test_article_sets_hero_image(self):
        #TODO filgure out how to test ImageField
        pass

    def test_article_sets_optional_image(self):
        #TODO filgure out how to test ImageField
        pass
