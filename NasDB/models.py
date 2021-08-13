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
    contact_person = models.CharField(max_length=200, null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=200, null=True)
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

    #Promotion
    promotion_Officer =  models.CharField(max_length=200, null=True, blank=True)
    REPORT_STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
        ('N/A', 'N/A')
    )
    promotional_report_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='NO',
        help_text='YES or NO'
    )

    #Apraisal
    appraisal_Officer =  models.CharField(max_length=200, null=True, blank=True)
    curriculum_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='NO',
        help_text='YES or NO'
    )
    CURRICULUM = (
        ('ITF', 'ITF'),
        ('ORGANISATION DESIGN', 'ORGANISATION DESIGN'),
        ('OTHERS', 'OTHERS'),
    )
    curriculum_type = models.CharField(
        max_length=200,
        choices=CURRICULUM,
        blank=True,
        default='ITF',
        
    )
    
    training_record_available = models.CharField(
        max_length=200,
        choices=REPORT_STATUS,
        blank=True,
        default='NO',
        
    )

    TRAINING_RECORD = (
        ('Log Book', 'Log Book'),
        ('Attendance Register', 'Attendance Register'),
        ('Daily Record Activity', 'Daily Record Activity'),
        ('None', 'None')
    )
    training_record_type = models.CharField(
        max_length= 200,
        choices=TRAINING_RECORD,
        blank=True,
        default='None'
    )
    certification_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='NO',
        
    )

    CERTIFICATION = (
        ('CERTIFICATE OF PARTICIPATION', 'CERTIFICATE OF PARTICIPATION'),
        ('CERTIFICATE OF COMPETENCY', 'CERTIFICATE OF COMPETENCY')
    )

    certification_type = models.CharField(
        max_length=200,
        choices=CERTIFICATION,
        blank=True,
        default='CERTIFICATE OF PARTICIPATION',
        
    )

    appraisal_report_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='N/A',
        
    )

    #Harmonisation
    harmonisation_Officer =  models.CharField(max_length=200, null=True, blank=True)
    harmonisation_report_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='N/A',
       
    )

    #Installation
    installation_Officer =  models.CharField(max_length=200, null=True, blank=True)
    installation_report_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='N/A',
        
    )

    #Supervision
    supervision_Officer =  models.CharField(max_length=200, null=True, blank=True)
    supervision_report_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='N/A',
        
    )

    #Monitoring
    monitoring_Officer =  models.CharField(max_length=200, null=True, blank=True)
    monitoring_report_available = models.CharField(
        max_length=5,
        choices=REPORT_STATUS,
        blank=True,
        default='N/A',
        
    )
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
    
    
