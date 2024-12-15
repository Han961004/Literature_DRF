from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from ..models.user import User
from ..models.profile import Profile


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)  # 비밀번호는 write_only 설정
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'password', 'token']
    
    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        self.user = user
        return data
    
    @staticmethod
    def get_token(user):
        '''
        get or create token
        '''
        token, created = Token.objects.get_or_create(user=user) # 토큰 생성
        return token.key