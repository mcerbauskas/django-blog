# signal fired when object is saved
from django.db.models.signals import post_save
# user model is the 'sender'
from django.contrib.auth.models import User
# the receiver
from django.dispatch import receiver
from .models import Profile

# when a user is saved, then send this signal. Signal will be received by this receiver/
# this receiver is the 'create_profile' function (takes all arguments that our 'post_save' signal passed to it)
@receiver(post_save, sender=User)
# **kwargs accepts any additional keyword arguments at the end of the function
def create_profile(sender, instance, created, **kwargs):
    # if that user was created, create a profile object
    if created:
        Profile.objects.create(user=instance)


# saves our profile every time the User object gets saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # 'instance' is the user
    instance.profile.save()
