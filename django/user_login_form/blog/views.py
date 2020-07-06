from django.shortcuts import render

def home(request):
	try:
		username = request.session['username']
	except KeyError:
		username = None
	return render(request, 'blog/home.html', {'username': username})
