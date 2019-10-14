from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# inheriting from models.Model


class Profile(models.Model):
    # 1:1 relationship with the User model
    # 'on_delete' tells us what we want to do with the profile is the User gets deleted
    # CASCADE - if user is deleted also delete his profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default image for any user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

# returning how we want this to be displayed in our ORM
    def __str__(self):
        return f'{self.user.username} Profile'
