### TDD example - why?

It's tempting to *just write the code* and add a test later. It is however also a bad thing to do.

* Once the code is finished, you will be tempted, *or forced by deadlines*, to just commit the code and move on. Result: **no test coverage**
* You will be writing the test to pass which is always worse than writing a test to fail.
   * When writing a test to pass, it is possible the test doesn't even fail if the feature breaks.
   * When writing a test to fail, you will always see it start passing once the feature is implemented. This means it will also break if the feature stops working.
