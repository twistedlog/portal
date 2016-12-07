from datetime import datetime

from django.db import transaction
from django.db.utils import IntegrityError
from django.test import Client, TestCase
from django.urls import reverse

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
        # Note:
        # http://stackoverflow.com/questions/21458387/transactionmanagementerror-you-cant-execute-queries-until-the-end-of-the-atom
        try:
            with transaction.atomic():
                article = Article.objects.create(
                    title='test',
                    author='admin1',
                    publication_date=datetime.utcnow(),
                    body='some text',
                    category=self.category)
        except IntegrityError as e:
            self.assertTrue('UNIQUE constraint failed:' in str(e))
        else:
            article.delete()
            self.fail('Title field not unique')

    def test_article_str_represenation(self):
        self.assertEqual(str(self.article), 'Title: test, Author: admin')

    def tearDown(self):
        self.article.delete()
        self.category.delete()


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='fiction')

    def test_category_sets_name(self):
        self.assertEqual(self.category.name, 'fiction')

    def test_category_name_is_unique(self):
        try:
            with transaction.atomic():
                category = Category.objects.create(name='fiction')
        except IntegrityError as e:
            self.assertTrue('UNIQUE constraint failed:' in str(e))
        else:
            category.delete()
            self.fail('Name field not unique')

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), 'Name: fiction')

    def tearDown(self):
        self.category.delete()


class TestArticleList(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_returns_http_status_code_200(self):
        url = reverse('article-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
