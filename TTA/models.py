from django.db import models
from django.urls import reverse #Used to generate URLS by reversing the URL Patterns
from django.db.models.fields.files import ImageField
from PIL import Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User


class SpecialInterventionProgram(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Special Intervention Progam'
        verbose_name_plural = 'Special Intervention Progam'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("trainee_by_sip", args = [self.slug])

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
        return reverse("trainee_by_state", args=[self.slug])

class TradeArea(models.Model):
    name = models.CharField(max_length= 200)
    slug = models.SlugField(max_length = 200)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Trade Area'
        verbose_name_plural = 'Trade Areas'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("trainee_by_tradearea", args=[self.slug])

class Bank(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("trainee_by_bank", kwargs={"pk": self.slug})
    

class Trainee(models.Model):
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    other_names = models.CharField(max_length=200)
    DOB = models.DateField(auto_now=False)
    email= models.CharField(max_length=200, unique=True)
    mobile_phone= models.CharField(max_length = 200, null=True, unique=True)
    address = models.TextField( null = True)
    image= models.ImageField(upload_to= 'uploads/trainee')
    special_Intervention_Program = models.ForeignKey(SpecialInterventionProgram, on_delete=models.SET_NULL, null = True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null = True)
    trade_Area = models.ForeignKey(TradeArea, on_delete=models.SET_NULL, null = True)
    #year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, max_length=4, default= datetime.now().year)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    account_Number = models.IntegerField()
    bvn = models.IntegerField(primary_key= True)
    date_of_Program = models.DateField(default=date.today)
    



    def Age(self):
        now = date.today()
        age1 = now - self.DOB
        age2 = int((age1).days / 365.2425)
        return age2
    
    def Year_Of_Program(self):
        year1 = self.date_of_Program
        year = year1.year
        return year 



    def __str__(self):
        return f'{self.last_name}, {self.other_names} {self.first_name}'

    def trainee_image(self):
        return format_html('<img src = "/media/%s" width="100" height="100" />' % (self.image))
        #return mark_safe('<img src = "/media/%s" width="100" height="100" />' % (self.image))
        
    trainee_image.short_description = 'Image'
    trainee_image.allow_tags = True

    def get_absolute_url(self):
        return reverse("trainee-detail", kwargs={"pk": self.bvn})
    