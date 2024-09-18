from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Player


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def all_player_index(req):
    players = Player.objects.all()
    return render(req, 'players/index.html', {'players': players})

def my_player_index(req):
    players = Player.objects.filter(user=req.user)
    return render(req, 'users/index.html', {'players': players})

def player_detail(req, player_id):
    player = Player.objects.get(id=player_id)
    return render(req, 'players/detail.html', {
        'player': player,
    })