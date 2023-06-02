from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

"""you can test the model with the test format below
NB: you can edit it to match the requirements you want"""
class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category= Category.objects.create(name= 'study group')
        test_user1= User.objects.create(username= 'patrick', password= '123456')
        test_post= Post.objects.create(category_id=1, title='post title', excerpt= 'everything everywhere', content= 'null', slug='post-title', author_id=1, status= 'published')

    def test_blog(self):
        post= Post.postobjects.get(id=1)
        category= Category.objects.get(id=1)
        author= f'{post.author}'
        excerpt= f'{post.excerpt}'
        title= f'{post.title}'
        content= f'{post.content}'
        status= f'{post.status}'
        self.assertEqual(author, 'patrick')
        self.assertEqual(excerpt, 'everything everywhere')
        self.assertEqual(title,'post title' )
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'post title')
        self.assertEqual(str(category), 'study group')

# Create your tests here.