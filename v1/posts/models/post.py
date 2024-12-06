from django.db import models
from ...accounts.models.user import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)  # 작성자 삭제 시 게시글도 삭제
    title = models.CharField(max_length=30)  
    content = models.TextField() 
    like = models.ManyToManyField(User, related_name='liked_posts', blank=True)  # 좋아요 필드 확장
    created_date = models.DateTimeField(auto_now_add=True) 
    modified_date = models.DateTimeField(auto_now=True)  
