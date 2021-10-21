from django.urls import path
from .views import HomePageView, AboutPageView, BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView, BlogCreateView, LikeView, AddCommentView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('about/', AboutPageView.as_view(), name='about'), # new
	path('blog/', BlogListView.as_view(), name='blog'),
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # new
	path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), 
    path('post/new/', BlogCreateView.as_view(), name='post_new'), # new
    #path('like/<int:pk>/', LikeView, name='like_post'),
    path('ajax/like/', LikeView, name='like'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name= 'add_comment')
]