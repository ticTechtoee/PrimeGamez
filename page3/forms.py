from django.forms import ModelForm
from .models import page3

class page3Form(ModelForm):
    class Meta:
        model = page3
        fields = '__all__'