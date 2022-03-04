from mlapplysite.blueprints.oauth2 import oauth
import requests
from flask import Flask, request, redirect
from .oauth import Oauth


@oauth.route("/", methods=["get"])
def index():
    return redirect(Oauth.discord_login_url)


@oauth.route("/login", methods=["get"])
def login():
    code = request.args.get("code")
    at = Oauth.get_access_token(code)

    user_json = Oauth.get_user_json(at)
    username = user_json.get("username"), user_json.get("discriminator")
    print(f"{username}")
    return redirect('/test')
