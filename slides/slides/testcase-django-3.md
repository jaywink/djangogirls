## The setUp method helps keep things DRY

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