### TDD example - publish functionality

So we're missing blog publishing functionality in our app, which is bad, so we will add it now.

We could just write the code for it, but instead **we will write a test for it**.

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
