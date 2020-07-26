from django.urls import path
from .views import users, register, login, profile, logout

app_name = 'users'
urlpatterns = [
    path('', users, name='users'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('logout', logout, name='logout')
]
