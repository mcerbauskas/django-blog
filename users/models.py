from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

    # overriding the save method, gets run after model is saved
    # a method that already exist in parent class, but we're creating our own to add functionality
    def save(self):
        super().save()
        # grabbing the image that is saved and resizing it
        # opens the image of current instance
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            # this is a touple
            output_size = (300, 300)
            img.thumbnail(output_size)
            # saving it to the same path to override large image
            img.save(self.image.path)


