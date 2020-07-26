from django.urls import path
from .views import rooms, room

app_name = 'rooms'
urlpatterns = [
    path('rooms', rooms, name='rooms'),
    path('rooms/<int:id>', room, name='room_detail')
]
