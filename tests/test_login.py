import unittest
import json
from main import app


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db
    
    def successfulLogin(self):
        payload = json.dumps({
            "email":"titzo",
            "password":"titoz"
        })

        # response = self.app.post('/api/home/registration', headers={"Content-Type": "application/json"}, data=payload)

        response = self.app.post('/api/home/login', headers={"Content-TYpe" : "application/json"}, data=payload)


        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.is_json, response.is_json)

    def unsuccessfulLogin(self):
        payload = json.dumps({
            "email":"titzo",
            "password":"titoz"
        })

        self.assertEqual(response.status_code, 401)

    
    def tearDown(self):
        """Delete database collections after the test is carried out"""
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
