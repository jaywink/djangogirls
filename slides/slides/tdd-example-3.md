### TDD example - template test

Since we're likely going to add a link in the template for this feature, we should write a test for it too. We know our requirements says the button/link should have the text *"Publish"* - so we can write a test for it even though we don't know yet how we will implement it - a button, A-tag, etc.

    def test_superuser_has_publish_button_in_unpublished_blog_post(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        ## We can safely check for just the word 'Publish', since we know the
        ## test post will not include it
        self.assertContains(response, "Publish") 
