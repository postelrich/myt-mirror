import os
from flask import Flask
from flask_socketio import SocketIO
from mirror.utils import load_config

app = Flask(__name__)
socketio = SocketIO(app)

config_path = os.path.expanduser("~/prj/myt-mirror/mirror_config.json")
config = load_config(config_path)
app.config.update(config)

import mirror.views
