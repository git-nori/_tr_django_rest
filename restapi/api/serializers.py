from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """本モデル用シリアライザ"""

    class Meta:
        model = Book  # 対象のモデルクラスを指定
        exclude = ['created_at']  # 利用しないモデルのフィールドを指定
