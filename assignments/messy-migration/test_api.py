import unittest
from app import main as app_module

class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        app_module.app.testing = True
        self.client = app_module.app.test_client()

    def test_health_check(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'User Management System', resp.data)

    def test_get_all_users(self):
        resp = self.client.get('/users')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json, list)

    def test_create_and_login_user(self):
        user = {'name': 'Test User', 'email': 'testuser@example.com', 'password': 'testpass123'}
        resp = self.client.post('/users', json=user)
        self.assertEqual(resp.status_code, 201)
        user_id = resp.json['user_id']
        # Login
        resp = self.client.post('/login', json={'email': user['email'], 'password': user['password']})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['status'], 'success')
        self.assertEqual(resp.json['user_id'], user_id)

    def test_invalid_login(self):
        resp = self.client.post('/login', json={'email': 'notfound@example.com', 'password': 'wrong'})
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.json['status'], 'failed')

if __name__ == '__main__':
    unittest.main()
