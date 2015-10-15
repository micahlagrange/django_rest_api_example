from django.test import TestCase, RequestFactory
from main.views import decode_request 

# Create your tests here.

class HttpTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
    
    def test_decode_request(self):
        request = self.factory.post('/users/', {"name": "jenkins_test_name", "mail": "jenkins_test_mail@mail.com", "blurb": "jenkins test blurb"})
        decoded_request = decode_request(request)
        self.assertequal("jenkins_test_name", decoded_request['name'])
        self.assertequal("jenkins_test_mail@mail.com", decoded_request['mail']
        self.assertequal("jenkins test blurb", decoded_request['blurb']
