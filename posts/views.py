# posts/views.py

from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
