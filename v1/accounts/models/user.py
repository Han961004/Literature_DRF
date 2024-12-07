from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set.")
        if not email:
            raise ValueError("The Email field must be set.")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  # Django 기본 Password 길이
    email = models.EmailField(unique=True)           
    last_login = models.DateTimeField(null=True, blank=True)  # AbstractBaseUser에서 제공하는 필드
    date_joined = models.DateTimeField(auto_now_add=True) 
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'  # 로그인을 위한 식별자로 사용할 필드
    
    class Meta:
        app_label = 'accounts'