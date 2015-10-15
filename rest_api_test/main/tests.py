from django.test import TestCase

# Create your tests here.

class HelloTestCase(TestCase):
    def hello_test(self):
        self.assertequal(1, 1)
