from django.forms import ModelForm
from page1.models import page1

class page2Form(ModelForm):
    class Meta:
        model = page1
        fields = ['amount']