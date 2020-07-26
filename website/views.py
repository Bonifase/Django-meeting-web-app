from django.shortcuts import render


def home(request):
    template = 'website/home.html'
    return render(request, template)


def about(request):
    template = 'website/about.html'
    return render(request, template)
