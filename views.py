from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView 
from .models import Post, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse # new
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

class BlogListView(ListView):
	model = Post
	template_name = 'blog.html'
class BlogDetailView(DetailView): # new
	model = Post
	template_name = 'post_detail.html'
class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    success_url = reverse_lazy('blog')

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('blog')

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog')


def LikeView(request):
    if request.method == "GET":
        i= request.GET.get('i',None)
        p= Post.objects.get(id=i)
        p.likes = p.likes+1
        p.save()
        data= {'i':p.like}
    return JsonResponse(data)

class AddCommentView(CreateView): # new
    model = Comment
    template_name = 'add_comment.html'
    fields =  '__all__'
   

