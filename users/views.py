from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # importing decorators
from .forms import UserRegisterForm

# Create your views here.

# in Django, python classes generate HTML forms for us
# some of them already exist (e.g. registration form)


def register(request):
    # checking if its a GET or a POST request
    if request.method == 'POST':
        # instanciates a user creation form with that post data
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # saving the user
            form.save()
            # validated form data will be in this form.cleaned_data dictionary
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # after succesfull account creation redirecting user to login page
            return redirect('login')
    else:
        # creating a blank instance form
        form = UserRegisterForm()
    # {'form': form }is so we could access the form from within the template
    # ('form' is a dictionary, and form is a variable)
    return render(request, 'users/register.html', {'form': form})

# python decorator | view user profile only if logged in
@login_required()
def profile(request):
    return render(request, 'users/profile.html')
