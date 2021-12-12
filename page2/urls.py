from django.urls import path
from . import views
app_name = 'page2'

urlpatterns = [
    path('', views.orders, name="orders"),
]
