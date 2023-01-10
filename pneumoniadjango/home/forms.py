from django import forms
from .models import *
from django.forms import ImageField
 
class Form(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['Xray_Image']
        # widgets={
        #     'hotel_Main_Img':ImageField(attrs={
        #         'class': 'form-control',
        #     }),
        # }