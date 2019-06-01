from django.test import TestCase

from ..models import Hitter


class HitterTest(TestCase):
    def test_email_field(self):
        email = 'a@b.com'
        hitter = Hitter.objects.create(email=email)
        self.assertEqual(hitter.email, email)
