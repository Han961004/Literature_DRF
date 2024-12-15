from rest_framework import serializers
from v1.accounts.models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'nickname', 'bio', 'platform']

class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['nickname', 'bio', 'platform']
    
    def update(self, instance, validated_data):
        # validated_data의 각 키-값 쌍을 순회
        for attr, value in validated_data.items():
            # 기존 객체(instance)의 속성(attr)을 새로운 값(value)으로 설정
            setattr(instance, attr, value)
        # 데이터베이스에 변경사항 저장
        instance.save()
        # 갱신된 객체 반환
        return instance
