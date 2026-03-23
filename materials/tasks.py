from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_course_update_email(email, course_title):
    send_mail(
        subject=f"Курс {course_title} обновлён",
        message=f"Материалы курса {course_title} были обновлены.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )