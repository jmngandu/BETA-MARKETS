from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
import random
import string

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    number = models.CharField(max_length=15, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    email = models.EmailField(unique=True)  # Ensure the email field is unique

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_users',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_users',
        blank=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    class Meta:
        unique_together = ('email',)  # This should be fine with the unique field set

    def __str__(self):
        return self.email

    def generate_verification_code(self):
        return ''.join(random.choices(string.digits, k=6))
