from flask import Flask
from flask_socketio import SocketIO

def init(app: Flask):
    sio = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False)
    return sio