from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Message
from django.contrib.auth.models import User
from .forms import MessageForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def roomlist(request):
    rooms = Room.objects.all().order_by('-updated')
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    room_messages =  Message.objects.filter(Q(text__icontains=q) |
                                            Q(room__name__icontains=q))
    
    context = {'rooms': rooms, 'room_messages': room_messages}
    return render(request, 'room/roomlist.html', context)

def delete_(request, pk):
    message = Message.objects.get(id=pk)
    context = {'message': message}
    if request.method == 'POST':
        message.delete()
        return redirect('roomlist')
    return render(request, 'room/delete.html', context)

def edit_(request, pk):
    message = Message.objects.get(id=pk)
    form = MessageForm(instance=message)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid:
            form.save()
            return redirect('roomlist')
    
    context = {'form': form}
    return render(request, 'room/edit.html', context)

def room_info(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room=room,
            text=request.POST.get('comment')
        )

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'room/room_info.html', context)

def user_profile(request, pk):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    room_messages =  Message.objects.filter(Q(text__icontains=q) |
                                            Q(room__name__icontains=q))
    user = User.objects.get(id=pk)
    all_rooms = Room.objects.all()
    all_messages = Message.objects.all()
    rooms = user.room_set.all()
    context = {'user': user, 'rooms': rooms,
     'room_messages': room_messages, 'all_rooms': all_rooms, 'all_messages': all_messages}
    return render(request, 'room/profile.html', context)

def roomlist_login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', user.id)
        else:
            return redirect('roomlist')

    context = {'page': page}
    return render(request, 'room/login_reg.html', context)