from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


class User(AbstractBaseUser, PermissionsMixin):
    """
    User django models
    """
    login_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
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
    phone = PhoneNumberField(unique=True, null=True, blank=True)

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        """Return full name for the user."""
        return f'{self.first_name} {self.last_name}'

    def get_username(self):
        """Return username for the user."""
        return self.username

    def __str__(self):
        return f'Пользователь id={self.id} username={self.username}'
