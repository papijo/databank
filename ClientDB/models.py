from django.db import models

from django.db import models
from django.urls import reverse #Used to generate URLS by reversing the URL Patterns
from django.db.models.fields.files import ImageField
from PIL import Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User

class Sector(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectors'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("client-organisation_by_sector", args=[self.slug])
    
    

class State(models.Model):
    name = models.CharField(max_length= 200)
    slug = models.SlugField(max_length = 200)

    class Meta:
        ordering = ('name', )
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("client-organisation_by_state", args=[self.slug])
    

class AreaOffice(models.Model):
    name = models.CharField(max_length= 200)
    slug = models.SlugField(max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = 'Area office'
        verbose_name_plural = 'Area Offices'

    def get_absolute_url(self):
        return reverse("client-organisation_by_areaoffice", args=[self.slug])
      

class Type(models.Model):
    name = models.CharField(max_length= 200)
    slug = models.SlugField(max_length = 200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'type'
        verbose_name_plural = 'types'
    
    def get_absolute_url(self):
        return reverse("client-organisation_by_type", args=[self.slug])
    


class ClientOrganisation(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length= 200)
    CAC_Number = models.IntegerField(primary_key= True)
    email = models.EmailField(unique=True)
    logo = models.ImageField(upload_to= 'uploads/client')
    sector = models.ForeignKey('Sector', on_delete=models.SET_NULL, null=True)
    area_of_Specialisation = models.CharField(max_length= 200)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    area_Office = models.ForeignKey('AreaOffice', on_delete=models.SET_NULL, null=True)
    date_formed = models.DateField(null=False)
    staff_Strength = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'CAC_Number']
        permissions = (("can_edit", "Set Organisation for Editing"),)

    def get_absolute_url(self):
        return reverse("client-organisation-detail", args=[str(self.CAC_Number)])
    
    
    def logo_image(self):
        return format_html('<img src = "/media/%s" width="100" height="100" />' % (self.logo))
        #return mark_safe('<img src = "/media/%s" width="100" height="100" />' % (self.logo))
       
    logo_image.short_description = 'Logo'
    logo_image.allow_tags = True
