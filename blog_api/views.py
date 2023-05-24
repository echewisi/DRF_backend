from django.shortcuts import render
from core.models import Post
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import PostSerializer
class PostList(ListCreateAPIView):
    queryset= Post.postobjects.all() #returns all objects flagged as 'published'
    serializer_class= PostSerializer
    
class PostDetail(RetrieveDestroyAPIView):
    pass


# Create your views here.
