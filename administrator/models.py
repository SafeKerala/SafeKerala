from django.db import models

# Create your models here.
class Logintable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)
class Policestation(models.Model):
    LOGIN_ID=models.ForeignKey(Logintable, on_delete=models.CASCADE,null=True,blank=True)
    policestationname=models.CharField(max_length=100,null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
class user(models.Model):
    LOGIN_ID=models.ForeignKey(Logintable, on_delete=models.CASCADE,null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
class complaints(models.Model):
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True,blank=True)
    complaints=models.CharField(max_length=100,null=True,blank=True)
    replycomplaint=models.CharField(max_length=100,null=True,blank=True)
    complaintdate=models.DateField(max_length=100,null=True,blank=True)
class viewfeedback(models.Model):
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True,blank=True)
    feedback=models.CharField(max_length=100,null=True,blank=True)
class notification(models.Model):
    LOGIN_ID=models.ForeignKey(Logintable, on_delete=models.CASCADE,null=True,blank=True)
    notification=models.CharField(max_length=100,null=True,blank=True)
class labourprofile(models.Model):
    LOGIN_ID=models.ForeignKey(Logintable, on_delete=models.CASCADE,null=True,blank=True)
    skills=models.CharField(max_length=100,null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
class criminallistmanagement(models.Model):
    criminalname=models.CharField(max_length=100,null=True,blank=True)
    criminalcase=models.CharField(max_length=100,null=True,blank=True)
class requesttable(models.Model):
    Userid=models.ForeignKey(user, on_delete=models.CASCADE,null=True,blank=True)
    Labourid=models.ForeignKey(labourprofile, on_delete=models.CASCADE,null=True,blank=True)
    Requeststatus=models.CharField(max_length=100,null=True,blank=True)
    Requestdate=models.DateField(max_length=100,null=True,blank=True)

    

    






    

    

    

    

