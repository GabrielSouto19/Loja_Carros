from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def register_view(request):
    if request.method == "GET":
        user_form = UserCreationForm()
    else:
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    return render(request,"register.html",{"user_form":user_form})


def login_view(request):
    if request.method == "GET":
        login_form = AuthenticationForm()
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request=request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("cars_list")
        else:
            login_form = AuthenticationForm()
    return render(request,"login.html",{"login_form":login_form})
    
def logout_view(request):
    logout(request=request)
    return redirect("cars_list")