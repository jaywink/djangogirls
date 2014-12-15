### Django test classes

For database functionality in your tests (ie the ORM), you need `TransactionTestCase` or `TestCase`. If not, you can stick to `SimpleTestCase`.

`TransactionTestCase` enables testing database rollback and commit functionality.

`TestCase` wraps each test in a transaction, speeding up resetting database.

Additionally `TestCase` automatically creates a `Client`, automatically loads fixtures and offers extra assertions useful for testing web sites.

**If in doubt, always use `TestCase`.**
