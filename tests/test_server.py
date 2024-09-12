import unittest
from flask import url_for
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app

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

    def test_submit_form(self):
        with app.test_request_context():
            test_data = {
                'name': 'Test User',
                'email': 'test@example.com',
                'subject': 'Job Opportunity',
                'message': 'This is a test message'
            }
            response = self.app.post(url_for('submit_form'), data=test_data)
            self.assertEqual(response.status_code, 302)
            
            print(f"Redirect location: {response.location}")
            
            expected_location = url_for('home', _external=True)
            self.assertEqual(response.location, expected_location,
                             f"Expected redirect to {expected_location}, but got {response.location}")

    def test_submit_form_incomplete(self):
        with app.test_request_context():
            test_data = {
                'name': 'Test User',
                'email': '',  
                'subject': 'Job Opportunity',
                'message': 'This is a test message'
            }
            response = self.app.post(url_for('submit_form'), data=test_data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, url_for('home', _external=True))

    def test_favicon(self):
        response = self.app.get('/favicon.ico')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'image/vnd.microsoft.icon')

if __name__ == '__main__':
    unittest.main()