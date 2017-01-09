from copy import deepcopy
from flask import render_template, request
from mirror import app


@app.route('/')
@app.route('/index')
def index():
    print(app.config['module_rows'])
    return render_template("index.html", module_rows=app.config['module_rows'],
                           layout_mode=bool(request.args.get('layout', False)))
