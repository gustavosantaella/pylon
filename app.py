from flask import Flask
from config.environment import env
from config.modules import register_modules
from src.routes.app import web, api
from mongoengine import connect
from flask_bcrypt import Bcrypt
from config.socketIO import init as init_socketIO
try:
    app = Flask(import_name=__name__, static_folder='./storage')
    # app.config["CACHE_TYPE"] = "null"
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    bycrypt = Bcrypt(app)
    db = connect(host=env('MONGO_URI'))
    if env("run_socketio") == 'True' or env("run_socketio") == "true":
        sio = init_socketIO(app)
        print("sio is running")
    register_modules()
    

    for bluprint in [web, api]:
        app.register_blueprint(bluprint)

except Exception as e:
    print("An error ocurred to init app")
    print(e)

if __name__ == '__main__':
    if env("run_socketio") == 'True' or env("run_socketio") == "true":
        sio.run("0.0.0.0", debug=True)
    else:
        app.run("0.0.0.0", debug=True)
