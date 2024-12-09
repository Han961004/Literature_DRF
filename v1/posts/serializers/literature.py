from rest_framework import serializers

from ...accounts.serializers.user import UserSerializer
from ..models.literature import Literature


class LiteratureSerializer(serializers.ModelSerializer):
    # post_comment_count = serializers.SerializerMethodField()
    user = UserSerializer()
    
    class Meta:
        model = Literature
        fields = '__all__'
        
    # @staticmethod
    # def get_post_comment_count(post):
    #     return Post

class LiteratureCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Literature
        fields = '__all__'

class LiteratureUpdateSerializer(serializers.ModelSerializer):
    pass

class LiteratureCommentSerialzier(LiteratureSerializer):
    pass

