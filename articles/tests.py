from datetime import datetime

from django.test import TestCase

from .models import Article, Category

# Create your tests here.


class TestArticle(TestCase):
    """
    Test class to test Article model
    """

    def setUp(self):
        self.date = datetime.utcnow()
        self.article = Article.objects.create(
            title='test',
            author='admin',
            publication_date=self.date,
            body='sample test'
        )

    def test_article_sets_title(self):
        self.assertEqual(self.article.title, 'test')

    def test_article_sets_author(self):
        self.assertEqual(self.article.author, 'admin')

    def test_article_sets_publication_date(self):
        self.assertEqual(self.article.publication_date, self.date)

    def test_article_sets_category(self):
        self.assertEqual(self.article.category, '')

    def test_article_sets_body(self):
        self.assertEqual(self.article.body, 'sample test')

    def test_article_sets_hero_image(self):
        #TODO filgure out how to test ImageField
        pass

    def test_article_sets_optional_image(self):
        #TODO filgure out how to test ImageField
        pass


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='fiction')

    def test_category_sets_name(self):
        self.assertEqual(self.category.name, 'fiction')

    def test_category_name_is_uique(self):
        pass
