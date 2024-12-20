from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.literature import LiteratureComment
from ..models.literature import LiteraturePost
from ..serializers.literature import LiteratureCommentSerializer, LiteratureCommentCreateSerializer


class LiteratureCommentView(APIView):
    def get(self, request, post_id):
        """
        특정 게시글의 댓글 목록 조회
        """
        post = get_object_or_404(LiteraturePost, id=post_id)  # 게시글 존재 여부 확인
        comments = post.comments.all()  # 해당 게시글의 모든 댓글 가져오기
        serializer = LiteratureCommentSerializer(comments, many=True)  # 댓글 목록 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        serializer = LiteratureCommentCreateSerializer(
            data=request.data,
            context={'request': request, 'post_id': post_id}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(LiteratureCommentSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiteratureCommentDetailView(APIView):
    """
    개별 댓글 조회, 수정, 삭제를 처리하는 View
    """

    def get(self, request, comment_id):
        """
        개별 댓글 조회
        """
        comment = get_object_or_404(LiteratureComment, pk=comment_id)
        serializer = LiteratureCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, comment_id):
        """
        댓글 수정
        """
        comment = get_object_or_404(LiteratureComment, pk=comment_id)
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = LiteratureCommentCreateSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(LiteratureCommentSerializer(serializer.instance).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        """
        댓글 삭제
        """
        comment = get_object_or_404(LiteratureComment, pk=comment_id)
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
