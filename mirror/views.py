from copy import deepcopy
from flask import render_template
from mirror import app


@app.route('/')
@app.route('/index')
def index():
    print(app.config['module_rows'])
    return render_template("index.html", module_rows=app.config['module_rows'])


@app.route('/layout')
def layout():
    module_rows = deepcopy(app.config['module_rows'])
    count = 1
    for i, row in enumerate(module_rows):
        if row[-1]:
            width = 0
            for module in row[-1]:
                module['name'] = "{}: {}".format(count, module.get('name', '<Unassigned>'))
                count += 1
                width += module['width']
            if width < 12:
                new_row = list(row)
                new_row[-1].append({'width': 12-width, 'name': "{}: {}".format(count,
                                                                               '<Unassigned>')})
                count += 1
        else:
            new_row = list(row)
            new_row[-1] = [{ 'width': 12, 'name': "{}: {}".format(count, '<Unassigned>')}]
            module_rows[i] = new_row
            count += 1

    return render_template("index.html", module_rows=module_rows,
                           layout_mode=True)
