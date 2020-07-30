from django.urls import path
from .views import plans, plan, join, checkout, unsubscribe 

app_name = 'plans'
urlpatterns = [
    path('', plans, name='plans'),
    path('register', plan, name='plan'),
    path('join', join, name='join'),
    path('checkout', checkout, name='checkout'),
    path('unsubscribe', unsubscribe, name='unsubscribe')
]