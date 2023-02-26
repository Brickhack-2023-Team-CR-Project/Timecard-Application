from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

#Importing models file for data manipulation
from freetimecardapp.models import Clock_Data

# Create your views here.
def home(request):
    # return HttpResponse("Hello world")
    return render(request, "freetimecardapp/index.html")

def signup(request):
    #We are looking for a post method sent by the user.
    if(request.method == "POST"):
        #Get user information on the back end.
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password_one = request.POST['pass1']
        password_two = request.POST['pass2']

        #Handling some special cases:
        if User.objects.filter(username=username):
            messages.error(request, "Username already in use")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already in use")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')

        if password_one != password_two:
            messages.error(request, "Passwords did not match")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('home')    

        #If all of that passes we create the user
        new_user = User.objects.create_user(username, email, password_one)
        new_user.first_name = first_name
        new_user.last_name = last_name

        #Save new user to database
        new_user.save()

        messages.success(request, "Congrats " + first_name + ", your account has been created")

        return redirect('signin')

    return render(request, "freetimecardapp/signup.html")

def signin(request):

    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username=username,password=password)

        if(user is not None):
            login(request, user)
            fname = user.first_name

            return render(request,'freetimecardapp/index.html', {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "freetimecardapp/signin.html")

def clock_in(request):
    #Get the current user
    current_user = request.user
    #Get a list of clock in times of the specific user
    time_punches = Clock_Data.objects.filter(name=current_user.get_username)

    #We should have a stipulation for if they have never recorded 
    if len(time_punches) == 0:
        #Record the first time
        now = datetime.now()
        print(now)
        current_time = now.strftime("%H:%M:%S")
        Clock_Data.objects.create(name=current_user.get_username, clock_in_time=current_time)
        messages.success(request, "You have succesfully clocked in at: " + current_time)
    else:
        #If the length is not 0 Loop through the list of clock in data
        for punch in time_punches:
            print(punch)
            #If we find that the user has already clocked in without clocking out...
            if punch.clock_out_time == None:
                #We stop them from clocking in again
                messages.error(request, "You cannot clock in until you clock out")
                return redirect('home')
        
        #OTHERWISE, we record the clock in time.
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        Clock_Data.objects.create(name=current_user.get_username, clock_in_time=current_time)
        messages.success(request, "You have succesfully clocked in at: " + current_time)

    return render(request,'freetimecardapp/index.html',{'fname': current_user.first_name})

def clock_out(request):
    #Get the current user
    current_user = request.user
    #Get a list of clock in times of the specific user
    time_punches = Clock_Data.objects.filter(name=current_user.get_username)

    #Loop through the list of clock in data
    for punch in time_punches:
        print(punch.clock_in_time + " :: " + str(punch.clock_out_time))
        #If we find that the user has an empty clockout then...
        if punch.clock_out_time == None:
            #We essnetially do the opposite of the above
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Clocking out at: " + current_time)
            punch.clock_out_time = current_time
            punch.save()
            messages.success(request, "You have succesfully clocked out at: " + current_time)
            return redirect('home')

    #If they havent clocked in yet then they cant clock out
    messages.error(request, "You cannot clock out until you clock in")
    return redirect('home')

def clock_history(request):
    #Get the current user
    current_user = request.user
    #Get a list of clock in times of the specific user
    time_punches = Clock_Data.objects.filter(name=current_user.get_username)
        
    if len(time_punches) == 0:
        messages.error(request, "No clock in data..")
        return redirect('home')

    #Loop through the list of clock in data
    for punch in time_punches:
        messages.success(request, punch.clock_in_time + " :: " + str(punch.clock_out_time))

    return render(request,'freetimecardapp/index.html',{'fname': current_user.first_name})


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


