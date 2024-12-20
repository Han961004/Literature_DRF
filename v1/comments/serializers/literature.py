from rest_framework import serializers
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from ..models.literature import LiteratureComment, LiteraturePost


class LiteratureCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = LiteratureComment
        fields = ['id', 'user', 'post', 'content', 'created_date', 'modified_date']

class LiteratureCommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # 현재 로그인 유저 자동 할당

    class Meta:
        model = LiteratureComment
        fields = ['user', 'content']  # `post` 필드를 제외하여 요청 데이터에 포함되지 않도록 함

    def create(self, validated_data):
        request = self.context.get('request')  # `request` 가져오기
        post_id = self.context.get('post_id')  # `post_id` 가져오기
        post = get_object_or_404(LiteraturePost, id=post_id)  # `post` 객체 확인
        validated_data['post'] = post  # `post` 필드를 추가
        return super().create(validated_data)
