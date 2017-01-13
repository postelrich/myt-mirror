import os
from copy import deepcopy
from flask import render_template, request, send_from_directory
from mirror import app


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
