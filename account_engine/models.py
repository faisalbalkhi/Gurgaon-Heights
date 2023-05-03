from django.db import models
from django_extensions.db.fields import AutoSlugField


# Create your models here.

class Amenities(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Property(models.Model):
    PROPERTY_TYPECHOICES = [
        ('R', 'RESIDENTIAL'),
        ('C', 'COMMERCIAL'),
    ]
    property_type= models.CharField(max_length=1, choices=PROPERTY_TYPECHOICES)
    title = models.CharField(max_length=200)
    amenities = models.ManyToManyField(Amenities, related_name='residential_amenities')
    location = models.CharField(max_length=200)
    area_min = models.IntegerField()
    area_max = models.IntegerField()
    price_min = models.IntegerField()
    price_max = models.IntegerField()
    psf = models.IntegerField("Per Sq. Ft")
    status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Residential_image')
    rating = models.IntegerField()
    slug = AutoSlugField(populate_from=['title'], null=True, blank=True)


    def __str__(self):
        return self.title
    