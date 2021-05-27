from django.urls import path
from .views import BlogListView, BlogDetailView , BlogCreateView,BlogUpdateView, BlogDeleteView, LikeView # new
urlpatterns = [
path('', BlogListView.as_view(), name='home'),
]

urlpatterns = [
    path('post/<int:pk>/delete/', # new
BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',
BlogUpdateView.as_view(), name='post_edit'), 
    path('post/new/', BlogCreateView.as_view(), name='post_new'), # new
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # new
    path('', BlogListView.as_view(), name='home'),
    path('like/<int:pk>/', LikeView, name='like_post'),
]