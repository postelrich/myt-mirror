from flask_socketio import emit
from mirror import app, socketio


@socketio.on('connect', namespace='/counter')
def counter_connect():
    emit('connected', {'msg': 'connected'})


@socketio.on('count', namespace='/counter')
def count_down():
    pass
