from flask_socketio import emit
from mirror import app, socketio
from time import sleep


@socketio.on('connect', namespace='/counter')
def counter_connect():
    emit('connected', {'msg': 'connected'})


@socketio.on('count', namespace='/counter')
def count_down(config):
    count = int(config['start'])
    while count > -1:
        emit('current_count', {'data': count})
        count -= 1
        sleep(1)
