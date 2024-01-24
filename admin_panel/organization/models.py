from django.db import models

class Organization(models.Model):
    organization_id = models.UUIDField(primary_key=True)
    organization_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    password = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username