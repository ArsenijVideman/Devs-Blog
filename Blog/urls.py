from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from registration.views import UserRegistration
from django.conf import settings
from django.conf.urls.static import static

# The `urlpatterns` variable is a list of URL patterns that Django uses to route incoming requests to
# the appropriate view functions. Each element in the list represents a URL pattern and consists of a
# `path()` function call.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('all_articles.urls'), name='posts'),
    path('register/', UserRegistration.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/user.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/exit.html'), name='logout'),
    path('profile/', UserRegistration.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
