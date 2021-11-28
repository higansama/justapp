from typing import List
from ninja import Schema, schema
from datetime import date


class FormBook(Schema):
  judul :str
  slug :str = None

class BookObject(Schema):
  id :int
  judul :str
  slug :str 
  date_created :date
  date_updated :date

class BookOut(Schema):
  judul :str
  slug :str
  date_created :date
  date_updated :date

class Pagination(Schema):
  count : int
  buku : List[BookObject] = None