from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def register_view(request):
    if request.method == "GET":
        user_form = UserCreationForm()
    else:
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("cars_list")
    return render(request,"register.html",{"user_form":user_form})


def login_view(request):
    login_form = AuthenticationForm()
    return render(request,"login.html",{"login_form":login_form})
    