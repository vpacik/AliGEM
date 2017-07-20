from unittest import TestCase

import aligem

class TestJoke(TestCase):
    def test_is_string(self):
        s = aligem.test.hi()
        self.assertTrue(isinstance(s, basestring))
