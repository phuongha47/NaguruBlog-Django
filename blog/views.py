from django.views.generic import ListView, DetailView  
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy, reverse # new
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))