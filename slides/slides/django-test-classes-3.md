### Django test classes

For real (or emulated) browser testing - you need the `LiveServerTestCase`.

It spawns a `runserver` instance for the tests to use, allowing _real_ UI testing using for example [Splinter](http://splinter.cobrateam.info), which is a high level framework for browser testing.
