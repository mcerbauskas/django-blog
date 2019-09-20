from django.shortcuts import render
from django.http import HttpResponse

#dummy data - list of dictionaries

posts = [
    {
        'author': 'MariusC',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '2019-09-19'
    },
    {
        'author': 'RubertM',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '2019-09-20'
    }
]

#function to handle the traffic from the home page of our blog
def home(request):
    #creating a dictionary with key 'posts'
    context = {
        'posts': posts
    }

    # vietoje return HttpResponse('<h1>Blog Home </h1>')
    # render returns http response in background
    # passing data from 'context' into the template and letting access it through the template
    return render(request, 'blog/home.html', context)

#adding 'about' route to the blog page
def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})


