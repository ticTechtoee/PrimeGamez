from django.forms import ModelForm
from .models import page4

class page4Form(ModelForm):
    class Meta:
        model = page4
        fields = '__all__'