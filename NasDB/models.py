from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
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
        return reverse("nas-organisation_by_trainingrecord", args=[self.slug])

class RecruitmentAndSelection(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'Recruitment and Selection Method'
        verbose_name_plural =  'Recruitment and Selection Methods'

    def get_absolute_url(self):
        return reverse("nas-organisation_by_recruitmentandselection", args=[self.slug])


class TrainingRecord(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length= 200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'training record'
        verbose_name_plural = 'training records'
    
    def get_absolute_url(self):
        return reverse("nas-organisation_by_type", args=[self.slug])

class TradeArea(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length= 200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'trade area'
        verbose_name_plural = 'trade areas'
    
    def get_absolute_url(self):
        return reverse("nas-organisation_by_tradearea", args=[self.slug])

class ProfessionalMembership(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length= 200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'professional membership'
        verbose_name_plural = 'professional memberships'
    
    def get_absolute_url(self):
        return reverse("nas-organisation_by_type", args=[self.slug])


class NasOrganisation(models.Model):
    name =  models.CharField(max_length= 200)
    address = models.TextField(max_length= 200)
    contact_person = models.CharField(max_length=200, null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=200, blank=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    sector = models.ForeignKey('Sector', on_delete=models.SET_NULL, null=True)
    sub_Sector = models.CharField(max_length=200)
    trade_Area = ManyToManyField('TradeArea')
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    YOE = models.DateField(auto_now= False)
    staff_Strength_Permanent = models.IntegerField(blank=True) 
    staff_Strength_Contract = models.IntegerField( blank=True)
    staff_Strength_Temporary = models.IntegerField( blank=True)
    id = models.AutoField(primary_key=True, help_text= "Unique Apprenticeship Number")
    CHOICE = [
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    
    cac_Registration = models.CharField(
        max_length=20,
        choices=CHOICE,
        blank=True,
        default='Yes'
    )

    cac_Reg_Number = models.IntegerField(blank=True, null=True)

    itf_Registration = models.CharField(
        max_length=20,
        choices=CHOICE,
        blank=True,
        default='No'
    )

    itf_Reg_Number = models.IntegerField(blank=True, null=True)


    APPRENTICE_SCHEME_STAGE = [
        ('Promotion', 'Promotion'),
        ('Appraisal', 'Appraisal'),
        ('Harmonisation', 'Harmonisation'),
        ('Installation', 'Installation'),
        ('Inspection, Supervision, Monitoring', 'Inspection, Supervision, Monitoring'),
    ]

    stage =  models.CharField(
        max_length=50, 
        choices= APPRENTICE_SCHEME_STAGE,
        blank=True,
        default = 'Promotion',
        help_text = 'Apprencticeship Stage',
    )

    #Promotion
    promotion_Officer =  models.CharField(max_length=200, blank=True)
    PROMOTION_REPORT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
       ]
    promotional_report_available = models.CharField(
        max_length=5,
        choices=PROMOTION_REPORT_STATUS,
        blank=True,
        default='NO',
        help_text='YES or NO'
    )
    promotional_report = models.FileField(upload_to= 'upload/nas/reports/promotion', blank=True)
    products =  models.CharField(max_length=200, blank=True)
    services = models.CharField(max_length=200, blank=True)
    tna = models.TextField(blank=True)

    #Apraisal
    appraisal_Officer =  models.CharField(max_length=200, blank=True)
    APPRAISAL_REPORT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]
    curriculum_available = models.CharField(
        max_length=5,
        choices=APPRAISAL_REPORT_STATUS,
        blank=True,
        default='NO',
        help_text='YES or NO'
    )
    CURRICULUM = [
        ('ITF', 'ITF'),
        ('ORGANISATION DESIGN', 'ORGANISATION DESIGN'),
        ('NSQ', 'NSQ'),
        ('OTHERS', 'OTHERS'),
    ]
    curriculum_type = models.CharField(
        max_length=200,
        choices=CURRICULUM,
        blank=True,
        default='ITF',  
    )
    other_curriculum_type = models.CharField(max_length=200, blank=True)

    recruitment_and_Selection = ForeignKey(RecruitmentAndSelection, on_delete=models.SET_NULL, null=True, blank=True)
    
    training_Approach_Practical  = models.IntegerField(blank=True, null=True)
    training_Approach_Theory = models.IntegerField(blank=True, null=True)
    training_Approach_Otj = models.IntegerField(blank=True, null=True)
    
    TRAINING_REPORT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]
    training_record_available = models.CharField(
        max_length=200,
        choices=TRAINING_REPORT_STATUS,
        blank=True,
        default='NO',
        
    )
    training_record_type = models.ManyToManyField(TrainingRecord, blank=True)

    CERTIFICATION_AVAILABLE_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]
    certification_available = models.CharField(
        max_length=5,
        choices=CERTIFICATION_AVAILABLE_STATUS,
        blank=True,
        default='NO',
        
    )
    CERTIFICATION = [
        ('CERTIFICATE OF PARTICIPATION', 'CERTIFICATE OF PARTICIPATION'),
        ('CERTIFICATE OF COMPETENCY', 'CERTIFICATE OF COMPETENCY'),
        ('CITY AND GUILD','CITY AND GUILD'),
        ('NABTEB', 'NABTEB'),
        ('NSQ', 'NSQ'),
        ('NUC/ATC', 'NUC/ATC'),
    ]

    certification_type = models.CharField(
        max_length=200,
        choices=CERTIFICATION,
        blank=True,
        default='CERTIFICATE OF PARTICIPATION',
        
    )

    APPRENTICESHIP_CONTRACT_AGREEMENT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
        
    ]

    apprenticeship_Contract_Agreement = models.CharField(
        max_length=5,
        choices=APPRENTICESHIP_CONTRACT_AGREEMENT_STATUS,
        blank=True,
        default='NO', 
    )

    welfare_for_Trainees = models.CharField(max_length=200, blank=True)

    appraisal_findings = models.TextField(blank=True, null=True)
    appraisal_recommendations = models.TextField(blank=True, null=True)
    appraisal_conclusion = models.TextField(blank=True, null=True)


    APPRAISAL_REPORT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
        
    ]
    appraisal_report_available = models.CharField(
        max_length=5,
        choices=APPRAISAL_REPORT_STATUS,
        blank=True,
        default='NO',
        
    )

    appraisal_report = models.FileField(upload_to= 'upload/nas/reports/appraisal', blank=True)

    #Harmonisation
    harmonisation_Officer =  models.CharField(max_length=200, null=True, blank=True)

    types_of_Apprenticeship_Installed = models.TextField(blank=True)
    apprencticeship_Type_Existing = models.TextField(blank=True)
    apprenticeship_Components_Lacking =  models.TextField(blank=True)
    apprenticeship_Components_Harmonised = models.TextField(blank=True)
    
    HARMONISATION_REPORT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
        
    ]
    harmonisation_report_available = models.CharField(
        max_length=5,
        choices=HARMONISATION_REPORT_STATUS,
        blank=True,
        default='NO',
       
    )
    harmonisation_report = models.FileField(upload_to= 'upload/nas/reports/harmonisation', blank=True)

    #Installation
    installation_Officer =  models.CharField(max_length=200, null=True, blank=True)

    apprenticeship_Type_Installed = models.TextField(blank=True)
    apprenticeship_Components_Installed = models.TextField(blank=True)

    
    INSTALLATION_REPORT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]
    installation_report_available = models.CharField(
        max_length=5,
        choices=INSTALLATION_REPORT_STATUS,
        blank=True,
        default='N/A',
        
    )
    installation_report = models.FileField(upload_to= 'upload/nas/reports/installation', blank=True)

    #Inspection/Supervision/Monitoring
    ISM_Officer =  models.CharField(max_length=200, null=True, blank=True)
    INSPECTION_CHOICES = [
        ('Not yet done', 'Not yet done'),
        ('Poor', 'Average'),
        ('Average', 'Average'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent')
    ]
    planning_of_Training_Programme = models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )

    proper_Use_of_Training_Facilities_tools_and_Equipment =  models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )

    
    use_of_Appropriate_Method_of_Training = models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )
   
    
    record_of_Trainees_Performance = models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )

    
    entries_in_Trainees_Logbook = models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )

    adherence_to_Syllabus_and_Curriculum =models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )



    progress_Report_of_the_Scheme = models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )

    
    general_Record_Keeping = models.CharField(
        choices=INSPECTION_CHOICES,
        max_length=20,
        blank=True,
        default='Not yet done'
    )

    installation_conclusion  = models.TextField(blank = True, null = True)

    
    ISM_REPORT_STATUS = [
        ('YES', 'YES'),
        ('NO', 'NO'),
        
    ]
    
    ISM_report_available = models.CharField(
        max_length=20,
        choices=ISM_REPORT_STATUS,
        blank=True,
        default='NO',
        
    )
    ISM_report = models.FileField(upload_to= 'upload/nas/reports/ism', blank=True)

    #Approvals and Certification
    provisional_approval = models.BooleanField(default=False)
    DOPA = models.DateField(auto_now=False, null = True, blank= True)
    full_approval = models.BooleanField(default=False)
    DOFA = models.DateField(auto_now=False, null=True, blank=True)

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
    

class InstructionalStaff(models.Model):
    name = models.CharField(max_length=200)
    trade_Area = models.ForeignKey(TradeArea, on_delete=models.SET_NULL, null=True)
    professional_Membership = models.ManyToManyField(ProfessionalMembership)
    doe = models.DateField(auto_now=False)
    organisation = models.ForeignKey(NasOrganisation,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    def yearsOfEmploy(self):
        now = date.today()
        date1 = now - self.doe
        date2 = int((date1).days / 365.2425)
        return date2
    
    def get_absolute_url(self):
        return reverse("instructional_staff-detail", kwargs={"pk": self.id})

class ApprencticeTrainee(models.Model):
    name = models.CharField(max_length=200)
    trade_Area = models.ForeignKey(TradeArea, on_delete=models.SET_NULL, null=True)
    doe = models.DateField(auto_now=False)
    organisation = models.ForeignKey(NasOrganisation,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    def yearsOfEmploy(self):
        now = date.today()
        date1 = now - self.doe
        date2 = int((date1).days / 365.2425)
        return date2
    
    def get_absolute_url(self):
        return reverse("apprentice_trainee-detail", kwargs={"pk": self.id})


    