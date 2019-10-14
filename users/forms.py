from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

