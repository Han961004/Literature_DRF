from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from ..models.post import Post
from ..serializers.post import PostSerializer, PostCreateSerializer, PostUpdateSerializer


class PostView(APIView):
    
    @staticmethod
    def get(request):
        '''
        all posts's list
        '''
        posts = Post.objects.all()
        return Response(PostSerializer(posts, many=True).data)
    
    @staticmethod
    def post(request):
        '''
        create
        '''
        serializer = PostCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(PostSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    
    @staticmethod
    def get(request, post_id):
        '''
        view individual post
        '''
        post = get_object_or_404(Post, pk=post_id)
        return Response(PostSerializer(post).data)
    
    @staticmethod
    def put(request, post_id):
        '''
        update post
        '''
        post = get_object_or_404(Post, pk=post_id)
    
    @staticmethod
    def delete(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

