from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .views import index
from finder.utils import get_location, get_barbers


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get("/")
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        self.assertEqual(response.status_code, 200)

class UtilsTest(TestCase):
    # Every test needs latitude and longitude
    def setUp(self):
        self.latitude, self.longitude = get_location()

    # Getting barber names
    def test_get_barbers(self):
        for biz in get_barbers(self.latitude, self.longitude)['businesses']:
            print(biz['name'])
