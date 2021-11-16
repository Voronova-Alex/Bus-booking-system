from django.shortcuts import render
from transliterate import translit
from .models import Message


def chat(request):
    return render(request, 'chat.html')


def room(request, room_name):
    room_name = translit(room_name, "ru", reversed=True)
    username = request.GET.get('username')
    messages = Message.objects.filter(room=room_name)[0:25]
    print(room_name)

    return render(request, 'room.html',
                  {'room_name': room_name, 'username': username, 'messages': messages, 'room_url': None, })
