from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from datetime import date
from uuid import uuid4
import datetime
import os

DIR_PRFILE = 'profile'

class Person(models.Model):
	def _path_image(instance,archivo):
		extension = os.path.splitext(archivo)[1][1:]
		path = os.path.join(DIR_PRFILE, date.today().strftime("%Y/%m"))
		name_file = '{}.{}'.format(uuid4().hex, extension)
		return os.path.join(path, name_file)

	code = models.CharField(max_length=10,null=True, blank=True)
	num_visit = models.IntegerField()
	description = models.CharField(max_length=100,null=True ,blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	lastname = models.CharField(max_length=100, null=True, blank=True)
	birthdate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
	telephone = models.CharField(max_length=30, null=True, blank=True)
	pin = models.CharField(max_length=100, null=True, blank=True)
	img_profile = models.ImageField(upload_to=_path_image, null=True, blank=True)
	fk_user = models.ForeignKey(User, null=False)

# state=1 friends | state=2 canceled | state=0 process
class Friend(models.Model):
	state = models.IntegerField(null=False, blank=False)
	asked = models.BooleanField(default=False)
	fk_person = models.ForeignKey(Person, related_name='person', null=False, blank=False)
	fk_person_friend = models.ForeignKey(Person, related_name='person_friend', null=False, blank=False)

class Request_Loans(models.Model):
	amount_request = models.FloatField(null=False, blank=False)
	amount_available = models.FloatField(null=False, blank=False)
	interest = models.FloatField(null=False, blank=False)
	date_return = models.IntegerField(null=False, blank=False)
	date_expiration = models.DateField(null=False, blank=False)
	date_create = models.DateField(auto_now_add=True)
	commentary = models.CharField(max_length=150, null=False, blank=False)
	state = models.BooleanField(default=True)
	fk_person = models.ForeignKey(Person, null=False, blank=False)

class Friends_Loans(models.Model):
	state = models.BooleanField(default=False)
	fk_request_loans = models.ForeignKey(Request_Loans, null=False, blank=True)
	fk_friends = models.ForeignKey(Friend, null=False, blank=False)

class Loans(models.Model):
	amount_loan = models.FloatField(null=False, blank=False)
	amount_interest = models.FloatField(null=False, blank=False)
	state = models.BooleanField(default=False)
	fk_friend_loans = models.ForeignKey(Friends_Loans, null=False, blank=False)

class Notification(models.Model):
	# num = 0 !friends | num = 1 !request_loans | num = 2 !loans 
	message = models.CharField(max_length=150, null=False, blank=False)
	num = models.IntegerField(null=False, blank=False)
	state = models.BooleanField(default=True)
	fk_friends = models.ForeignKey(Friend, null=True, blank=True)
	fk_loans = models.ForeignKey(Loans, null=True, blank=True)
	fk_request_loans = models.ForeignKey(Request_Loans, null=True, blank=True)
	fk_person = models.ForeignKey(Person, null=False, blank=False)

class Account(models.Model):
	amount_available = models.FloatField(null=False, blank=False) 
	amount_locked = models.FloatField(null=False, blank=False) 
	fk_person = models.ForeignKey(Person, null=False, blank=False)
