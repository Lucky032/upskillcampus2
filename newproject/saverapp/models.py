from django.db import models
from django.contrib.auth.models import User


class Personalinfo(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # In production, use hashing for passwords
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} {self.email} {self.password}" 

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"Password for {self.website} - {self.username}"
