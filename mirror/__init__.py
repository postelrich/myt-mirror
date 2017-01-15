import importlib
import jinja2
import os
from flask import Flask
from flask_socketio import SocketIO
from mirror.utils import load_config

app = Flask(__name__)
socketio = SocketIO(app)

config_path = os.path.expanduser("~/prj/myt-mirror/mirror_config.json")
config = load_config(config_path)
app.config.update(config)
loaders = [app.jinja_loader]
for name in config['module_names']:
    loaders.append(jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'modules', name)))
app.jinja_loader = jinja2.ChoiceLoader(loaders)

import mirror.views
import mirror.modules.counter
# for m in config['modules']:
    # if 'py' in m:
        # print(m['name'])
        # globals()[m['name']] = importlib.import_module('mirror.modules', m['name'])
