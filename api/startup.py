from flask import Flask
from flask_cors import CORS

import ms_config

app = Flask(__name__)

ALLOWED_ORIGINS = [""] if ms_config.PRODUCTION else ["http://localhost:3000/*"]
CORS(app, resources={"/*": {"origins": ALLOWED_ORIGINS}})