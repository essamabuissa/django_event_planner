from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import Event , Booking
from .forms import UserSignup, UserLogin, EventCreateForm
from django.contrib import messages
from datetime import datetime
from django.db.models import Q



def home(request):
    return render(request, 'home.html')

class Signup(View):
    form_class = UserSignup
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, "You have successfully signed up.")
            login(request, user)
            return redirect("home")
        messages.warning(request, form.errors)
        return redirect("signup")


class Login(View):
    form_class = UserLogin
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                messages.success(request, "Welcome Back!")
                return redirect('event-list')

            messages.warning(request, "Wrong email/password combination. Please try again.")
            return redirect("login")
        messages.warning(request, form.errors)
        return redirect("login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect("login")

#Create Event View:

def EventCreate(request):
    if request.user.is_anonymous:
        return redirect('login')

    form = EventCreateForm()
    if request.method == "POST":
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save(commit = False)
            event.organizer = request.user
            event.save()
            messages.success(request , "Event Successfully Created!")
            return redirect('dashboard') # did not do it yet (create list)
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)


#List Of Events View:
def EventList(request):
    events = Event.objects.filter(date__gt = datetime.today())
    query = request.GET.get("q")
    if query:
        events = events.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)|
            Q(organizer__username__icontains=query)
            ).distinct()
    context = {
        "events" : events,
    }
    return render(request,'list.html',context)

#Event Details View:
def EventDetail(request , event_id):
    event = Event.objects.get(id = event_id)
    context = {
    "event" : event,
    }
    return render(request,'detail.html',context)

#Event Update View:
def EventUpdate(request,event_id):
    event_obj = Event.objects.get(id = event_id)
    form = EventCreateForm(instance = event_obj)
    if request.method == "POST":
        form = EventCreateForm(request.POST , instance = event_obj)
        if form.is_valid():
            form.save()
            messages.success(request , "Event Successfully Updated!")
            return redirect('event-detail',event_id) # did not do it yet (create list)
    context = {
        "form":form,
        "event": event_obj
    }
    return render(request, 'update.html', context)

#Event Delete View:
def EventDelete(request,event_id):
    event = Event.objects.get(id = event_id)

    event.delete()
    messages.success(request,"Event Successfully Deleted!")
    return redirect('event-list')

#Event Dashboard for the organizer:
def EventDashboard(request):
    if request.user.is_anonymous:
        redirect('login')
    events = Event.objects.filter(organizer = request.user)

    context = {
    "events" : events
    }

    return render(request,"dashboard.html",context)
