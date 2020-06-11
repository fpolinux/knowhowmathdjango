from django.shortcuts import render

def home(request):
	return render(request, 'mainapp/home.html')

def about(request):
	return render(request, 'mainapp/about.html', {'title': 'About'})

def enrol(request):
	return render(request, 'mainapp/enrol.html', {'title': 'Enrol'})

def courses(request):
	return render(request, 'mainapp/courses.html', {'title': 'Courses'})
