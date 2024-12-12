from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    '''
    Django의 User 관리를 위한 커스텀 User 모델의 매니저 클래스
    '''
    def create_user(self, username, email, password=None, **extra_fields):
        '''
        일반 유저를 생성
        '''
        if not username:
            raise ValueError("아이디는 필수입니다.")
        if not email:
            raise ValueError("이메일은 필수입니다.")
        
        email = self.normalize_email(email)                                 # 이메일 표준화처리하여 저장
        user = self.model(username=username, email=email, **extra_fields)   # User 인스턴스를 생성
        user.set_password(password)                                         # 패스워드 저장
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):     # 관리자 권한을 가진 슈퍼유저 생성 메서드
        '''
        슈퍼 유저를 생성
        '''
        extra_fields.setdefault('is_staff', True)                                   # is_staff를 True
        extra_fields.setdefault('is_superuser', True)                               # is_superuser를 True

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser는 is_staff가 True여야 합니다.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser는 is_superuser가 True여야 합니다.")
        
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)                 # Django 기본 Password 길이
    email = models.EmailField(unique=True)           
    last_login = models.DateTimeField(null=True, blank=True)    # AbstractBaseUser에서 제공하는 필드
    date_joined = models.DateTimeField(auto_now_add=True) 
    is_superuser = models.BooleanField(default=False)           # 사용자가 최고 관리자인지 나타냄 / 모든 권한 및 DB 작업 가능 및 퍼미션 허용
    is_staff = models.BooleanField(default=False)               # 사용자가 Django Admin 패널에 로그인할 수 있는지 나타냄
    is_active = models.BooleanField(default=True)               # 비/활성화 여부
    objects = UserManager()
    
    USERNAME_FIELD = 'username'                                 # 필수 요구 사항