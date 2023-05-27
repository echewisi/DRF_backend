from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category= Category.objects.create(name= 'django')
        test_user1= User.objects.create(username= 'testuser1', password= '123456')

# Create your tests here.
