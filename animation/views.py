from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Animation
from .forms import AnimationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'animation/home.html')

def animations(request):
    animations = Animation.objects.all()
    q = request.GET.get('q') if request.GET.get('q') else ''
    animations = Animation.objects.filter(Q(name__icontains=q) | Q(year__icontains=q))
    counter = animations.count()
    context = {'animations': animations, 'counter': counter}
    return render(request, 'animation/animations.html', context)

def info(request, pk):
    animation = Animation.objects.get(id=pk)
    context = {'animation': animation}
    return render(request, 'animation/animation_info.html', context)

@login_required(login_url='login')
def edit(request, pk):
    animation = Animation.objects.get(id=pk)
    form = AnimationForm(instance=animation)

    # if request.user != animation.user:
    #     return HttpResponse('what the fuck bitch?!!')

    if request.method == 'POST':
        form = AnimationForm(request.POST, instance=animation)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {'form': form}
    return render(request, 'animation/edit.html', context)

@login_required(login_url='login')
def delete(request ,pk):
    animation = Animation.objects.get(id=pk)

    # if request.user != animation.user:
    #     return HttpResponse('what the fuck bitch?!!')
    
    if request.method == 'POST':
        animation.delete()
        return redirect('animations')
    context = { 'animation' :animation}
    return render(request, 'animation/delete.html', context)

@login_required(login_url='login')
def create(request):
    form = AnimationForm()
    if request.method == 'POST':
        form = AnimationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('animations')
    context = {'form': form}
    return render(request, 'animation/edit.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'the user does not exist!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('animations')
        else:
            messages.error(request, 'wrong username or password!')

    context = {'page': page}
    return render(request, 'animation/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def signupUser(request):
    page = 'signup'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse(request, 'what the fuck bitch??!')
            #messages.error(request, 'are you blind bitch?')
    context = {'page': page , 'form' : form}
    return render(request, 'animation/login.html', context)