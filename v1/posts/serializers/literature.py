from rest_framework import serializers

from ...accounts.serializers.user import UserSerializer
from ..models.literature import LiteraturePost


class LiteratureSerializer(serializers.ModelSerializer):
    # 작성자 정보를 포함하는 시리얼라이저
    user = UserSerializer(read_only=True)
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = LiteraturePost
        fields = '__all__'

    @staticmethod
    def get_like_count(post):
        '''
        좋아요 수를 반환합니다.
        '''
        return post.like.count()

class LiteratureCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LiteraturePost
        fields = ['user', 'title', 'content']  # 생성 시 필요한 필드 제한

class LiteratureUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LiteraturePost
        fields = ['title', 'content', 'modified_date']  # 수정 가능한 필드
        read_only_fields = ['modified_date']  # 수정 시 자동 업데이트되는 필드