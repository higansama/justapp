from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):

  def handle(self, *args, **options):
      u = User()
      u.username = "admin"
      u.password = make_password("admin123")
      u.is_active = True
      u.save()
      self.stdout.write("Username 'admin' dan password 'admin123' telah dibuat")