from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from ..models.literature import LiteraturePost
from ..serializers.literature import LiteratureSerializer, LiteratureCreateSerializer, LiteratureUpdateSerializer


class LiteratureView(APIView):
    
    @staticmethod
    def get():
        '''
        all posts's list
        '''
        literatures = LiteraturePost.objects.all()
        return Response(LiteratureSerializer(literatures, many=True).data)
    
    @staticmethod
    def post(request):
        '''
        create
        '''
        serializer = LiteratureCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(LiteratureSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LiteratureDetailView(APIView):
    
    @staticmethod
    def get(post_id):
        '''
        view individual post
        '''
        literature = get_object_or_404(LiteraturePost, pk=post_id)
        return Response(LiteratureSerializer(literature).data)
    
    # @staticmethod
    # def put(request, post_id):
    #     '''
    #     update post
    #     '''
    #     post = get_object_or_404(LiteraturePost, pk=post_id)
    #     return 
    
    @staticmethod
    def delete(request, post_id):
        post = get_object_or_404(LiteraturePost, pk=post_id)
        if post.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LiteratureCreateView(APIView):
    
    @staticmethod
    def post(request):
        """
        Create a new Literature post.
        """
        serializer = LiteratureCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(LiteratureSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
