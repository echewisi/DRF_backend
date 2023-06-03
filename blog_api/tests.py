from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from core.models import *
from django.contrib.auth.models import User

class PostTests(APITestCase):
    def test_view_posts(self):
        
        url= reverse('blog_api:list_create')
        response= self.client.get(url, format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category= Category.objects.create(name= 'django')
        self.test_user1= User.objects.create_user(name= 'patrick', password= "123456")
        data={"title": "new", "author": 1, "excerpt": "new", "content": "new"}  
        url= reverse("blog_api:list_create")
        response= self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# Create your tests here.
