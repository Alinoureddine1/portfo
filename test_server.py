import unittest
from flask import url_for
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_resume_redirect(self):
        response = self.app.get('/resume.pdf')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/static/resume.pdf', response.location)

    def test_html_page(self):
        response = self.app.get('/thankyou.html')
        self.assertEqual(response.status_code, 200)

    def test_submit_form(self):
        test_data = {
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }
        response = self.app.post('/submit_form', data=test_data)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/thankyou.html', response.location)

if __name__ == '__main__':
    unittest.main()