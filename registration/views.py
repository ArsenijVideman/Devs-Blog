from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class UserRegistration:

    def register(request):
        """
        The `register` function handles user registration by validating and saving the registration form
        data, displaying a success message, and redirecting to the home page.

        :param request: The request object represents the HTTP request made by the user. It contains
        information such as the user's browser, IP address, and any data sent with the request
        :return: a rendered HTML template with the registration form and a title.
        """
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
        """
        The above function is a view function for rendering the user's profile page, which requires the
        user to be logged in.

        :param request: The request object represents the HTTP request that the user made to access the
        view. It contains information about the user's request, such as the URL, headers, and any data
        sent with the request
        :return: the rendered profile.html template.
    """

        if request.method == 'POST':
            profile_form = ProfileImageForm(
                request.POST, request.FILES, instance=request.user.profile)
            update_user_form = UserUpdateForm(
                request.POST, instance=request.user)

            if profile_form.is_valid() and update_user_form.is_valid():
                update_user_form.save()
                profile_form.save()
                messages.success(
                    request, f"User updated successfully")
                return redirect('profile')

        else:
            profile_form = ProfileImageForm(instance=request.user.profile)
            update_user_form = UserUpdateForm(instance=request.user)

        template_name = 'registration/profile.html'
        info_page = {
            'profile_form': profile_form,
            'update_user_form': update_user_form
        }

        return render(request,
                      template_name,
                      info_page
                      )
