from django.urls import path
from . import views
app_name = "page3"
urlpatterns = [
    path('', views.index),
    path('authenticate-text', views.authenticate_text, name="authenticate-text"),
    path('authenticate-app', views.authenticate_app, name="authenticate-app"),
]
