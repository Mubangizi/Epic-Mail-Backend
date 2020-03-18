import unittest 

import pytest

import json

from server import create_app

class MyTestClass(unittest.TestCase): 

  def setUp(self):
    # define initialize app
    self.app = create_app('testing')
    self.client = self.app.test_client()
    # propagate the exceptions to the test client
    self.app.testing = True 

  def tearDown(self):
    pass 

  def test_home_status_code(self):
    # sends HTTP GET request to the application
    # on the specified path
    result = self.client.get('/') 

    # assert the status code of the response
    self.assertEqual(result.status_code, 200) 

  def test_home_data(self):
    # sends HTTP GET request to the application
    # on the specified path
    result = self.client.get('/') 

    # assert the response data
    data = json.loads(result.data)
    self.assertEqual(data["message"], "Welcome to Epic Mail API")