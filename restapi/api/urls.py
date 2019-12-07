from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view()),  # 本モデルの取得(一覧)・登録
    path('books/<pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),  # 本モデルの取得(詳細)・更新・一部更新・削除
]