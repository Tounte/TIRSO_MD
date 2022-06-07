from django.db import models

class Excel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to ='documents/')
    created = models.DateTimeField(auto_now_add=True, editable=False)

class Destination(models.Model):
    destination = models.fields.CharField(max_length=100)

class Origine(models.Model):
    origin = models.fields.CharField(max_length=100)

class Transporteur(models.Model):
    transporter = models.fields.CharField(max_length=100)

class Clients(models.Model):
    clients = models.fields.CharField(max_length=100)

