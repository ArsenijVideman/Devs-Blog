from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from registration.views import UserRegistration


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('all_articles.urls'), name='posts'),
    path('register/', UserRegistration.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/user.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/exit.html'), name='logout'),
    path('profile/', UserRegistration.profile, name='profile'),
]
