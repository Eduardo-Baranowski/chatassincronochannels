from django.views.decorators.csrf import csrf_exempt


# chat/views.py
from django.shortcuts import render

@csrf_exempt
def index(request):
    return render(request, 'chat/index.html', {})

@csrf_exempt
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
