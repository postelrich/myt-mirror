from flask import render_template
from mirror import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", module_rows=app.config['module_rows'])
