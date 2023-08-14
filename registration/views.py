from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class UserRegistration:

    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    request, f'{username} registered successfully!')
                return redirect('home')
        else:
            form = UserRegisterForm()

        template_name = 'registration/registration.html'
        return render(request,
                      template_name,
                      {'form': form,
                       'title': 'Register'}
                      )

    @login_required
    def profile(request):
        template_name = 'registration/profile.html'

        return render(request,
                      template_name)
