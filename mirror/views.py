import os
from flask import render_template, request, send_from_directory
from flask_socketio import emit
from mirror import app, socketio


@app.route('/')
@app.route('/index')
def index():
    print(app.config['module_rows'])
    return render_template("index.html", modules=app.config['modules'], 
                           module_rows=app.config['module_rows'],
                           layout_mode=bool(request.args.get('layout', False)))


@app.route('/modules/<path:filename>')
def modules_static(filename):
    if '..' in filename:
        pass
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'modules'), filename)


# @socketio.on('connect', namespace='/counter')
# def counter_connect():
    # emit('connected', {'msg': 'connected'})
    # emit('connected', 'Connected')


# @socketio.on('count', namespace='/counter')
# def count_down(config):
    # print("count")
    # emit('current_count', {'msg': 1})
