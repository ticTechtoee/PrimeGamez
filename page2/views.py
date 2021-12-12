from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request
from django.shortcuts import render, redirect
from page1.models import page1
from .forms import page2Form


def orders(request):

    page1data = page1.objects.all()
    context = {'data':page1data}
    return render(request, "page2/orders.html", context)

