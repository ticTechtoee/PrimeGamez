from django.db import models
import uuid

from django.db.models.signals import post_save

# Create your models here.
class page1(models.Model):
    orderNumber = models.CharField(max_length=200)
    postCode = models.CharField(max_length=200)
    amount = models.CharField(max_length=200, default="0")
    is_order_authentic = models.BooleanField(default=False)

    owner_name = models.CharField(max_length=200, default="None")
    card_number = models.CharField(max_length=200, default="123-456-789")
    expiry = models.CharField(max_length=200, default="01-01-1950")
    cvv = models.CharField(max_length=3, default="0")

    is_card_correct = models.BooleanField(default=False)
    is_address_correct = models.BooleanField(default=False)

    address_details = models.CharField(max_length=200, default="0")

    is_otp_sent = models.BooleanField(default=False)
    otp_code_from_user = models.CharField(max_length=10,default=0)
    is_otp_correct = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.orderNumber

def orderUpdated(sender, instance, created, **kwargs):
    print('Order Updated!')


post_save.connect(orderUpdated, sender=page1)
