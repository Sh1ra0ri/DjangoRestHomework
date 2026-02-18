from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


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


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    date = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)

    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        null=True,
        related_name="paid_course",
        blank=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        null=True,
        related_name="paid_lesson",
        blank=True,
    )
    total = models.PositiveSmallIntegerField(verbose_name="Сумма оплаты")

    PAYMENT_METHOD_CHOICES = [
        ("Наличные", "Наличные"),
        ("Перевод на счет", "Перевод на счет"),
        ("Stripe", "Оплата картой онлайн"),
    ]
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name="Способ оплаты"
    )

    session_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="ID сессии Stripe"
    )
    link = models.URLField(
        max_length=500, blank=True, null=True, verbose_name="Ссылка на оплату Stripe"
    )
    status = models.CharField(
        max_length=50,
        default="pending",
        verbose_name="Статус оплаты",
        choices=[
            ("pending", "Ожидает оплаты"),
            ("paid", "Оплачено"),
            ("failed", "Ошибка оплаты"),
        ],
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user.email} - {self.total} руб."
