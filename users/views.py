from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import Customer


@login_required
def users(request):
    template = 'users/users.html'
    return render(request, template)


def signup(request):
    template = 'users/signup.html'
    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        # Check to see the form is valid
        if user_form.is_valid():
            # Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            return redirect('website:home')
        else:
            print(user_form.errors)
            return render(request, template, {'user_form': user_form})

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, template, {'user_form': user_form})


def login_user(request):
    template = 'users/login.html'

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return redirect('website:home')
            else:
                # If account is not active:
                message = "Your account is not active."
                return render(request, template, {'message': message})
        else:
            message = "Invalid login details supplied."
            return render(request, template, {'message': message})

    else:
        # Nothing has been provided for username or password.
        return render(request, template)


@login_required
def profile(request):
    template = 'users/profile.html'
    users = Customer.objects.all()
    return render(request, template, {'users': users})


@login_required
def logout_user(request):
    logout(request)
    return redirect('website:home')



