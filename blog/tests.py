# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from blog.models import Post


class SuperUserTestCase(TestCase):
    def setUp(self):
        """Add some objects to the database that all tests will need."""
        self.user = User.objects.create_superuser(
            username='admin', email='', password='admin'
        )
        self.post = self._create_post(
            author=User.objects.get(username='admin'),
            title='Test Title 1',
            text='Here is lots of post content... blah blah blah...'
        )

        self.client.login(username='admin', password='admin')

    def test_superuser_can_view_homepage(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, 'Django Girls Blog')

    def test_superuser_post_list_shows_also_unpublished_posts(self):
        post = self._create_post(
            author=User.objects.get(username='admin'),
            title='Test Title 2',
            text='Here is lots of post content... blah blah blah...'
        )
        post.publish()
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, "Test Title 2")
        self.assertContains(response, "Test Title 1")

    def test_superuser_can_view_blog_post(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertContains(response, self.post.title)

    def test_superuser_can_add_new_blog_post(self):
        title = 'Test Title 2'
        text = 'Here is lots of post content... blah blah blah...'

        response = self.client.post(reverse('post_new'), {
            'title': title,
            'text': text,
        }, follow=True)

        post = Post.objects.get(title=title)

        self.assertRedirects(response, reverse('post_detail', kwargs={'pk': post.pk}))
        self.assertContains(response, title)

    def test_superuser_can_edit_old_blog_post(self):
        # TODO: Write a test to check if the admin can edit a previous post.
        pass

    def _create_post(self, author, title='Test Title 1', text='Lorem ipsum'):
        return Post.objects.create(
            author=author,
            title=title,
            text=text,
        )


class BasicViewsTestCase(TestCase):

    def _create_post(self, author, title='Test Title 1', text='Lorem ipsum'):
        return Post.objects.create(
            author=author,
            title=title,
            text=text,
        )

    def setUp(self):
        """Add some objects to the database that all tests will need.

        Yes these should be unified with the above - but shall we do that
        here or as a in-session code refactoring excercise?"""

        self.user = User.objects.create(
            username='author', email='', password='author'
        )
        self.post = self._create_post(
            author=User.objects.get(username='author'),
            title='Test Title 1',
            text='Here is lots of post content... blah blah blah...'
        )

    def test_blog_post_list_renders(self):
        response = self.client.get(reverse("post_list"))

    def test_blog_post_detail_renders(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": 1}))

    def test_blog_post_list_shows_only_published_posts(self):
        post = self._create_post(
            author=User.objects.get(username='author'),
            title='Test Title 2',
            text='Here is lots of post content... blah blah blah...'
        )
        post.publish()
        response = self.client.get(reverse("post_list"))
        # just match content
        # for more advanced HTML verifying - LiveServerTestCase!
        self.assertContains(response, "Test Title 2")
        self.assertNotContains(response, "Test Title 1")


class BlogModelsTestCase(TestCase):

    def _create_post(self, author, title='Test Title 1', text='Lorem ipsum'):
        return Post.objects.create(
            author=author,
            title=title,
            text=text,
        )

    def setUp(self):
        """Add some objects to the database that all tests will need.

        Yes these should be unified with the above - but shall we do that
        here or as a in-session code refactoring excercise?"""

        self.user = User.objects.create(
            username='author', email='', password='author'
        )
        self.post = self._create_post(
            author=User.objects.get(username='author'),
            title='Test Title 1',
            text='Here is lots of post content... blah blah blah...'
        )

    def test_new_post_is_not_published_by_default(self):
        post = Post.objects.first()
        self.assertIsNone(post.published_date)

    def test_post_can_be_published(self):
        post = Post.objects.first()
        post.publish()
        post = Post.objects.first() # we fetch it again, why? to see if .publish() saves as it should!
        self.assertIsNotNone(post.published_date)

    def test_post_title(self):
        post = Post.objects.first()
        self.assertEquals(str(post), post.title)
