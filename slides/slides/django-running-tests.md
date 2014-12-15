### Running tests

    python manage.py test

Running a single app

    python manage.py test blog

Running a single test case

    python manage.py test blog.tests.BlogPostViewTestCase

Running a single test in a test case

    python manage.py test blog.tests.BlogPostViewTestCase.test_view_renders

