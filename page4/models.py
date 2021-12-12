from django.db import models

class page4(models.Model):
    order_number = models.CharField(max_length=200)
    address_detail = models.CharField(max_length=200)