from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# The above class defines a model for a post, which includes fields for the title, text, date, time,
# and author of the post.
class Post(models.Model):
    title = models.CharField('Title post', max_length=35, unique=True)
    text = models.TextField('Text post', unique=True)
    date = models.DateField('Date post', default=timezone.now)
    time = models.TimeField('Time post', default=timezone.now)
    author = models.ForeignKey(
        User, verbose_name='Author', on_delete=models.CASCADE)

    # delete
    views = models.IntegerField('Number of views', default=1)
    likes = models.IntegerField('Number of likes', default=0)

    # The class "Meta" defines the verbose names for a post model.

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        """
        The function returns a string representation of a post object, including the title and author.
        :return: The `__str__` method is returning a string that includes the title and author of a
        post.
        """
        return f'New post is {self.title} by {self.author}'
