from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import HelpRequest, Event, users, Manager,Venue


# Create your views here.

@login_required(login_url='login')  # this will check if you are logged in or not
def home(request):
    return render(request,'index.html')


def signup(request):
    if request.method == "GET":

        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'signup.html', context=context)
    else:
        form = UserCreationForm(request.POST)

        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            print(user.id,user.username)
            user_data = users(username=user.username,password=user.password)
            user_data.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)


def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = { "form": form }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username,password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                "form": form
            }
            return render(request, 'login.html', context=context)


def signout(request):
    logout(request)
    #using django.contribs logouts the user
    return redirect('login')

@login_required(login_url='login')
def venues(request):
    return render(request,'venues.html')


@login_required(login_url='login')
def event(request):
    registered_managers = Manager.objects.filter(is_available='Available')
    venues= Venue.objects.all()
    if request.method == 'POST':
        event = Event()
        event.event_name = request.POST.get('eventName')
        event.event_type = request.POST.get('eventType')
        event.place_to_host = request.POST.get('placeToHost')
        event.venue_selection = request.POST.get('venueSelection')
        event.venue_details = request.POST.get('venueDetailsInput')
        event.date_of_event = request.POST.get('dateOfEvent')
        event.event_manager_name = request.POST.get('eventManagerName')
        event.phone_number = request.POST.get('phoneNumber')
        event.save()
        #All event details saves inside the event table
        return render(request, 'eventplan.html', {'registered_managers': registered_managers ,'venues':venues})  # Redirect to success page after saving
    else:
        return render(request, 'eventplan.html', {'registered_managers': registered_managers ,'venues':venues})

@login_required(login_url='login')
def mlist(request):
    registered_managers = Manager.objects.all()

    return render(request, 'mlist.html',{'registered_managers': registered_managers})

@login_required(login_url='login')
def booked_events(request):
    user = request.user
    # Get the currently logged-in user
    # Filter events where the event is registered by loged user
    BE = Event.objects.filter(event_name=user.username)
    return render(request, 'orders.html', {'BE': BE})


@login_required(login_url='login')
def help(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        help_text = request.POST.get('help')
        if username and email:
            # Saving the help request to the database
            help = HelpRequest.objects.create(username=username, email=email, help_text=help_text)
            help.save()
            #it saves the user query into the help table of the database
            alert_message = "Your query is submitted successfully."
            # Return the HttpResponse object
        return render(request, 'help.html', {'alert_message': alert_message})

    return render(request,'help.html')
