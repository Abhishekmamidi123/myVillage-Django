# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

## Not required as we are using REST API##
class house(models.Model):
	lon=models.FloatField()
	lat=models.FloatField()
	income=models.FloatField()
	doorNo=models.CharField(max_length=35,unique=True)
	def __str__(self):
		return str(self.doorNo)

class member(models.Model):
	name=models.CharField(max_length=35)
	gender=models.CharField(max_length=7)
	age=models.IntegerField()
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class housePhoto(models.Model):
	photo=models.CharField(max_length=350)
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return self.photo

class houseAudio(models.Model):
	audio=models.CharField(max_length=350)
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return self.audio

class farm(models.Model):
	area=models.FloatField()
	house=models.ForeignKey(house,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.house)

class point(models.Model):
	lon=models.FloatField()
	lat=models.FloatField()
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	sequenceNo=models.IntegerField()
	def __str__(self):
		return str(self.farm)

class crop(models.Model):
	crop=models.CharField(max_length=345,unique=True)
	def __str__(self):
		return self.crop

class season(models.Model):
	season=models.CharField(max_length=345,unique=True)
	def __str__(self):
		return self.season

class cropping(models.Model):
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	crop=models.ForeignKey(crop,on_delete=models.CASCADE)
	season=models.ForeignKey(season,on_delete=models.CASCADE)
	year=models.CharField(max_length=350)
	area=models.FloatField()
#	Unique has to be done
	def __str__(self):
		return str(self.year)

class farmPhoto(models.Model):
	photo=models.CharField(max_length=350)
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	def __str__(self):
		return self.farm

class farmAudio(models.Model):
	audio=models.CharField(max_length=350)
	farm=models.ForeignKey(farm,on_delete=models.CASCADE)
	def __str__(self):
		return self.farm

class well(models.Model):
	lon=models.FloatField()
	lat=models.FloatField()
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
		return self.well

class wellPhoto(models.Model):
	photo=models.CharField(max_length=350)
	well=models.ForeignKey(well,on_delete=models.CASCADE)
	def __str__(self):
		return self.well

class wellAudio(models.Model):
	audio=models.CharField(max_length=350)
	well=models.ForeignKey(well,on_delete=models.CASCADE)
	def __str__(self):
		return self.well
