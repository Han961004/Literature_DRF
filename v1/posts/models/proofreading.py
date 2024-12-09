from django.db import models
from ...accounts.models.user import User
from ...posts.models.literature import Literature


class Proofreading(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)  # 작성자 삭제 시 게시글도 삭제
    literature = models.ForeignKey(Literature, related_name='proofreadings', on_delete=models.CASCADE) # 첨삭을 요청할 게시글 id
    title = models.CharField(max_length=30)  
    content = models.TextField() 
    created_date = models.DateTimeField(auto_now_add=True) 
    modified_date = models.DateTimeField(auto_now=True)  
