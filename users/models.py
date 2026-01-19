from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True, verbose_name="email", help_text="Введите вашу почту"
    )
    username = None
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=30, null=True, verbose_name="Город", help_text="Введите ваш город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        null=True,
        blank=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

