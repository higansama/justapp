from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from book.models import Books

class Command(BaseCommand):

  def handle(self, *args, **options):
    data = [
      {"judul": "buku satu"},
      {"judul": "buku dua"},
      {"judul": "buku tiga"},
      {"judul": "buku empat"},
      {"judul": "buku lima"},
      {"judul": "buku enam"},
      {"judul": "buku tujuh"},
      {"judul": "buku delapan"},
    ]
    i = 1
    for buku in data:
      b = Books.objects.create(judul=buku["judul"])
      print("Buku ke " , i , " dibuat, id ", b)
      i += 1