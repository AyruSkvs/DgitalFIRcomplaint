from django.db import models

# Create your models here.
class memberdata(models.Model):
    fullname=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    age = models.BigIntegerField(default=None)
    phone = models.BigIntegerField(default=None)
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    mandal = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50)
    pin_code = models.BigIntegerField(default=None)
    Near_police_station = models.CharField(max_length=20)
    text_area = models.CharField(max_length=8000)




