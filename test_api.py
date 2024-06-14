import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'
    
    def test_create_blog_post(self):
        """Test creating a blog post."""
        data = {'id': 1, 'title': 'Test Post', 'content': 'This is a test post.'}
        response = requests.post(f'{self.BASE_URL}/blog', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['status'], 'sucess')

    def test_create_blog_post_invalid(self):
        """Test creating a blog post with invalid data."""
        data = {'id': 1, 'title': 'Test Post'}  # Missing 'content'
        response = requests.post(f'{self.BASE_URL}/blog', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_get_blog_posts(self):
        """Test retrieving blog posts."""
        response = requests.get(f'{self.BASE_URL}/blog')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()