from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-published_date')


class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'text', )
    template_name = 'blog/post_edit.html'

    def get_object(self):
        post = super().get_object()
        post.published_date = timezone.now()
        post.save()
        return post

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'text', )
    template_name = 'blog/post_edit.html'

    def get_object(self):
        post = super().get_object()
        post.published_date = timezone.now()
        post.save()
        return post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
