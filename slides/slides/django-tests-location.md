### Placing test files

Place application specific tests in application folders.

Remember, unit tests should be as independant as possible. Try to keep applications reusable by not depending tests on other project applications.

Once you have more than a few tests, consider creating a `tests` folder and clearly separating different types of tests into separate files. For example:

```
blog/
blog/tests/
blog/tests/__init__.py
blog/tests/test_models.py
blog/tests/test_views.py
blog/tests/test_templates.py
```
