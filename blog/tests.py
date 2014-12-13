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