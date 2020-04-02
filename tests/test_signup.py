import unittest
import json
from main import app, db
from models.usermodel import UserModel

class SignupTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_seccessful_signup(self):
        payload = json.dumps({
            "full_name":"mr tee",
            "email" :"kalunge",
            "password" :"kalungezz"
        })
        
        response = self.app.post('/api/home/registration', headers={"Content-Type": "application/json"}, data=payload)
        # response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)


        #then
        self.assertEqual(response.is_json, response.is_json)
        self.assertEqual(200, response.status_code)


        def tearDown(self):
            """Delete database collections after the test is carried out"""
            for collection in self.db.list_collection_names():
                self.db.drop_collection(collection)