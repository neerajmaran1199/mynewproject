from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView, ListView, DetailView, DeleteView
# Create your views here.
def HomePage(request):
    name = 'ankit'
    return render(request, 'newspaper/index.html',{'student':name} )


def Page(request):
    posts = Post.objects.all()
    
    return render(request, 'newspaper/home.html',{'posts':posts} )

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'newspaper/create.html'
    

class PostListView(ListView):
    model = Post
    template_name = 'newspaper/home.html'
    context_object_name = 'posts'
   

class PostDetailView(DetailView):
    model = Post
    template_name = 'newspaper/post_detail.html'
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'newspaper/post_delete.html'

class PostUpdateView(DetailView):
    model = Post
    template_name = 'newspaper/post_update.html'