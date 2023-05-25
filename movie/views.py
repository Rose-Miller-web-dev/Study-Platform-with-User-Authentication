from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def cast(request):
    return render(request, 'movie/cast.html')

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'yo bitch!')
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cast')
    context = {'page': page}
    return render(request, 'movie/login_signup.html', context)

def logoutUser(request):
    logout(request)
    context = {}
    return render(request, 'movie/useful.html', context)

def signupUser(request):
    page = 'signup'
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid :
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect ('cast')
        else :
            return HttpResponse(request, 'what the fuck bitch??!')
        
    context = {'page': page}
    return render(request, 'movie/login_signup.html', context)

