from flask import Flask
from pydocgen.main.controller import main
from pydocgen.config import configure_app
import os

app = Flask(__name__)
configure_app(app)


app.register_blueprint(main, url_prefix = '/')