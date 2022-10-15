from datetime import datetime
from shutil import ExecError
from time import timezone
from jwt import encode, decode, ExpiredSignatureError, exceptions
from config.environment import env
from config.jwt import algorithm

default_key = env("jwt_secret_key")
class JWT:
    TOKEN_EXPIRED :str= 'Token has expired'
    ERROR_TO_ENCODE :str= 'Error to encode token'
    @staticmethod
    def encode(payload, secret_key:str | None = None) -> str:
        try:
            encoded = encode(payload=payload, key=secret_key or default_key, algorithm=algorithm)
            return encoded
        except Exception as e:
            print(e)
            raise Exception(JWT.ERROR_TO_ENCODE)
        
    @staticmethod
    def decode(encoded, secret_key:str | None = None):
        try:
            token = decode(encoded, key=secret_key or default_key, algorithms=[algorithm], options=({"exp": datetime.now()}))
            return token
        except ExpiredSignatureError as e :
            raise Exception(JWT.TOKEN_EXPIRED)