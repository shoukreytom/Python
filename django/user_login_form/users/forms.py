from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import User

class UserRegisterationForm(forms.Form):
	username = forms.CharField(label='Username', min_length=4, max_length=40)
	email = forms.EmailField()
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=15)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, max_length=15)

	def clean_username(self):
		username = self.cleaned_data['username']
		re = User.objects.filter(username=username)
		if re.count():
			raise ValidationError('This username is already exists!')
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		re = User.objects.filter(email=email)
		if re.count():
			raise ValidationError('This email is already exists!')
		return email

	def clean_password2(self):
	 	password1 = self.cleaned_data['password1']
	 	password2 = self.cleaned_data['password2']
	 	if password1 and password2 and password1 != password2:
	 		raise ValidationError("Password don't match")
	 	return password2

	def save(self):
		user = User.objects.create(
			username=self.cleaned_data['username'],
			email=self.cleaned_data['email'],
			password=self.cleaned_data['password1']
		)
		return user



class LoginForm(forms.Form):
	username = forms.CharField(label='Username', min_length=4, max_length=40)
	password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=15)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			user = User.objects.get(username=username)
		except ObjectDoesNotExist:
			raise ValidationError("")
		return username

	def clean_password(self):
		password = self.cleaned_data['password']
		try:
			username = self.cleaned_data['username']
			user = User.objects.get(username=username)
		except (ObjectDoesNotExist, KeyError):
			raise ValidationError("username or password is wrong")
		if user.password != password:
			raise ValidationError("")
		return password
