from django.db import models
from django.urls import reverse #Used to generate URLS by reversing the URL Patterns
from django.db.models.fields.files import ImageField
from PIL import Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User


class State(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)

	class Meta:
		ordering = ('name', )
		verbose_name = 'state'
		verbose_name_plural = 'states'
	
	def get_absolute_url(self):
		return reverse("staff_by_state", args= [self.slug])
	
	def  __str__(self):	
		return self.name

class Division(models.Model):

	name = models.CharField(max_length = 200)
	slug = models.SlugField(max_length= 200)

	class Meta:
		ordering = ('name', )
		verbose_name = 'division'
		verbose_name_plural = 'divisions'

	def  __str__(self):	
		return self.name
	
	def get_absolute_url(self):
		return reverse('staff_by_division', args = [self.slug])
	
class Designation(models.Model):

	name = models.CharField(max_length = 200)
	slug = models.SlugField(max_length= 200)

	def  __str__(self):	
		return self.name

	class Meta:
		ordering = ('name', )
		verbose_name = 'designation'
		verbose_name_plural = 'designations'
	
	def get_absolute_url(self):
		return reverse('staff_by_designation', args = [self.slug])

# class AnnualLeave(models.Model):
# 	name = models.CharField(max_length = 200)
# 	slug = models.SlugField(max_length= 200)

# 	def  __str__(self):	
# 		return self.name

# 	class Meta:
# 		ordering = ('name', )
# 		verbose_name = 'annualleave'
# 		verbose_name_plural = 'annualleaves'
	
# 	def get_absolute_url(self):
# 		return reverse('staff_by_annualleave', args = [self.slug])


class Certification(models.Model):

	name = models.CharField(max_length = 200, null=True)
	

	class Meta:
		ordering = ('name', )
		verbose_name = 'certification'
		verbose_name_plural = 'certifications'

	def  __str__(self):	
		return self.name
	

class Training(models.Model):

	name = models.CharField(max_length=200)

	class Meta:
		ordering = ('name', )
		verbose_name = 'training'
		verbose_name_plural = 'trainings'

	def  __str__(self):	
		return self.name

class StaffBio(models.Model):
	#Bio
	surname= models.CharField(max_length=200, db_index=True)
	firstname= models.CharField(max_length=200)
	othernames= models.CharField(max_length=200, blank=True)
	date_of_Birth = models.DateField(auto_now=False)
	state_of_Origin = models.ForeignKey('State', on_delete=models.SET_NULL, null = True)
	LGA = models.CharField(max_length=200, blank=False)
	senatorial_District = models.CharField(max_length=200, blank=False)
	GENDER_OPTION = (
		('Male', 'Male'),
		('Female', 'Female'),
	)
	sex = models.CharField(
		choices= GENDER_OPTION,
		blank=False,
		default='Male',
		max_length= 20
	)

	MARITAL_STATUS_CHOICES = (
		('Single', 'Single'),
		('Married', 'Married')
	)
	marital_Status  = models.CharField(
		choices=MARITAL_STATUS_CHOICES,
		blank=False,
		default='Single',
		max_length=20
	)

	#Official
	date_of_Employment = models.DateField(auto_now=False, null = True)
	#annualleave = models.ForeignKey('AnnualLeave', on_delete=models.SET_NULL, null = True )
	staffId= models.SmallIntegerField(primary_key= True)
	designation = models.ForeignKey('Designation', on_delete=models.SET_NULL, null = True)
	division= models.ForeignKey(Division, on_delete=models.SET_NULL,  null=True)
	CONITFS_LEVEL = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
		('10', '10'),
		('11', '11'),
		('12', '12'),
		('13', '13'),
		('14', '14'),
		('15', '15'),
		('16', '16'),
		('17', '17'),
	)
	conitfs = models.CharField(
		choices= CONITFS_LEVEL,
		blank = False,
		default='1',
		max_length=20
	)
	date_of_Last_Promotion = models.DateField(auto_now=False, null=True)
	date_of_next_Promotion = models.DateField(auto_now=False, null=True)

	#Contact Information
	email_official= models.CharField(max_length=200, unique=True)
	email= models.CharField(max_length=200 , unique=True)
	mobile_phone= models.CharField(max_length = 200, null=True , unique=True)
	address = models.CharField(max_length = 200, null = True)
	


	#Education
	diploma = models.CharField(max_length=200, blank=True)
	bachelors_degree=models.CharField(max_length=200, null=True, blank=True)
	masters_degree=models.CharField(max_length=200,  null=True, blank=True)
	doctorate_degree = models.CharField(max_length = 200, null=True, blank=True)

	#Career Development
	certification= models.ManyToManyField('Certification', blank = True)
	trainings_attended=models.ManyToManyField('Training')
	image= models.ImageField(upload_to= 'uploads/staff')
	favQuote = models.CharField(max_length = 200, null = True)
	leave_Start = models.DateField(auto_now=False, blank=True)
	leave_End = models.DateField(auto_now=False, blank=True)
	
	LEAVE_STATUS = (
		('Annual Leave', 'Annual Leave'),
		('Absconded', 'Absconded'),
		('Available', 'Available'),
		('Sick Leave', 'Sick Leave'),
		('Casual Leave', 'Casual Leave'),
		('Career Development', 'Career Development'),
		('Sabbatical Leave', 'Sabbatical Leave')
	)

	status =  models.CharField(
		choices=LEAVE_STATUS,
		blank=False,
		default='Available',
		max_length=20
	)

	 

	# class Meta:
	# 	permissions = (("can_edit", "Set Staff for Editing"),)


	def getAge(self):
		now = date.today()
		age1 = now - self.date_of_Birth
		age2 = int((age1).days / 365.2425)
		return age2
		
	def getEmplomentAge(self):
		now = date.today()
		date1 = now - self.date_of_Employment
		date2 = int((date1).days / 365.2425)
		return date2
	
	def getPromotionAge(self):
		now = date.today()
		date1 = now - self.date_of_Last_Promotion
		date2 = int((date1).days / 365.2425)
		return date2

	def getNextPromotionAge(self):
		now = date.today()
		date1 = self.date_of_next_Promotion - now
		date2 = int((date1).days / 365.2425)
		return date2
	


	def get_absolute_url(self):
		return reverse('staff-bio', args = [str(self.staffId)])

	def __str__(self):
		return f'{self.surname}, {self.othernames} {self.firstname}' 
	

	def display_certification(self):
		return ', '.join(certification.name for certification in self.certification.all())
	
	display_certification.short_description = 'certification'


	def staff_image(self):
		return format_html('<img src = "/media/%s" width="100" height="100" />' % (self.image))
		return mark_safe('<img src = "/media/%s" width="100" height="100" />' % (self.image))
        
	staff_image.short_description = 'Image'
	staff_image.allow_tags = True


# class AnnualLeaveStatus(models.Model):
# 	staff= models.ForeignKey('StaffBio', on_delete=models.SET_NULL,  null=True)
# 	leave_start= models.DateField( null = False)
# 	leave_end= models.DateField( null = False)


# 	LEAVE_STATUS = (
# 		('l', 'On Leave'),
# 		('ab', 'Absconded'),
# 		('av', 'Available'),
# 		('sl', 'Sick Leave'),
# 		('c', 'Casual Leave'),
# 		('cd', 'Career Development'),
# 		('sb', 'Sabbatical Leave')
# 	)

# 	status = models.CharField(
# 		max_length=2,
# 		choices= LEAVE_STATUS,
# 		blank=False,
# 		default='av',
# 	)

# 	class Meta:
# 		ordering: ['leave_start']
# 		permissions = (("can_edit", "Set Staff for Editing"),)
		
# 	def __str__(self):
# 		return f'{self.staff.surname} ({self.staff.staffId})'
	
# 	@property
# 	def is_on_leave(self):
# 		if self.leave_end and date.today() > self.leave_end:
# 			return True
# 		return False