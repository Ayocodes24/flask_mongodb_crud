import unittest
from app import app, mongo
from models.user import User
from bson.objectid import ObjectId

class UserResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        
    def test_update_user(self):
        user_id = mongo.db.users.insert_one({
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'password_hash': User('Jane Doe', 'jane@example.com', 'password123').password_hash
        }).inserted_id

        response = self.app.put(f'/users/{user_id}', json={
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        
    def test_delete_user(self):
        user_id = mongo.db.users.insert_one({
            'name': 'Jake Doe',
            'email': 'jake@example.com',
            'password_hash': User('Jake Doe', 'jake@example.com', 'password123').password_hash
        }).inserted_id

        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
