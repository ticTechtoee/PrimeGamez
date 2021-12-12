from django.forms import ModelForm, fields
from .models import page1

class page1Form(ModelForm):
    class Meta:
        model = page1
        fields = ['orderNumber','postCode',]