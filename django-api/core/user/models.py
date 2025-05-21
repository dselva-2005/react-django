import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
from abstract.models import AbrstractManager,AbrstractModel

class UserManager(BaseUserManager,AbrstractManager):
    
    def create_user(self,username,email, password=None, **kwargs):
        '''create and return a User with an email, phone number, username and password'''

        if username is None: 
            raise TypeError('user must have an username.')
        
        if email is None:
            raise TypeError('user must have an email.')
        
        if password is None:
            raise TypeError('user must have a password.')
        
        user = self.model(username=username, email=self.normalize_email(email),bio=kwargs.get('bio')  \
                          ,first_name=kwargs.get('first_name'),last_name=kwargs.get('last_name'),avatar=kwargs.get('avatar'))
        
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,username,email,password,**kwargs):
        """create and return a user with superuser permissions"""
        
        if username is None: 
            raise TypeError('Superuser must have an username.')
        
        if email is None:
            raise TypeError('Superuser must have an email.')
        
        if password is None:
            raise TypeError('Superuser must have a password.')

        superuser = self.create_user(username=username,password=password,email=email,**kwargs)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)

        return superuser

# Create your models here.
class User(AbrstractModel,AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255, db_index=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    bio = models.CharField(max_length=500,null=True)
    avatar = models.ImageField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
