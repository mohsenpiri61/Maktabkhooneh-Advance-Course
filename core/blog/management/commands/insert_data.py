from django.core.management.base import BaseCommand

from faker import Faker
import random 
from datetime import datetime

from accounts.models import User, Profile
from blog.models import Post, Category


category_list = ["IT", "Design", "Fun"]


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user_obj = User.objects.create_user(email=self.fake.email(), password="Test@123456")
        profile_obj = Profile.objects.get(user=user_obj)
        profile_obj.first_name = self.fake.first_name()
        profile_obj.last_name = self.fake.last_name()
        profile_obj.description = self.fake.paragraph(nb_sentences=5)
        profile_obj.save()

        for _ in range(7):
            Post.objects.create(
                author=profile_obj,
                title=self.fake.paragraph(nb_sentences=1),
                content=self.fake.paragraph(nb_sentences=10),
                status=random.choice([True, False]),
                category=Category.objects.get(name=random.choice(category_list)),
                published_date=datetime.now(),
            )
