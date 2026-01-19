from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Укажите название"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Укажите описание"
    )
    preview = models.ImageField(
        upload_to="materials/course_preview",
        null=True,
        blank=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Укажите название"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Укажите описание"
    )
    preview = models.ImageField(
        upload_to="materials/course_preview",
        null=True,
        blank=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    link = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка",
        help_text="Укажите ссылку на видео",
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
