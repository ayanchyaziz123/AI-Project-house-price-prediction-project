from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.
class Location(models.Model):
    location = models.CharField(primary_key=True, max_length=200)
class Society(models.Model):
    society = models.CharField(primary_key=True, max_length=200)
class Area(models.Model):
    areaType = models.CharField(primary_key=True, max_length=200)
class House(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    areaType = models.ForeignKey(Area, on_delete=models.CASCADE)
    houseId = models.AutoField(primary_key=True, auto_created=True)
    house_title = models.CharField(max_length=200)
    house_descriptions = models.TextField()
    size = models.CharField(max_length=200)
    total_sqrft = models.IntegerField()
    bathroom = models.IntegerField()
    balcony = models.IntegerField()
    price = models.FloatField()
    availability = models.CharField(max_length=200)
    post_creatDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    house_image =  models.ImageField(blank=False, null=False)


