from django.db import models

class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.EmailField()
	password = models.CharField(max_length=15)

	def __str__(self):
		return self.username


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default="default.jpg", upload_to="profile_pics")

	def __str__(self):
		return f"<Profile {self.user.username}>"
