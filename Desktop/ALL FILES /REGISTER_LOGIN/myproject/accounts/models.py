from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50,blank=True,null=True)

    groups = models.ManyToManyField(
        Group,
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True
    )