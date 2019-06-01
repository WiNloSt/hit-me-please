from django.contrib import admin
from django.test import TestCase

from ..admin import HitterAdmin
from ..models import Hitter


class HitterAdminTest(TestCase):
    def test_hitter_registration(self):
        self.assertIsInstance(admin.site._registry[Hitter], HitterAdmin)

    def test_hitter_list_display(self):
        list_display = ('email',)
        self.assertEqual(HitterAdmin.list_display, list_display)
