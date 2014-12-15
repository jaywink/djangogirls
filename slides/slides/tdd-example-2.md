### TDD example - continued

Running this test will obviously fail, since the functionality does not exist.

	$ python manage.py test blog.tests.SuperUserTestCase
	Creating test database for alias 'default'...
	..E..
	======================================================================
	ERROR: test_superuser_can_publish_blog_post (blog.tests.SuperUserTestCase)
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "/home/jason/workspace/djangogirls/blog/tests.py", line 49, in test_superuser_can_publish_blog_post
	    response = self.client.post(reverse("post_publish", kwargs={"pk": self.post.pk}))
	  File "/home/jason/.virtualenvs/djangogirls/lib/python3.4/site-packages/django/core/urlresolvers.py", line 551, in reverse
	    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
	  File "/home/jason/.virtualenvs/djangogirls/lib/python3.4/site-packages/django/core/urlresolvers.py", line 468, in _reverse_with_prefix
	    (lookup_view_s, args, kwargs, len(patterns), patterns))
	django.core.urlresolvers.NoReverseMatch: Reverse for 'post_publish' with arguments '()' and keyword arguments '{'pk': 1}' not found. 0 pattern(s) tried: []

	----------------------------------------------------------------------
	Ran 5 tests in 0.416s

	FAILED (errors=1)
	Destroying test database for alias 'default'...
