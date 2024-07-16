from django.test import TestCase
from datetime import datetime
from ..forms import PostForm
from ..models import Category

class TestPostForm(TestCase):
    
    def test_post_form_valid_with_data(self):
        category_obj = Category.objects.create(name='django_test')
        form = PostForm(data={'title': 'test', 'content': 'desc', 'category': category_obj, 'status': True, 'published_date': datetime.now()})
        self.assertTrue(form.is_valid())                