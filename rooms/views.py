from django.shortcuts import render
from .models import Room


def rooms(request):
    template = 'rooms/rooms.html'
    all_rooms = Room.objects.all()
    return render(request, template, {'rooms': all_rooms})


def room(request, id):
    template = 'rooms/room.html'
    room_obj = Room.objects.get(pk=id)
    return render(request, template, {'room': room_obj})