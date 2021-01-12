from django.db import models


class GetInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    aadhar = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    hotelname = models.CharField(max_length=30)
    datetime = models.CharField(max_length=30)





