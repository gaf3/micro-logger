# micro-logger

A JSON logger made for microservices

# Usage

```python
import micro_logger

# This overrides the root logger as well

logger = micro_logger.getLogger("my-service")

logger.info("sure", extra={"a": 1})
```

# Testing

```python
import micro_logger_unittest

import micro_logger

# Use this class as a base

class TestUnitTest(micro_logger_unittest.TestCase):

    # Override for all tests

    @unittest.mock.patch("micro_logger.getLogger", micro_logger_unittest.MockLogger)
    def setUp(self):

        self.logger = micro_logger.getLogger("unit")

    # Any test can check for logging

    def test_assertLogged(self):

        self.logger.info("sure", extra={"a": 1})

        self.assertLogged(self.logger, "info", "sure", extra={"a": 1})
```
