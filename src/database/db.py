import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def getConnection():
    try:
        return psycopg2.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB'),
            port=config('DB_PORT')
        )
    except DatabaseError as ex:
        raise ex
