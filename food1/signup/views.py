from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate

# Create your views here.
def signup(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("index")    
    else:
        form = SignupForm()


    form = SignupForm()
    return render(response, "signup/signup.html", {"form": form})
