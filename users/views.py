from django.shortcuts import render


def users(request):
    template = 'users/users.html'
    return render(request, template)


def register(request):
    template = 'users/register.html'
    return render(request, template)


def login(request):
    template = 'users/login.html'
    return render(request, template)


def profile(request):
    template = 'users/profile.html'
    return render(request, template)


def logout(request):
    template = 'users/logout.html'
    return render(request, template)
