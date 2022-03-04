from .blueprints import *
from flask import Flask
import os

BASE_DIRECTORY = os.getcwdb().decode("utf-8")
app = Flask(__name__, static_folder=os.path.join(BASE_DIRECTORY, "static"),
            template_folder=os.path.join(BASE_DIRECTORY, "templates"),
            root_path=BASE_DIRECTORY)


app.register_blueprint(main, url_prefix="/")
app.register_blueprint(oauth, url_prefix="/")