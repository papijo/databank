from django.db import models
from django.urls import reverse #Used to generate URLS by reversing the URL Patterns
from django.db.models.fields.files import ImageField
from PIL import Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


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
        return reverse("nas-organisation_by_sector", args=[self.slug])

class State(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name', )
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("nas-organisation_by_state", args=[self.slug])

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
        return reverse("nas-organisation_by_type", args=[self.slug])


class NasOrganisation(models.Model):
    name =  models.CharField(max_length= 200)
    address = models.TextField(max_length= 200)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    sector = models.ForeignKey('Sector', on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    YOE = models.DateField(auto_now= False)
    staff_Strength = models.IntegerField()
    id = models.AutoField(primary_key=True, help_text= "Unique Apprenticeship Number")
    area_of_Specialization = models.CharField(max_length=200)

    APPRENTICE_SCHEME_STAGE = (
        ('Promotion', 'Promotion'),
        ('Appraisal', 'Appraisal'),
        ('Harmonisation', 'Harmonisation'),
        ('Installation', 'Installation'),
        ('Supervision', 'Supervision'),
        ('Monitoring', 'Monitoring'),
    )

    stage =  models.CharField(
        max_length=20, 
        choices= APPRENTICE_SCHEME_STAGE,
        blank=True,
        default = 'Promotion',
        help_text = 'Apprencticeship Stage',
    )

    promotion_Officer =  models.CharField(max_length=200, null=True, blank=True)
    appraisal_Officer =  models.CharField(max_length=200, null=True, blank=True)
    harmonisation_Officer =  models.CharField(max_length=200, null=True, blank=True)
    installation_Officer =  models.CharField(max_length=200, null=True, blank=True)
    supervision_Officer =  models.CharField(max_length=200, null=True, blank=True)
    monitoring_Officer =  models.CharField(max_length=200, null=True, blank=True)
    provisional_approval = models.BooleanField(default=False)
    DOPA = models.DateField(auto_now=False, null = True, blank= True)

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['name', 'id' ]
        permissions = (("can_edit", "Set NasOrganisation for Editing"),)

    def get_absolute_url(self):
        return reverse("nas-organisation-detail", kwargs={"pk": self.id})
    
    def get_age(self):
        now = date.today()
        age1 = now - self.YOE
        age2 = int((age1).days / 365.2425)
        return age2
    
    
