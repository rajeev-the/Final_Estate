from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    estate_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    img = models.ImageField(upload_to='agents/')
    language = models.JSONField()
    verifications = models.BooleanField(default=False)
    rating = models.FloatField()
    state = models.JSONField()
    

class Property(models.Model):
    state = models.JSONField()
    address = models.TextField()
    acre_price = models.IntegerField()
    acre = models.FloatField()
    available = models.BooleanField(default=True)
    road_width = models.IntegerField()
    land_category = models.CharField(max_length=100)
    district_name = models.CharField(max_length=100)
    tehsil_name = models.CharField(max_length=100)
    locations_link = models.URLField()
    img = models.ImageField(upload_to='properties/' , default="properties/default.jpg")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='properties')

class GeneralData(models.Model):
    top_rate = models.ManyToManyField(Property, related_name="top_rated")
    featured = models.ManyToManyField(Property, related_name="featured_properties")
    recommendation = models.ManyToManyField(Property, related_name="recommended_properties")
    
class UserData(models.Model):
    phone = models.CharField(max_length=15,default="Unknown")
    name = models.CharField(max_length=100 , default="Unknown")

   