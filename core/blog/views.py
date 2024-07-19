from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin, )


# override a TemplateView
class HomePageView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "mohsen"
        context["post_obj"] = Post.objects.all()
        return context


# override a RedirectView
class PageView(RedirectView):
    url = 'https://maktabkhooneh.com/'

    def get_redirect_url(self, *args, **kwargs):
        post_obj = get_object_or_404(Post, pk=kwargs['pk'])
        print(post_obj)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(PermissionRequiredMixin, ListView):
    permission_required = "blog.view_post"
    # queryset = Post.objects.all()

    model = Post
    context_object_name = "obj_post"
    paginate_by = 4
    ordering = "-id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)  # note that obj_post is called in html no posts
    #     return posts


class PostDetailView(DetailView):
    model = Post


# creation of form using Formview
"""
class PostCreateFormView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content','status', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'blog.edit_post'
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
    success_url = "/blog/post/"


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"