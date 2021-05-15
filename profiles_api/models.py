from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager for User Profiles """

    def create_user(self, email, name, password=None):
        """ Create A New User Profile """
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Crerate and Save a New Superuser with the given Data """
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in this system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve Full Name of the User """
        return self.name

    def get_short_name(self):
        """ Retrieve Short Name of the User """
        return self.name

    def __str__(self):
        """ Retrieve string Representaion of the User """
        return self.email
