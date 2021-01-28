from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import pyrebase

config = {
    'databaseURL': "https://fir-port-website-default-rtdb.firebaseio.com/",
    'apiKey': "AIzaSyA2qoXX5Pm_98GzFrWlYzVGgSpsQDP_OKw",
    'authDomain': "fir-port-website.firebaseapp.com",
    'projectId': "fir-port-website",
    'storageBucket': "fir-port-website.appspot.com",
    'messagingSenderId': "150297746462",
    'appId': "1:150297746462:web:0b9933610aee1f7c3e620f",
    'measurementId': "G-XY9BQDMRQX"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def sendMsg(request):
    if request.method == 'POST':
        import time
        from datetime import datetime, timezone
        import pytz

        tz = pytz.timezone('Asia/Bangkok')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        milisec = int(time.mktime(time_now.timetuple()))

        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "subject": subject,
            "message": message,
        }
        db.child("msg").push(data)
    return

# Create your views here.

def index(request):
    sendMsg(request)
    return render(request, 'base/index.html')

def profile(request):
    return render(request, 'base/profile.html')

def about(request):
    return render(request, 'base/about.html')

def post(request):
    sendMsg(request)
    return render(request, 'base/post.html')

def posts(request):
    return render(request, 'base/posts.html')