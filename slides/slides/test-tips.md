### Use descriptive names for tests
<br>
Bad:

    def test_view_publishing_stuff(self):

Good:

    def test_staff_member_can_publish_blog_post(self):

<br>
Keep tests small - above example should only test if *staff member can publish a post*, as the name says.
