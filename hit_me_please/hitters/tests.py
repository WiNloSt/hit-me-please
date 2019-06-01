from django.test import TestCase

from .models import Hitter


class HitterTest(TestCase):
    def test_email_field(self):
        Hitter.objects.create(email='a@b.com')
