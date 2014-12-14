### TDD example - continued

As expected, this test, will also fail.

    FAIL: test_superuser_has_publish_button_in_unpublished_blog_post (blog.tests.SuperUserTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/jason/workspace/djangogirls/blog/tests.py", line 61, in test_superuser_has_publish_button_in_unpublished_blog_post
        self.assertContains(response, "Publish")
      File "/home/jason/.virtualenvs/djangogirls/lib/python3.4/site-packages/django/test/testcases.py", line 363, in assertContains
        msg_prefix + "Couldn't find %s in response" % text_repr)
    AssertionError: False is not true : Couldn't find 'Publish' in response

What about the model `.publish()` functionality? We don't need a test for that, we're already covered there.
