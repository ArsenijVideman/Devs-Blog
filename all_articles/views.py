# The above code defines two classes, Home and About, each with a single method that renders a
# specific HTML template.
from django.shortcuts import render
from .models import Post


# The above class represents a home page with a list of news posts and an info page with the same list
# of news posts.
class Home:

    info_page = {
        'posts': Post.objects.all(),
        'title': 'Home',
    }

    def home(request):
        template_name = 'blog/home.html'
        return render(request, template_name, context=Home.info_page)


# The above class defines an asynchronous function called "about" that renders an HTML template named
# "about.html" with the information stored in the "info_page" dictionary.
class About:

    info_page = {
        'title': 'About',
    }

    def about(request):
        template_name = 'blog/about.html'
        return render(request, template_name, context=About.info_page)


# The class `MyPosts` contains a list of posts with their titles, texts, dates, times, and authors, as
# well as an info page with the list of posts and a title. The `my_posts` method returns a rendered
# template with the info page when called.
class MyPosts:

    info_page = {
        'posts': Post.objects.all(),
        'title': 'My Posts',
    }

    def my_posts(request):
        template_name = 'blog/my_posts.html'
        return render(request, template_name, context=MyPosts.info_page)
