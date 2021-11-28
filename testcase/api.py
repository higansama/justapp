from django.http import response
from ninja import NinjaAPI
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .schema.formbase import *
from .jwt import *
from ninja.security import HttpBearer
from book.api import private as book_routers
from book.api import public as public_book_routers


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if jwt_decode(token):
            return True
            

api = NinjaAPI()
api.add_router("", book_routers,  auth=AuthBearer())
api.add_router("", public_book_routers)

@api.get("/hello", auth=AuthBearer())
def hello(request):
    return "Hello world"


@api.post("/login")
def login(request, item: LoginForm = Form(...)):
    user = authenticate(username=item.username, password=item.password)
    token = ""
    if user:
        # create jwt
        token = generate_access_token(user)
    else:
        return {"msg": "Data Invalid"}
    return {"msg": "success", "data": token}


@api.post("/auth", response=UserOutResponse,  auth=AuthBearer())
def test(request, item: JwtToken = Form(...)):
    user = jwt_decode(item.token)
    return user
