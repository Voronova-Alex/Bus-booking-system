from django.shortcuts import render
from .models import Message


def chat(request):
    return render(request, 'chat.html')


def room(request, room_name):
    username = request.GET.get('username')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'room.html',
                  {'room_name': room_name, 'username': username, 'messages': messages, 'room_url': None, })
