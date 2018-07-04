from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         print( 1+1 )
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):

    def test_uses_home_template(self):
            response = self.client.get('/')
            self.assertTemplateUsed(response, 'home.html')