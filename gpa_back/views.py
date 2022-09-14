


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import group_required
from .forms import RaceForm,InterventionForm
from django.contrib import messages
from django.http import HttpRequest
from .models import Intervention,Race
# Views


@login_required
def home(request:HttpRequest):
    messages.add_message(request, messages.INFO,  'Bienvenue, %s ' % request.user.username)
    if request.user.is_authenticated:
        if bool(request.user.groups.filter(name="RESPONSABLE")) | request.user.is_superuser:
            races_pending= Race.objects.filter(status="PENDING").all()
            interventions_pending= Intervention.objects.filter(status="PENDING").all()
            context={"races": races_pending,'interventions':interventions_pending}
            template="dashboard.html"
            print("ACCOUNTABLE CTX :{}".format(context))
            return render(request, template, context)
    else:
        template="dashboard.html"
        context={}
        print("NOT ACCOUNTABLE CTX :{}".format(context))
        return render(request, template, context)

@login_required
@group_required("CHEF PROJET")
def ask_for_race(request:HttpRequest):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RaceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.cleaned_data["status"]="PENDING"
            form.save()
            messages.add_message(request, messages.SUCCESS,  'Demande de Course enregistrée.')
            return redirect('ask-for-race')
        else:
            messages.add_message(request, messages.ERROR,  form.errors)
            return redirect('ask-for-race')
    # if a GET (or any other method) we'll create a blank form
    else:
        race_form = RaceForm()
    return render(request, "forms/race.html", {'form':race_form})


@login_required
@group_required("COURSIER")
def ask_for_intervention(request:HttpRequest):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InterventionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.cleaned_data["status"]="PENDING"
            form.save()
            messages.add_message(request, messages.SUCCESS,  'Demande d\'intervention enregistrée.')
            return redirect('ask-for-intervention')
        else:
            messages.add_message(request, messages.ERROR,  form.errors)
            return redirect('ask-for-intervention')
    # if a GET (or any other method) we'll create a blank form
    else:
        intervention_form = InterventionForm()
    return render(request, "forms/intervention.html", {'form':intervention_form})

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
