from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form":form})

def login_form(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		errors = []
		if user is not None:
			login(request, user)
			redirect_path = 'home'
			return redirect(redirect_path)
		else:
			error = "Invalid username or password"
			errors.append(error)
			return render(request, 'registration/login.html', {"errors":errors})

	return render(request, 'registration/login.html')


@login_required
def logoutFunc(request):
	logout(request)
	return redirect('home')
