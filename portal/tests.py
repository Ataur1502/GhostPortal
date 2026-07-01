from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class GhostPortalTests(TestCase):
    def test_landing_page(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Employee Secure Portal")
        self.assertContains(response, "GHOST")

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302) # Redirects to login

    def test_guest_login_and_dashboard(self):
        # The migration has already created the 'guest' user, but in django TestCase
        # standard migrations are applied, so we can verify if the user exists
        # or we can create/verify login. Let's try log in.
        login_success = self.client.login(username='guest', password='guest123')
        self.assertTrue(login_success)
        
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome, Guest")
        self.assertContains(response, "Employee Handbook.pdf")
        self.assertContains(response, "<!-- The document password isn't random. Think about who you are. -->")

    def test_download_handbook_requires_login(self):
        response = self.client.get(reverse('download_handbook'))
        self.assertEqual(response.status_code, 302)

    def test_download_handbook_authenticated(self):
        self.client.login(username='guest', password='guest123')
        response = self.client.get(reverse('download_handbook'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="Employee_Handbook.pdf"')

    def test_custom_404(self):
        response = self.client.get('/this-page-does-not-exist/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "RESOURCE NOT FOUND", status_code=404)
