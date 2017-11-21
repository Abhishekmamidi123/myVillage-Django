# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

class house(models.Model):
	lat=models.FloatField()
	lon=models.FloatField()
	income=models.FloatField()
	members=models.IntegerField()
	doorNo=models.CharField(max_length=35,unique=True)
	def __str__(self):
		return str(self.doorNo)

class member(models.Model):
	name=models.CharField(max_length=35)
	gender=models.CharField(max_length=7)
	dob=models.DateField(default=date.today)
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.name)

class housePhoto(models.Model):
	photo=models.ImageField(upload_to='images')
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.house)

class houseAudio(models.Model):
	audio=models.FileField(upload_to='audio')
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.audio)

class farm(models.Model):
	area=models.FloatField()
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.house)

class point(models.Model):
	lat=models.FloatField()
	lon=models.FloatField()
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	sequenceNo=models.IntegerField()
	def __str__(self):
		return str(self.farm)

class crop(models.Model):
	crop=models.CharField(max_length=345,unique=True)
	def __str__(self):
		return str(self.crop)

class season(models.Model):
	season=models.CharField(max_length=345,unique=True)
	def __str__(self):
		return str(self.season)

class cropping(models.Model):
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)	
	crop=models.ForeignKey(crop,on_delete=models.CASCADE)
	season=models.ForeignKey(season,on_delete=models.CASCADE)
	year=models.CharField(max_length=350)
	area=models.FloatField()
#	Unique has to be doneaaaaaaa
	def __str__(self):
		return str(self.year)

class farmPhoto(models.Model):
	photo=models.ImageField('images')
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.farm)

class farmAudio(models.Model):
	audio=models.FileField('audio')
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.farm)

class well(models.Model):
	lat=models.FloatField()
	lon=models.FloatField()
	depth=models.FloatField()
	averageWaterYield=models.FloatField()
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.farm)

class dateTime(models.Model):
	date=models.CharField(max_length=50)
	well=models.ForeignKey(well,on_delete=models.CASCADE)
	wateryield=models.FloatField()
	def __str__(self):
		return str(self.well)

class wellPhoto(models.Model):
	photo=models.ImageField('images')
	well=models.ForeignKey(well,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.well)

class wellAudio(models.Model):
	audio=models.FileField('audio')
	well=models.ForeignKey(well,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.well)

class graphColors(models.Model):
	photo=models.ImageField('image')

class weather(models.Model):
	date=models.CharField(max_length=50)
	temperature=models.FloatField()
	def __str__(self):
		return self.date+" "+str(self.temperature)


