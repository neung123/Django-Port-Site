from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('posts/', views.posts, name="posts"),
	path('post/<slug:slug>/', views.post, name="post"),
	path('profile/', views.profile, name="profile"),
]