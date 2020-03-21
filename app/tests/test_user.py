import unittest

from server import create_app
from app.models import db

class UserTestCase(unittest.TestCase):
    """ user test case """

    def setUp(self):
        """ executed before each test """

        # define test variables and initialize app
        self.app = create_app('testing')
        self.client = self.app.test_client()
        
        self.test_user = {
            'email': 'test_email@testdomain.com',
            'username': 'test_name',
            'password': 'test_password'
        }

        with self.app.app_context():
            """ bind app to current context """

            # create all tables
            db.engine.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
            db.create_all()

    def tearDown(self):
        """ executed after each test """
        # destroy created data
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


    def test_sign_up(self):
        """ test user creation """

        response = self.client.post('/auth/signup', json=self.test_user)

        self.assertEqual(response.status_code, 201)
        self.assertIn('test_email@testdomain.com', str(response.data))
        self.assertIn('test_name', str(response.data))

    def test_sign_up_existing_email(self):
        """ test email exists """

        response1 =self.client.post('/auth/signup', json=self.test_user)
        self.assertEqual(response1.status_code, 201)

        response2 =self.client.post('/auth/signup', json=self.test_user)
        self.assertEqual(response2.status_code, 400)
        self.assertIn('Email test_email@testdomain.com already in use.', str(response2.data))

    def test_sign_up_wrong_email_structure(self):
        """ test wrong email structure """

        test_user_wrong_email = {
            'email': 'test_emailtest@domaincom',
            'username': 'test_username',
            'password': 'test_password'
        }
        response =self.client.post('/auth/signup', json=test_user_wrong_email)
        self.assertEqual(response.status_code, 400)

    def test_get_all_users(self):
        """ get all users """
        response = self.client.get('/users')

        self.assertEqual(response.status_code, 200)

if __name__ == 'main':
    unittest.main()