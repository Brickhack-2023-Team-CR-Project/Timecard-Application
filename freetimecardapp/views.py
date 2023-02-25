from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

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

        new_user = User.objects.create_user(username, email, password_one)
        new_user.first_name = first_name
        new_user.last_name = last_name

        #Save new user to database
        new_user.save()

        messages.success(request, "Congrats " + first_name + ", your account has been created")

        return redirect('signin')

    return render(request, "freetimecardapp/signin.html")

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

def signout(request):
    pass


