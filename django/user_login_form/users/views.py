from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterationForm, LoginForm
from .models import User

def register(request):
	if request.method == 'POST':
		form = UserRegisterationForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Your account has been created successfully! you can login now.')
			form.save()
			return redirect('login')
	else:
		form = UserRegisterationForm()
	return render(request, 'users/register.html', {'form': form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			request.session['username'] = form.cleaned_data['username']
			request.session['password'] = form.cleaned_data['password']
			return redirect('blog-home')
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form})

def logout(request):
	request.session.flush()
	return redirect('blog-home')


def profile(request):
	try:
		username = request.session['username']
	except KeyError:
		messages.warning(request, "you must login first!")
		return redirect('login')
	user = User.objects.get(username=username)
	return render(request, 'users/profile.html', {'user': user, 'username': username})
