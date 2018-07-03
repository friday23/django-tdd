from django.test import TestCase


class SmokeTest(TestCase):

    def test_bad_maths(self):
        print( 1+1 )
        self.assertEqual(1 + 1, 3)