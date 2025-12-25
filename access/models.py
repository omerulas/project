from django.db import models
from access.manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    # Add field or relation here whatever you need!
    
    email = models.EmailField(verbose_name='E-posta', unique=True)
    full_name = models.CharField(verbose_name='Adı Soyadı', max_length=125)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="access_user_groups", # Çakışmayı önleyen benzersiz isim
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="access_user_permissions", # Çakışmayı önleyen benzersiz isim
        related_query_name="user",
    )
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email