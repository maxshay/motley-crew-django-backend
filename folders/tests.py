from django.test import TestCase
import base64
import json
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

class TestTest(APITestCase):
    def test_test(self):
        self.assertEqual(1,1)
