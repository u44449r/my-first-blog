from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),#トップページ
    path('post/<int:pk>/', views.post_detail, name='post_detail'),# /post/1とか
    path('post/new', views.post_new, name='post_new'),#/post/new 新記事
]