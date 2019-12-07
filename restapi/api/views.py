from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(views.APIView):
    """本モデルの取得(一覧)・登録APIクラス"""

    """本モデルの取得(一覧)APIに対応するハンドラメソッド"""
    def get(self, request, *args, **kwargs):
        book_list = Book.objects.all()
        serializer = BookSerializer(instance=book_list, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
