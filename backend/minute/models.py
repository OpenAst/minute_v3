from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  username = models.CharField(_("Username"), max_length=255, unique=True)
  first_name = models.CharField(_("First Name"), max_length=180)
  last_name = models.CharField(_("Last Name"), max_length=180, null=True, blank=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)

  objects = CustomUserManager()
  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ['username']
  
  
  class Meta:
    verbose_name = _("User")
    verbose_name_plural = _("Users")
    
  def __str__(self):
    return self.email  

