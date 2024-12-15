from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from ..models.user import User
from ..models.profile import Profile


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        '''
        User와 연관된 Profile 생성 및 패스워드 암호화
        '''
        validated_data['password'] = make_password(validated_data['password'])  # 비밀번호 암호화
        user = super().create(validated_data)
        Profile.objects.create(user=user, nickname=validated_data.get('nickname', 'Default'), platform='web')
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
