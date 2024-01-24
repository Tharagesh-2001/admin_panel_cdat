from django.db import models
from organization.models import Organization


class OrgAdmin(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    admin_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    password = models.CharField(max_length=255)

class Services(models.Model):
    organization = models.ForeignKey(OrgAdmin, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True)
    service_name = models.CharField(max_length=255)
    tag_name = models.CharField(max_length=255)