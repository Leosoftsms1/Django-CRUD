from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from.models import BlogPost , 
    class PostListView(ListView):
    model = Post
    # context_object_name = 'object_list'
    ordering = ['-date_posted']

    class PostCreateView(ListView):
    model = Post
       fields = "_all_"
       success_url = reverse_lazy("blog:all")
          template_name = 'blogcreate.html'

   class PostDetailView(DetailView):
       model = Post
       fields = "_all_"
       success_url = reverse_lazy("blog:all")
          template_name = 'blogdetail.html'

class PostDeleteView(DetailView):
       model = Post
       fields = "_all_"
       success_url = reverse_lazy("blog:all")
          template_name = 'blogdetail.html'
          