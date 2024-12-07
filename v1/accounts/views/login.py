from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from ..models.user import User
from ..serializers.user import UserLoginSerializer


class LoginView(APIView):
    authentication_classes = []  # 인증 비활성화
    permission_classes = []      # 권한 검사 비활성화
    
    @staticmethod
    def post(request):
        '''
        get user data and API Token
        
        authenticate()는 내부적으로 UserManager를 사용해 사용자 정보를 조회
        authenticate는 django에서 인증을 수행할 때 등록된 AUTHENTICATION_BACKENDS를 사용
        기본 인증인 ModelBackend는 UserManager의 get 메서드를 호출해 사용자 정보를 조회
        
        UserManager는 objects를 통해 사용자 데이터를 제공하거나 처리
        이는 LoginView가 User 모델의 데이터를 쿼리하고 인증하는 데 필요한 기반을 제공
        '''
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user:
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    