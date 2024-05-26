from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.views.generic.base import RedirectView


app_name = "blog_app"
urlpatterns = [
    path('home', TemplateView.as_view(template_name="home.html", extra_context={"name": "test is ok"})),
    path('homepage', views.HomePageView.as_view(), name='homepage'),
    path('go-to-maktabkhooneh', RedirectView.as_view(url='https://maktabkhooneh.com/'), name='maktab1'),
    path('maktabkhooneh', RedirectView.as_view(pattern_name="blog_app:maktab1"), name='maktab2'),
    path('home/<int:pk>/', views.PageView.as_view()),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    #path("post/create/", views.PostCreateFormView.as_view(), name="post-create"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

]