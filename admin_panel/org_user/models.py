from django.db import models
from org_admin.models import OrgAdmin

class OrgUser(models.Model):
    role_choices = [
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer')
    ]
    org_admin = models.ForeignKey(OrgAdmin, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=role_choices)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.username} - {self.role}"

class Services(models.Model):
    uuid = models.UUIDField(primary_key=True)
    service_name = models.CharField(max_length=255)
    tag_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)