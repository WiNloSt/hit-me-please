from django.test import TestCase

from ..models import Hitter


class LandingPageViewTest(TestCase):
    def test_form_elements(self):
        response = self.client.get('')

        expected_elements = (
            '<h1>Hit me!</h1>',
            '<form action="" method="post">',
            '<input type="hidden" name="csrfmiddlewaretoken"',
            '<input id="email" name="email" type="email" />',
            '<button type="submit">Submit</button>',
        )

        for expected_element in expected_elements:
            self.assertContains(response, expected_element, status_code=200)

    def test_form_submit(self):
        email = 'kelvin@prontomarketing.com'
        form_data = {'email': email}

        response = self.client.post('/', data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Hitter.objects.count(), 1)

        hitter = Hitter.objects.get(email=email)
        self.assertEqual(hitter.email, email)
