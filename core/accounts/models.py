from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionMixin)

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)
    f_name = models.CharField(max_length=31)
    
    REQUIERED_FIELD = []
    
    created_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    