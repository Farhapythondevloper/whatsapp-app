from django import forms
from . import models 

class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        fields = '__all__'
        