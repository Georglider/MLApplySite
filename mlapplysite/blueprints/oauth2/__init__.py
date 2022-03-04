from flask import Blueprint

oauth = Blueprint('oauth2', __name__)

from .login import *

