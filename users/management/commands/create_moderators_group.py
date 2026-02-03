from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Создание группы модераторов'

    def handle(self, *args, **kwargs):
        Group.objects.get_or_create(name='Модераторы')
        self.stdout.write(self.style.SUCCESS('Группа "Модераторы" создана'))