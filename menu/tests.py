from django.test import SimpleTestCase
from django.urls import reverse


class MenuPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('menu')
        self.response = self.client.get(url)

    def test_menupage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'catalog.html')

    def test_menupage_contains_correct_html(self):
        self.assertContains(self.response, 'Your TreeMenu')

    def test_menupage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'some text')

