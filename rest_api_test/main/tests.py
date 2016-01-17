from django.test import TestCase, RequestFactory
from main.views import decode_request 
import json

# Create your tests here.
class MockRequestObject():
    def __init__(self, body):
        self.body = json.dumps(body)


class HttpTestCase(TestCase):
    def test_decode_request(self):
        request = MockRequestObject({"name": "jenkins_test_name", "mail": "jenkins_test_mail@mail.com", "blurb": "jenkins test blurb"})
        decoded_request = decode_request(request)
        self.assertEqual("jenkins_test_name", decoded_request['name'])
        self.assertEqual("jenkins_test_mail@mail.com", decoded_request['mail'])
        self.assertEqual("jenkins test blurb", decoded_request['blurb'])
