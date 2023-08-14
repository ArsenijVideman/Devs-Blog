# This code is defining the URL patterns for a Django application.
from django.urls import path
from . import views

# The `urlpatterns` variable is a list of URL patterns for a Django application. Each URL pattern is
# defined using the `path()` function from the `django.urls` module.
urlpatterns = [
    path('', views.Home.home, name='home'),
    path('about/', views.About.about, name='about'),
    path('my_posts/', views.MyPosts.my_posts, name='my_posts'),
]
