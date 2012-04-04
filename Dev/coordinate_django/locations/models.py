from django.db import models

class Location(models.Model):
	# Core Fields
	name = models.CharField(max_length=200)
	address = models.TextField()
	
	size = models.IntegerField()
	max_num_booths = models.IntegerField()
	max_occupancy = models.IntegerField()
	
	contact_name = models.CharField(max_length=200)
	contact_email = models.EmailField()
	contact_phone = models.CharField(max_length = 20)
	
	alt_contact_name = models.CharField(max_length=200)
	alt_contact_email = models.EmailField()
	alt_contact_phone = models.CharField(max_length = 20)
	
	# Relationships
	floorplans = models.ForeignKey('Floorplan', related_name="location_floorplans")

class Floorplan(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='floorplans')
	location = models.ForeignKey('Location')
	
class Boothspace(models.Model):
	# Implement Marker Choices
	
	booth_num = models.IntegerField()
	top = models.IntegerField(default=50)
	left = models.IntegerField(default=50)
	occupant = models.ForeignKey('events.Participant')
	#marker
	is_bookable = models.BooleanField(default=True)
	floorplan = models.ForeignKey('Floorplan')