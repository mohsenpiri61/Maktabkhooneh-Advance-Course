from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DetailView


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


class PostListView(ListView):
    # permission_required = "blog.view_post"
    # queryset = Post.objects.all()
    model = Post
    context_object_name = "obj_post"
    paginate_by = 2
    ordering = "-id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)  # note that obj_post is called in html no posts
    #     return posts
