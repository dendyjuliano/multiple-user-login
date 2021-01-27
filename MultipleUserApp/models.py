from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_role = models.ForeignKey(Role, on_delete=models.SET_NULL,null=True)

