from config.environment import env
if env("run_socketio") == 'True' or env("run_socketio") == "true":
    from app import sio

    @sio.on("connnect")
    def connect(auth):
        print("connected", auth)
        return True
    @sio.on('disconnect')
    def test_disconnect():
        print('Client disconnected')

