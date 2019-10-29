from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# UserRegisterForm inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # adding additional fields to this form
    # EmailField() can take an argument that is called 'required'. Default required is set to True so leaving it empty
    email = forms.EmailField()

    # within Meta we specify what we want this model to interract with
    class Meta:
        # whenever this form validates its going to create a new User
        model = User
        # fields that want to be shown on the form
        fields = ['username', 'email', 'password1', 'password2']


# creating a model form which allows us to create a form that will work with a specific DB model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

