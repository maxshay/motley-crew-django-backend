from django.test import TestCase
import base64 # new
import json # new
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase




#fix data base error permission denided to create database
class TestTest(APITestCase):
    def test_test(self):
        self.assertEqual(1,1)
