from rest_framework import serializers

from ...accounts.serializers.user import UserSerializer
from ..models.post import Post


class PostSerializer(serializers.ModelSerializer):
    # post_comment_count = serializers.SerializerMethodField()
    user = UserSerializer()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    # @staticmethod
    # def get_post_comment_count(post):
    #     return Post

class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'

class PostUpdateSerializer(serializers.ModelSerializer):
    pass

class PostCommentSerialzier(PostSerializer):
    pass

