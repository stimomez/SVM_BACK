from decouple import config
import datetime
import pytz
import jwt


class Security():
    secret = config('JWT_KEY')
    tz = pytz.timezone('America/Bogota')

    @classmethod
    def generate_token(cls, authenticated_user):

        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=480),
            'id': authenticated_user['id'],
            'username': authenticated_user['username'],
            'role_id': authenticated_user['role_id']
        }
        return jwt.encode(payload, cls.secret, algorithm='HS256')

    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' in headers.keys():
            autorization = headers['Authorization']
            encoded_token = autorization.split(' ')[1]

            try:
                payload = jwt.decode(
                    encoded_token, cls.secret, algorithms=['HS256'])
                return payload
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                return False
        return False
