import datetime, jwt, time
from django.conf import settings

def get_time_delta(hours=1, days=0):
    current_time = datetime.datetime.now()
    expiration_time = current_time + datetime.timedelta(days=days, hours=hours)
    exp_timestamp = int(expiration_time.timestamp())
    return exp_timestamp

def generate_jwt_token(user, hours=1, days=0):
    exp_timestamp= get_time_delta(hours=hours, days=days)
    
    encoded_token = {
        "id": user.id, 
        "username": user.username,
        "email": user.email,
        "iat": int(time.time()) ,
        "exp": exp_timestamp
    }

    token = jwt.encode(encoded_token, settings.SECRET_KEY, algorithm="HS256")

    return token