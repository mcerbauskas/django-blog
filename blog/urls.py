from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    # leave it as an empy path as it's for a homepage, not admin page
    # PostListView class has to be converted into actual view 'as_view()'
    path('', PostListView.as_view(), name='blog-home'),
    # <int:pk> primary key, expecting only integer
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]