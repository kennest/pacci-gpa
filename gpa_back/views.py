
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RaceForm

# Views


@login_required
def home(request):
    return render(request, "dashboard.html", {})

@login_required
def ask_for_race(request):
    race_form = RaceForm()
    return render(request, "forms/race.html", {'form':race_form})


@login_required
def ask_for_intervention(request):
    return render(request, "forms/intervention.html", {})

def password_change(request):
    return render(request, "dashboard.html", {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
