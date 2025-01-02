from django.db import models
from ...accounts.models.user import User


class ProofreadingPost(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)  # 작성자 삭제 시 게시글도 삭제
    title = models.CharField(max_length=30)  
    content = models.TextField() 
    created_date = models.DateTimeField(auto_now_add=True) 
    modified_date = models.DateTimeField(auto_now=True)  
