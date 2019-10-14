from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Creating a "Post" model. Each class is going to be it's own table in the DB


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=100)  # arguments that specify restrains on these fields
    content = models.TextField()  # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)  # passing function as default value (thats why no parenthesis)
    # one to many relationship between User and a Post
    authors = models.ForeignKey(User, on_delete=models.CASCADE)  # when the user gets deleted, his posts are also deleted

    # to make posts more desciptive
    def __str__(self):
        return self.title