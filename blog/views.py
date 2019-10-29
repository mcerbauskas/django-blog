from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse

# run a query on our Post model and pass in the data from sql instead
# function to handle the traffic from the home page of our blog
def home(request):
    # creating a dictionary with key 'posts'
    context = {
        'posts': Post.objects.all()
    }

    # instead of return HttpResponse('<h1>Blog Home </h1>')
    # render returns http response in background
    # passing data from 'context' into the template and letting access it through the template
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    # this tells our ListView what model to query in order to create a List
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering our posts by newest date at the top
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

# a view with a form where we create a new form
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', ]

#adding 'about' route to the blog page
def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})


