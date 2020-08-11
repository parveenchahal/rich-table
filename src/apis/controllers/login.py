import base64
from datetime import datetime
import pytz
from flask import redirect
from flask_restful import request, original_flask_make_response as make_response, ResponseBase, abort
import json
from controllers import Controller
import config
from jwt.utils import b64decode as _b64decode

class Login(Controller):

    def __init__(self):
        super().__init__(None)

    def __login(self):
        return redirect(config.LoginURL, code=302)

    def __auth(self, args: dict):
        redirect_uri = args.get("state", config.BaseURL)
        session = args.get("session", None)
        if session is not None:
            header, session_payload, sig = session.split(".")
            expiry = int(json.loads(_b64decode(session_payload))["expiry"])
            expiry = datetime.fromtimestamp(expiry, pytz.utc)
            response = make_response(redirect(redirect_uri, code=302))
            response.set_cookie('session', session, expires=expiry, secure=True, httponly=True)
            return response
        return "Session not found in params.", 403

    def get(self):
        path = request.path
        if "/login".__eq__(path):
            return self.__login()
        elif "/auth".__eq__(path):
            args = request.args
            return self.__auth(args)
        else:
            return abort(404)