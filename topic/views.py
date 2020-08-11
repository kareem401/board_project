from django.views.generic import ListView, DetailView
from .models import Post
class TopicListView(ListView):
	model = Post
	template_name = 'home.html'

class TopicDetailView(DetailView):
	model = Post
	template_name = "post_detail.html"