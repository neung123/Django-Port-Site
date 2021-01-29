from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('posts/', views.posts, name="posts"),
	path('experience', views.experience, name="experience"),
	path('profile/', views.profile, name="profile"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
]