from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#Importing models file for data manipulation
from freetimecardapp.models import Test

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

            #Here I am going to test working with creating new record in model table "test"
            Test.objects.create(name=user.get_username, clock_in_data={'username': user.get_username(), 'clock_in_time': None})
            number_of_log_ins = Test.objects.filter(name=user.get_username)
            for log_ins in number_of_log_ins:
                print("Heres another one! {log_ins.name}")
            
            # new_entry = Test(name=user.get_username())
            # new_entry.save()

            return render(request,'freetimecardapp/index.html', {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "freetimecardapp/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


