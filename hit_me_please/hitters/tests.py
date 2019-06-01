from django.contrib import admin
from django.test import TestCase

from .admin import HitterAdmin
from .models import Hitter


class HitterTest(TestCase):
    def test_email_field(self):
        email = 'a@b.com'
        hitter = Hitter.objects.create(email=email)
        self.assertEqual(hitter.email, email)


class HitterAdminTest(TestCase):
    def test_hitter_registration(self):
        self.assertIsInstance(admin.site._registry[Hitter], HitterAdmin)
