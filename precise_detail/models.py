from django.db import models



class Estimate(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    bed = models.IntegerField(null=True)
    bath = models.IntegerField(null=True)
    sqft = models.IntegerField(null=True)
    pets = models.IntegerField(null=True)
    frequency = models.IntegerField(null=True)
    
    def __str__(self):
        return self.last + ", " + self.first
    
    