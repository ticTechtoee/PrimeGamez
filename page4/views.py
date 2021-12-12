from django.shortcuts import render
from django.http import request
from django.shortcuts import render, redirect
from .models import page4
from .forms import page4Form


def index(request):
    form = page4Form()
    
    if request.method == 'POST':
        form = page4Form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, "page4/index.html", context)