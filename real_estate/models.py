from django.db import models


class ApartmentForSelling(models.Model):
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    view = models.CharField(max_length=255)
    room_number = models.PositiveSmallIntegerField()
    bathrooms = models.CharField(max_length=255)
    cladding = models.CharField(max_length=255)
    floor = models.PositiveSmallIntegerField()
    property = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    is_sold = models.BooleanField(default=False)
    
class ApartmentForRenting(models.Model):
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    view = models.CharField(max_length=255)
    room_number = models.PositiveSmallIntegerField()
    bathrooms = models.CharField(max_length=255)
    cladding = models.CharField(max_length=255)
    floor = models.PositiveSmallIntegerField()
    renting_period = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    is_sold = models.BooleanField(default=False)
     
class ShopForSelling(models.Model):
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    property = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    is_sold = models.BooleanField(default=False)
    
class ShopForRenting(models.Model):
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    renting_period = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    is_sold = models.BooleanField(default=False)
       
class Land(models.Model):
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    property = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    is_sold = models.BooleanField(default=False)