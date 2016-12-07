from datetime import datetime

from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Article, Category

# Create your tests here.


class TestArticle(TestCase):
    """
    Test class to test Article model
    """

    def setUp(self):
        self.date = datetime.utcnow()
        self.category = Category.objects.create(name='fiction')
        self.article = Article.objects.create(
            title='test',
            author='admin',
            publication_date=self.date,
            body='sample test',
            category=self.category
        )

    def test_article_sets_title(self):
        self.assertEqual(self.article.title, 'test')

    def test_article_sets_author(self):
        self.assertEqual(self.article.author, 'admin')

    def test_article_sets_publication_date(self):
        self.assertEqual(self.article.publication_date, self.date)

    def test_article_sets_category(self):
        self.assertEqual(self.article.category, self.category)

    def test_article_sets_body(self):
        self.assertEqual(self.article.body, 'sample test')

    def test_article_sets_hero_image(self):
        # TODO figure out how to test ImageField
        # let the tests fail for now
        self.assertEqual(self.article.hero_image, ' ')

    def test_article_sets_optional_image(self):
        # TODO figure out how to test ImageField
        # let the tests fail for now
        self.assertEqual(self.article.optional_image, ' ')

    def test_article_title_is_unique(self):
        with self.assertRaises(IntegrityError) as e:
            Article.objects.create(
                title='test',
                author='admin1',
                publication_date=datetime.utcnow(),
                body='some text',
                category=self.category)
        self.assertTrue('UNIQUE constraint failed:' in str(e.exception))


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='fiction')

    def test_category_sets_name(self):
        self.assertEqual(self.category.name, 'fiction')

    def test_category_name_is_unique(self):
        with self.assertRaises(IntegrityError) as e:
            Category.objects.create(name='fiction')
        self.assertTrue('UNIQUE constraint failed:' in str(e.exception))
