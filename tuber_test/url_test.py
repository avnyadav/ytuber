from django.test import TestCase

class UrlTestCase(TestCase):

    def testHomePage(self):
        response = self.client.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def testAboutPage(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def testContactPage(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)