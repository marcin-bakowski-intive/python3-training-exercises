from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class FibonacciRestAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_fibonacci_numbers_invalid_n_parameter(self):
        resp = self.client.get(reverse("fibonacci"))

        self.assertEqual(resp.status_code, 400)
        self.assertIn("error_message", resp.data)

    def test_fibonacci_numbers_returns_list(self):
        resp = self.client.get(reverse("fibonacci"), data={"n": 5})

        self.assertEqual(resp.status_code, 200)
        # assert returned response content
        self.fail("TODO")
