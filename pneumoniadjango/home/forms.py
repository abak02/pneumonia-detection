from django import forms
from .models import *
from django.forms import ImageField
 
class HotelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['hotel_Main_Img']
        # widgets={
        #     'hotel_Main_Img':ImageField(attrs={
        #         'class': 'form-control',
        #     }),
        # }