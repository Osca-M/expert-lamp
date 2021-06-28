from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to create a superuser"""

    def handle(self, *args, **options):
        self.stdout.write('Creating super user')
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.ERROR('Super user exists'))

        else:
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@admins.com',
                password='admin'
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            self.stdout.write(self.style.SUCCESS('Super User  has been created'))