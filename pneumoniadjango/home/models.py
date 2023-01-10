from django.db import models
# models.py
class Image(models.Model):
    #name = models.CharField(max_length=50)
    Xray_Image= models.ImageField(
       upload_to=''
    )