from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=255, blank=True)
    percentage = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + str(self.user)

class Work(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(blank=True, upload_to='work/')
    link = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + str(self.user)

class Service(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + str(self.user)

class Contact(models.Model):
    reciever = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject + ' - ' + str(self.reciever)

class Portfolio(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, blank=True)
    profile_photo = models.ImageField(blank=True, upload_to='user-images/')
    about_me_text = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    date_of_birth = models.DateField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    services = models.ManyToManyField(Service, blank=True)
    hire_me_text = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv', blank=True)
    portfolio_text = models.TextField(blank=True)
    works = models.ManyToManyField(Work, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    behance = models.CharField(max_length=255, blank=True)
    pinterest = models.CharField(max_length=255, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    google_map = models.CharField(max_length=555, blank=True)
    footer_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user)
