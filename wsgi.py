from flask import Flask, render_template

import os, string
import datetime
from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
# import requests
# import sendgrid
# from sendgrid.helpers.mail import *
# from passlib.hash import sha256_crypt

## Internally developed modules
import models

app = Flask(__name__)
app.config.from_pyfile('wsgi.cfg')
models.db.init_app(app)


@app.before_request
def before_request():
    g.branding = {
        "root_url": "www.brand.com",
        "brand_name": "Brand, Inc.",
        "default_title": "Our company pitch here!"
    }
    g.client = {
        "browser": request.user_agent.browser,
        "ip_address": request.headers.get("x-forwarded-for")
    }


@application.route("/")
def index():
    return render_template("base_nav.html")

if __name__ == "__main__":
    app.run()
