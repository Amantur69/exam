from django.urls import path, include
from .views import *


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', UserProfileListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view()),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('likes/', LikeListCreateAPIView.as_view()),
    path('likes/<int:pk>/', LikeRetrieveUpdateDestroyAPIView.as_view()),



]