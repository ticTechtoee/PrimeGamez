from django.db import models

class page3(models.Model):
    is_textMessageButton_clicked = models.BooleanField(default=False)
    is_appMessageButton_clicked = models.BooleanField(default=False)
