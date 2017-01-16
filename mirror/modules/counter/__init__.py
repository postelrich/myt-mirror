"""
Simple example of how to write a python module which is started via websocket
and counts down to 0.
"""
from flask_socketio import emit
from mirror import app, socketio
from time import sleep


@socketio.on('connect', namespace='/counter')
def counter_connect():
    """Send ack for socket connection."""
    emit('connected', {'msg': 'connected'})


@socketio.on('count', namespace='/counter')
def count_down(config):
    """Count down from given number and emit updates."""
    count = int(config['start'])
    while count > -1:
        emit('current_count', {'data': count})
        count -= 1
        sleep(1)
