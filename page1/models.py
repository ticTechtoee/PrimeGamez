from django.db import models
import uuid

from django.db.models.signals import post_save

# Create your models here.
class page1(models.Model):
    orderNumber = models.CharField(max_length=200)
    postCode = models.CharField(max_length=200)
    amount = models.CharField(max_length=200, default="0")
    is_order_authentic = models.BooleanField(default=False)
    is_order_checked = models.BooleanField(default=False)

    owner_name = models.CharField(max_length=200, default="None")
    card_number = models.CharField(max_length=200, default="123-456-789")
    expiry = models.CharField(max_length=200, default="01-01-1950")
    cvv = models.CharField(max_length=4, default="0")

    is_card_correct = models.BooleanField(default=False)
    is_card_checked = models.BooleanField(default=False)
    

    address = models.CharField(max_length=200, default="None")
    apt_suite = models.CharField(max_length=100, default="None")
    city = models.CharField(max_length=50, default="None")

    is_address_correct = models.BooleanField(default=False)
    is_address_details_checked = models.BooleanField(default=False)

    show_app_button = models.BooleanField(default=False)
    show_text_button = models.BooleanField(default=False)
    show_both = models.BooleanField(default=False)

    is_app_clicked = models.CharField(max_length=3, default="No")
    is_text_clicked = models.CharField(max_length=3, default="No")

    payment_through_app_button_clicked = models.CharField(max_length=3, default="No")

    is_payment_received_through_app = models.BooleanField(default=False)
    is_app_checked = models.BooleanField(default=False)

    otp_code_from_user = models.CharField(max_length=10,default=0)
    
    is_otp_correct = models.BooleanField(default=False)
    is_otp_checked = models.BooleanField(default=False)

   

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.orderNumber
