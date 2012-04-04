from django.contrib.auth.models import User
from django.db import models

class Association(models.Model):
#Association describes an association that is hosting the event
	# Core Fields
	name = models.CharField(max_length=200)
	logo = models.ImageField(upload_to='assoc_logos')
	description = models.TextField()
	notes = models.TextField()
	
	# Metadata
	creator = models.ForeignKey(User)
	slug = models.SlugField(unique=True)
	updated = models.DateTimeField(auto_now=True)
	
	# Contact Info
	contact_name = models.CharField(max_length=200)
	contact_email = models.EmailField()
	contact_phone = models.CharField(max_length = 20)
	contact_address = models.TextField()
	alt_contact_name = models.CharField(max_length=200)
	alt_contact_email = models.EmailField()
	alt_contact_phone = models.CharField(max_length = 20)
	
	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return "/associations/%s/" % (self.slug)

class Participant(models.Model):
# Participant describes a vendor or exhibitor who will hold a booth at the event			
	# Core Fields
	name = models.CharField(max_length=200)
	description = models.TextField()
	notes = models.TextField()
	
	# Metadata
	creator = models.ForeignKey(User)
	slug = models.SlugField(unique=True)
	updated = models.DateTimeField(auto_now=True)

	#Contact Info
	contact_name = models.CharField(max_length=200)
	contact_email = models.EmailField()
	contact_phone = models.CharField(max_length = 20)
	contact_address = models.TextField()
	alt_contact_name = models.CharField(max_length=200)
	alt_contact_email = models.EmailField()
	alt_contact_phone = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.name
	
		def get_absolute_url(self):
			return "/participants/%s/" % (self.slug)

class SponsorModel(models.Model):
#Describes a set of sponsor choices
	levels = models.ForeignKey("SponsorLevel")
	def __unicode__(self):
		return self.levels

class SponsorLevel(models.Model):
#Describes sponsor choice	
	name = models.CharField(max_length=60)
	description = models.TextField()
	
class Event(models.Model):
#Describes an Event
	# Status
	PUBLIC_STATUS = 1
	PRIVATE_STATUS = 2
	HIDDEN_STATUS = 3 
	STATUS_CHOICES = (
		(PUBLIC_STATUS, 'Public'),
		(PRIVATE_STATUS, 'Private'),
		(HIDDEN_STATUS, 'Hidden'),
	)
	
	# Core Fields
	name = models.CharField(max_length=200)
	
	
	# Dates
	start_date = models.DateTimeField('Start Date & Time')
	end_date = models.DateTimeField('End Date & Time')
	
	# Metadata
	creator = models.ForeignKey(User)
	status = models.IntegerField(choices=STATUS_CHOICES, default=PRIVATE_STATUS)
	slug = models.SlugField(unique=True)
	updated = models.DateTimeField(auto_now=True)
	
	# Relationships
	participants = models.ForeignKey(Participant)
	floorplan = models.OneToOneField('locations.Floorplan')
	association = models.OneToOneField(Association)
	sponsor_model = models.OneToOneField(SponsorModel)

	class Meta:
		ordering = ["start_date"]
	def __unicode__(self):
		return self.name


	
