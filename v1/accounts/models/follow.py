from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follow_set")
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followed_set")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        constraint 중복 팔로우 문제 해결
        indexes 에서 성능 최적화 Follow.objects.fillter(follower=user) 같은 쿼리에서 더 빠른 검색 가능
        '''
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followee'], name='unique_follower_followee')
        ]
        indexes = [
            models.Index(fields=['follower']),
            models.Index(fields=['followee']),
        ]