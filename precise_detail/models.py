from django.db import models



class Estimate(models.Model):
    name = models.CharField(max_length=100, default='unknown')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    bed = models.CharField(max_length=5, null=True, blank=True)
    bath = models.CharField(max_length=5, null=True, blank=True)
    sqft = models.CharField(max_length=20, null=True, blank=True)
    pets = models.CharField(max_length=5, null=True, blank=True)
    frequency = models.CharField(max_length=20, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    