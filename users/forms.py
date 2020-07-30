from django.forms import ModelForm, CharField, PasswordInput
from django.contrib.auth.models import User
from .models import Customer


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('phone', 'address', 'membership')
