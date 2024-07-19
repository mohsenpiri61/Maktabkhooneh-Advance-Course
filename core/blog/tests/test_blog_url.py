from django.test import SimpleTestCase
from django.urls import reverse,resolve
from ..views import HomePageView, PostListView, PostDetailView


class TestUrl(SimpleTestCase):

    def test_blog_index_url_resolve(self):
        url = reverse('blog_app:homepage')
        self.assertEquals(resolve(url).func.view_class,HomePageView)
    
    def test_blog_post_list_url_resolve(self):
        url = reverse('blog_app:post-list')
        self.assertEquals(resolve(url).func.view_class,PostListView)

    def test_blog_post_detail_url_resolve(self):
        url = reverse('blog_app:post-detail',kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class,PostDetailView)
