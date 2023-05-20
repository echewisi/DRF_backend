from django.shortcuts import render
from core.models import Post
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from .serializers import PostSerializer
class PostList(ListAPIView):
    queryset= Post.postobjects.all() #returns all objects flagged as 'published'
    serializer_class= PostSerializer
class PostDetail(RetrieveDestroyAPIView):
    pass


# Create your views here.
