from django.urls import path
from . import views
from .views import TopicListView, TopicDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   	path('', TopicListView.as_view(), name='home'),
   	path('post/<int:pk>/', TopicDetailView.as_view(), name='post_detail'),
]

urlpatterns += staticfiles_urlpatterns()