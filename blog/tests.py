# -*- coding: utf-8 -*-
import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.test import TestCase

from selenium.webdriver.firefox.webdriver import WebDriver

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

    def test_superuser_can_publish_blog_post(self):
        # Note: if this was a live server test case, we could browse to the
        # post and click the button. While that is fine, the publish view
        # can be separately and individually tested by directly posting to it.
        response = self.client.post(reverse("post_publish", kwargs={"pk": self.post.pk}))
        # We could check for status code, but `assertRedirects` is better
        self.assertRedirects(response, reverse("post_detail", kwargs={"pk": self.post.pk}))
        # Note: We check here if the publish was successful, even though that is already
        # handled by the model test.
        # When testing, more can be better.
        post = Post.objects.get(id=self.post.pk)
        self.assertIsNotNone(post.published_date)

    def test_superuser_has_publish_button_in_unpublished_blog_post(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        # We can safely check for just the word 'Publish', since we know the
        # test post will not include it
        self.assertContains(response, "Publish")

    def test_superuser_can_edit_old_blog_post(self):
        new_title = 'Test Title 3'
        new_text = 'Blah blah blah...'

        response = self.client.post(reverse('post_edit', kwargs={'pk': self.post.pk}), {
            'title': new_title,
            'text': new_text
        }, follow=True)

        self.assertRedirects(response, reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertContains(response, new_title)

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


class SeleniumTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTestCase, cls).tearDownClass()

    def setUp(self):
        super().setUp()
        User.objects.create_superuser(username="admin", password="admin", email='')

    def build_absolute_url(self, relative_url):
        if not relative_url.startswith('/'):
            relative_url = reverse(relative_url)
        return '%s%s' % (self.live_server_url, relative_url)

    def test_browse_to_page(self):
        # Browse to the login page
        self.selenium.get(self.build_absolute_url('/admin/login/?next=/'))
        time.sleep(3)

        # Fill out input
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        time.sleep(3)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('admin')
        time.sleep(3)

        # Log in
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        time.sleep(3)

        # Browse to new post
        self.selenium.get(self.build_absolute_url('post_new'))
        time.sleep(3)

        # Fill out input
        title_input = self.selenium.find_element_by_name("title")
        title_input.send_keys('The best title ever')
        time.sleep(3)
        text_input = self.selenium.find_element_by_name("text")
        text_input.send_keys('admin')

        for word in 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut scelerisque sapien eros, quis pellentesque dolor imperdiet eu. Fusce ligula justo, viverra in eros non, convallis porta velit. Maecenas varius bibendum commodo. Suspendisse suscipit congue vestibulum. Aliquam sit amet commodo nisi. Suspendisse lectus nisl, lobortis id lacus eu, mollis convallis libero. Mauris et neque sit amet tortor eleifend pellentesque. Praesent quis mauris eget risus posuere suscipit. Nullam purus sapien, aliquet id erat et, blandit suscipit dolor. Nunc mattis lacinia metus ac rutrum. Curabitur ut ligula sit amet purus feugiat ornare sed ac neque. Maecenas porttitor erat orci, ut sodales nunc egestas vitae. Praesent feugiat rhoncus neque, non faucibus mauris. Pellentesque placerat auctor imperdiet. Duis pulvinar, metus nec placerat gravida, nibh leo tristique tortor, ut porta lacus eros et libero. '.split():
            text_input.send_keys(word + " ")
        time.sleep(3)

        # Submit post
        self.selenium.find_element_by_xpath('//button[@value="Save"]').click()
        time.sleep(3)



