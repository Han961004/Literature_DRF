from django.db import models
from ...accounts.models.user import User
from ...posts.models.literature import LiteraturePost

class LiteratureComment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)  # 댓글 작성자
    post = models.ForeignKey(LiteraturePost, related_name='comments', on_delete=models.CASCADE)  # 연결된 게시글
    content = models.TextField()  # 댓글 내용
    created_date = models.DateTimeField(auto_now_add=True)  # 댓글 작성 날짜
    modified_date = models.DateTimeField(auto_now=True)  # 댓글 수정 날짜
    