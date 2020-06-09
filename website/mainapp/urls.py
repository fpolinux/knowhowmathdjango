from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='knowhowmath-home'),
	path('about/', views.about, name='knowhowmath-about'),
	path('enrol/', views.enrol, name='knowhowmath-enrol'),
	path('courses/', views.courses, name='knowhowmath-courses'),
]