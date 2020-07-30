from django.urls import path
from .views import users, signup, login_user, profile, logout_user

app_name = 'users'
urlpatterns = [
    path('users', users, name='users'),
    path('signup', signup, name='signup'),
    path('login', login_user, name='login'),
    path('profile', profile, name='profile'),
    path('logout', logout_user, name='logout')
]
