from django.db import models
# models.py
class Image(models.Model):
    #name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='')