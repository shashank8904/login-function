from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "authentication/index.html") 

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        email = request.POST.get('email','')
        pass1 = request.POST.get('pass1','')
        pass2 = request.POST.get('pass2','')

        if pass1 != pass2:
            return HttpResponse("your password is not matching ")
        else:

         my_user = User.objects.create_user(username, email, pass1)
         my_user.first_name = fname
         my_user.last_name = lname

         my_user.save()

         messages.success(request,"Your Account has been Successfully Created.")

        

         return redirect('signin')


    return render(request, "authentication/signup.html")

def signin(request):

    if request.method =="POST":
        username = request.POST['username']
        pass1 = request.POST.get('pass1','')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')
    

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

