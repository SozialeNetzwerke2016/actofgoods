from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User, Group

# Create your models here.
class Message(models.Model):
	text = models.CharField(max_length=300)

class Address(models.Model):
	latitude = models.FloatField()
	longditude = models.FloatField()

# Not acces now errors incomings
class Userdata(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	pseudonym = models.CharField(max_length=15)
	phone = models.CharField(max_length=13)
	messages= models.ManyToManyField(Message)
	GENDER = (('m', 'Male'),('f', 'Female'),)
	gender = models.CharField(max_length=1, choices=GENDER)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

class CategoriesNeeds(models.Model):
	name = models.CharField(max_length=50)

class CategoriesInf(models.Model):
	name = models.CharField(max_length=50)

class CategoriesRep(models.Model):
	name = models.CharField(max_length=50)

class Groupdata(models.Model):
	group = models.OneToOneField(Group, on_delete=models.CASCADE)
	email = models.EmailField(max_length=254)
	phone = models.CharField(max_length=15)
	is_NGO = models.BooleanField(default=True)
	# mabye changed
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Need(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
	headline = models.CharField(max_length=30, default='')
	text = models.TextField(default='')
	closed = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now=True)
	categorie = models.ForeignKey(CategoriesNeeds)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Information(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
	headline = models.CharField(max_length=30, default='')
	text = models.TextField(default='')
	closed = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now=True)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Comment(models.Model):
	inf = models.ForeignKey(Information,on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(default='')
	date = models.DateTimeField(auto_now=True)

class Vote(models.Model):
	date = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	info = models.ForeignKey(Information, on_delete=models.CASCADE)

class Report(models.Model):
	text = models.TextField(default='')
	categorie = models.ForeignKey(CategoriesRep)
	need = models.ForeignKey(Need)
	info = models.ForeignKey(Information)
	Comment = models.ForeignKey(Comment)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class ContactUs(models.Model):
    email = models.EmailField(max_length=254)
    headline = models.CharField(max_length=30, default='')
    text = models.TextField(default='')
    create_date = models.DateTimeField(default = timezone.now)#timezone.now()#models.DateTimeField(default = timezone.now

    def save(self, *args, **kwargs):
        # if not self.id:
        self.create_date = now()
        super(ContactUs, self).save(*args, **kwargs)
