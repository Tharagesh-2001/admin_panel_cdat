from django.db import models

class Organization(models.Model):
    organization_id = models.IntegerField(max_length=255)
    organization_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    password = models.CharField(max_length=255)
    access_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)