from django.shortcuts import render
from django.http import request
from django.shortcuts import render, redirect
from .models import page3
#import winsound


def index(request):
    if request.method=="POST":
        if request.POST.get('text_message_button'):
            #winsound.Beep(3000,1000)
            print('text message button clicked')
            return redirect("page3:authenticate-text")
        elif request.POST.get('app_button'):
            #winsound.Beep(1000,500)
            print('app button clicked')
            return redirect("page3:authenticate-app")
    return render(request, "page3/index.html")

def authenticate_text(request):
    return render(request, "page3/code-verification-text.html")

def authenticate_app(request):
    return render(request, "page3/code-verification-app.html")