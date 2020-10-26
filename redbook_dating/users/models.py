from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):
    """
    User django models
    """
    login_validator = UnicodeUsernameValidator()

    nickname = models.CharField(
        _('nickname'),
        max_length=200,
        null=False,
        blank=True,
        unique=True,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=200,
        null=False,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=200,
        null=False,
        blank=True,
    )
    email = models.EmailField(
        _('email'),
        max_length=50,
        unique=True,
        null=False,
        blank=True,
    )
    phone = PhoneNumberField(
        unique=True,
        null=True,
        blank=True,
        verbose_name='номер телефона'
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Return full name for the user."""
        return f'{self.first_name} {self.last_name}'

    def get_username(self):
        """Return username for the user."""
        return self.nickname

    def __str__(self):
        return f'Пользователь id={self.id} email={self.email}'
