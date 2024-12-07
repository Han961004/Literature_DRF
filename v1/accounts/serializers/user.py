from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from ..models.user import User
from ..models.profile import Profile


class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    platform = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'email', 'platform']
    
    @staticmethod
    def get_nickname(user):
        # Profile에서 nickname 가져오기
        profile = Profile.objects.filter(user=user).first()
        return profile.nickname if profile else None

    @staticmethod
    def get_platform(user):
        # Profile에서 platform 가져오기
        profile = Profile.objects.filter(user=user).first()
        return profile.platform if profile else None


class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        
    def create(self, validated_data):
        '''
        password 암호화 및 user 생성
        '''
        # User 생성
        user = super().create(validated_data)
        # Profile 생성
        Profile.objects.create(user=user, nickname=validated_data.get('username', 'Default'), platform='web')
        return user

    
    @staticmethod
    def validate_password(password):
        validate_password(password)
        return password
    
    # @staticmethod
    # def validate_username(value):
    #     pass
    
    # @staticmethod
    # def validate_nickname(value):
    #     pass
    
    # @staticmethod
    # def validate_email(value):
    #     pass

class UserLoginSerializer(UserSerializer):
    token = serializers.SerializerMethodField()  # 토큰 필드

    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'email', 'platform', 'token']
    
    @staticmethod
    def get_token(user):
        '''
        get or create token
        '''

        token, created = Token.objects.get_or_create(user=user) # 토큰 생성
        return token.key

class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = []