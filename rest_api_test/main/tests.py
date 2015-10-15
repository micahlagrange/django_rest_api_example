from django.test import TestCase, RequestFactory
from views import decode_request 

# Create your tests here.

class HttpTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
    
    def test_decode_request(self):
        request = self.factory.get('/users/1')
        decoded_request = decode_request(request)
        print(decoded_request)
