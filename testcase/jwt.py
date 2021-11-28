import datetime
from django.contrib.auth.models import User
import jwt
from django.conf import settings

def generate_access_token(object):
    payload = {
        'id': object.pk,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        # 'user': object.usertype
    }
    access_token = jwt.encode(payload, settings.SECRET_KEY, "HS256")

    return access_token


def jwt_decode(token):
    # authorization_heaader = request.headers.get('Authorization')
    # access_token = authorization_heaader.split(' ')[1]
    payload = jwt.decode(
        token, settings.SECRET_KEY, algorithms=['HS256'])

    print("Payload ", payload)
    id = payload['id']
    user = User.objects.get(pk=id)
    if user:
        return True
    return False
