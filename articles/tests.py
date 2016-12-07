from django.test import TestCase

from .models import Article

# Create your tests here.


class TestArticle(TestCase):
    """
    Test class to test Article model
    """

    def setUp(self):
        self.article = Article.objects.create(title='test', author='admin')

    def test_article_sets_title(self):
        self.assertEqual(self.article.title, 'test')

    def test_article_sets_author(self):
        self.assertEqual(self.article.author, 'admin')

    def test_article_sets_publication_date(self):
        self.assertEqual(self.article.publication_date, '')

    def test_article_sets_category(self):
        self.assertEqual(self.article.category, '')

    def test_article_sets_body(self):
        self.assertEqual(self.article.body, '')

    def test_article_sets_hero_image(self):
        #TODO filgure out how to test ImageField
        pass

    def test_article_sets_optional_image(self):
        #TODO filgure out how to test ImageField
        pass
