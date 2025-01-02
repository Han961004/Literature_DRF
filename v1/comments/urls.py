from django.urls import path
from .views.literature import *


urlpatterns = [
    path('v1/posts/<int:post_id>/comments/', LiteratureCommentView.as_view(), name='literature-comments'),
    path('v1/posts/<int:post_id>/<int:comment_id>/', LiteratureCommentDetailView.as_view(), name='literature-comment-detail'),
]
