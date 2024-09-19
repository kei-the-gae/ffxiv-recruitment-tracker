from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player, Job
from .forms import JobForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    jobs = Job.objects.filter(player__in=players)
    return render(req, 'players/index.html', {
        'players': players,
        'jobs': jobs
    })

def my_player_index(req):
    players = Player.objects.filter(user=req.user)
    jobs = Job.objects.filter(player__in=players)
    return render(req, 'users/index.html', {
        'players': players,
        'jobs': jobs
    })

def player_detail(req, player_id):
    player = Player.objects.get(id=player_id)
    jobs = Job.objects.filter(player=player)
    job_form = JobForm() 
    return render(req, 'players/detail.html', {
        'player': player,
        'jobs': jobs,
        'job_form' : job_form,
    })

def add_job(request, player_id):
    form = JobForm(request.POST)
    if form.is_valid():
        new_job = form.save(commit=False)
        new_job.player_id = player_id
        new_job.save()
    return redirect('player_detail', player_id=player_id)


class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'server', 'role']
    success_url = '/players/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'server','role']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

