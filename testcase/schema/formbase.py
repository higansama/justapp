from datetime import date
from ninja import Form, Schema


class LoginForm(Schema):
  username :str
  password :str

class UserOutResponse(Schema):
  username: str

class JwtToken(Schema):
  token :str
