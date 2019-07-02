from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
	path('', PostListView.as_view(), name = 'stories-home'),
	path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
	path('stories/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
	path('stories/new/', PostCreateView.as_view(), name = 'post-create'),
	path('stories/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
	path('stories/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
	path('about/', views.about, name = 'stories-about'),
]