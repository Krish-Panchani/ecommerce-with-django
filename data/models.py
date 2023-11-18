from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone

class user(models.Model):
	name = models.CharField(max_length=50)
	mobile = models.BigIntegerField()
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	message = models.CharField(max_length=250,default=None)
	created_time = models.DateTimeField(default=timezone.now)
	updated_time = models.DateTimeField(auto_now=True)

class homephoto(models.Model):
	photos = models.ImageField(upload_to="img",default="None")
	
class textile(models.Model):
	photos = models.ImageField(upload_to="textile",default="None")
	name = models.CharField(max_length=50)
	message = models.CharField(max_length=50,default=None)
	size = models.CharField(max_length=2)
	size1 = models.CharField(max_length=2)
	size2 = models.CharField(max_length=2)
	size3 = models.CharField(max_length=2)
	mainprice = models.IntegerField(blank=True, null=True)
	discount = models.IntegerField(blank=True, null=True)
	realprice = models.IntegerField(blank=True, null=True)
	created_time = models.DateTimeField(default=timezone.now)
	updated_time = models.DateTimeField(auto_now=True)

class jewellery(models.Model):
	photos = models.ImageField(upload_to="textile",default="None")
	name = models.CharField(max_length=50)
	message = models.CharField(max_length=50,default=None)
	mainprice = models.IntegerField(blank=True, null=True)
	discount = models.IntegerField(blank=True, null=True)
	realprice = models.IntegerField(blank=True, null=True)
	created_time = models.DateTimeField(default=timezone.now)
	updated_time = models.DateTimeField(auto_now=True)

class vegetable(models.Model):
	photos = models.ImageField(upload_to="textile",default="None")
	name = models.CharField(max_length=50)
	kg = models.IntegerField(blank=True, null=True)
	mainprice = models.IntegerField(blank=True, null=True)
	discount = models.IntegerField(blank=True, null=True)
	realprice = models.IntegerField(blank=True, null=True)
	created_time = models.DateTimeField(default=timezone.now)
	updated_time = models.DateTimeField(auto_now=True)

class other(models.Model):
	photos = models.ImageField(upload_to="textile",default="None")
	name = models.CharField(max_length=50)
	message = models.CharField(max_length=50,default=None)
	size = models.CharField(max_length=2)
	size1 = models.CharField(max_length=2)
	size2 = models.CharField(max_length=2)
	size3 = models.CharField(max_length=2)
	mainprice = models.IntegerField(blank=True, null=True)
	discount = models.IntegerField(blank=True, null=True)
	realprice = models.IntegerField(blank=True, null=True)
	created_time = models.DateTimeField(default=timezone.now)
	updated_time = models.DateTimeField(auto_now=True)