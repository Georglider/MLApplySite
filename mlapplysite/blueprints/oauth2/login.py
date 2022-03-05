
from mlapplysite.blueprints.oauth2 import oauth
import requests
from flask import Flask, request, redirect
from .oauth import Oauth
import sqlite3
from loguru import logger


data = sqlite3.connect("server.db", check_same_thread=False)
sql = data.cursor()
sql.execute(f'''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER,
            name TEXT
            )''')

logger.debug("Connected to database")

@oauth.route("/", methods=["get"])
def index():
    return redirect(Oauth.discord_login_url)


@oauth.route("/login", methods=["get"])
def login():
    code = request.args.get("code")
    at = Oauth.get_access_token(code)
    user_json = Oauth.get_user_json(at)
    username = user_json.get("id")
    name = user_json.get("username")
    logger.debug(f"{username}")
    print(type(username))
    sql.execute("INSERT INTO users VALUES (?,?)", (f"{username}",  name))
    data.commit()
    logger.debug(f"{username} added to database")
    return redirect('/test')
