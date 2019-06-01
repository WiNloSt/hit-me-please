from django.test import TestCase


class LandingPageViewTest(TestCase):
    def test_form_elements(self):
        response = self.client.get('')

        expected_elements = (
            '<form action="" method="post">',
            '<input id="email" name="email" type="email" />',
            '<button type="submit">Submit</button>',
        )

        for expected_element in expected_elements:
            self.assertContains(response, expected_element, status_code=200)
