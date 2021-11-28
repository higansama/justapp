from typing import List
from django.http import response
from ninja import Router
from django.contrib.auth.models import User
from ninja.params_functions import Form
from .schema import *
from .models import *

private = Router()


@private.post("private/book", response=BookObject)
def CreateBook(request, item: FormBook = Form(...)):
    buku = Books()
    buku.judul = item.judul
    buku.save()
    return buku


@private.get("private/book", response=List[BookObject])
def GetAllBook(request):
    books = Books.objects.all()
    return books


@private.get("private/book/pagination", response=Pagination)
def BookPagination(request, limit: int = 10):
    books = Books.objects.all()
    panjang = len(books)
    if limit > panjang:
        limit = panjang
    return Pagination(count=panjang, buku=books[:limit])


@private.patch("private/book/{id}")
def EditBook(request, id: int, form: FormBook):
    buku = Books.objects.get(pk=id)
    buku.judul = form.judul
    buku.save()
    print("buku =>", buku)
    return {"message": "success"}


@private.delete("private/book/{id}")
def EditBook(request, id: int):
    buku = Books.objects.filter(pk=id)
    buku.delete()
    return {"message": "success"}


public = Router()


@public.get("public/book", response=List[BookObject])
def GetQueryBook(request, q=""):
    if q != "":
        return Books.objects.filter(judul__icontains=q)
    else:
        return Books.objects.all()


@public.get("public/book/{slug}", response=BookObject)
def GetSlugBook(request, slug: str):
    return Books.objects.get(slug__contains=slug)
