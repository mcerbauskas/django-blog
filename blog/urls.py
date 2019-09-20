from django.urls import path
from . import views

urlpatterns = [
    #leave it as an empy path as it's for a homepage, not admin page
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]