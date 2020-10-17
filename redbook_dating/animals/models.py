from django.db import models
from django.utils.translation import gettext_lazy as _


class Species(models.Model):
    """Animals species django model."""
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Класс',
    )


class SubSpecies(models.Model):
    """Animals subspecies django model."""
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Подкласс')
    parent_species = models.ForeignKey(
        'Species',
        on_delete=models.PROTECT,
        verbose_name='Родительский класс',
    )


class Animal(models.Model):
    """Red-book Animal django model."""
    name = models.CharField(max_length=200, verbose_name='Кличка')
    age = models.IntegerField(verbose_name='Возраст', null=True, blank=True)

    class Gender(models.TextChoices):
        MAN = 'М', _('Man')
        WOMAN = 'W', _('Woman')

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        verbose_name='Пол',
        null=False,
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Владелец'
    )
    subspecies = models.ForeignKey(
        'SubSpecies',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Подкласс'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )

    def __str__(self):
        return (
            f'Животное: {self.name}'
            f' Подвид: {self.subspecies}'
            f' Владелец: {self.user}'
        )
