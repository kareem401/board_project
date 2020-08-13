from django.urls import path
from . import views
from .views import TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('post/<int:pk>/delete/', TopicDeleteView.as_view(), name='post_delete'),
	path('post/<int:pk>/edit/', TopicUpdateView.as_view(), name='post_edit'),
	path('post/new/', TopicCreateView.as_view(), name="post_new"),
   	path('', TopicListView.as_view(), name='home'),
   	path('post/<int:pk>/', TopicDetailView.as_view(), name='post_detail'),
   	path('', TopicCreateView.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()