## Simple but effective

    from django.core.urlresolvers import reverse
    from django.test import TestCase
    
    class SuperUserTestCase(TestCase):
        def test_superuser_can_view_homepage(self):
            response = self.client.get(reverse('post_list'))
            self.assertContains(response, 'Django Girls Blog')