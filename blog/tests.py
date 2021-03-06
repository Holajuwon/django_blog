from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create(
      username='testuser',
      email='test@gmail.com',
      password='secret'
    )

    self.post = Post.objects.create(
      title='Test Post Title',
      author=self.user,
      body='Test Post Body'
    )

  def test_string_representation(self):
    post = Post(title='A sample title')
    self.assertEqual(str(post), post.title)

  def test_post_content(self):
    self.assertEqual(f'{self.post.title}', 'Test Post Title')
    self.assertEqual(f'{self.post.author}', 'testuser')
    self.assertEqual(f'{self.post.body}', 'Test Post Body')

  def test_post_list_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Test Post Body')
    self.assertTemplateUsed(response, 'home.html')

  def test_post_detail_page(self):
    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/10000/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'Test Post Title')
    self.assertTemplateUsed(response, 'post_detail.html')

