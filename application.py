#!/usr/bin/env python
# -*- coding: utf-8 -*-
# heroku logs -a api-onlineloans -t --source app

import os
from uuid import uuid4 as guid

from random import choice, randint
from time import sleep
from datetime import datetime, timedelta

from flask import Flask
from flask import request, Response, redirect
from flask import render_template, send_from_directory
from flask import jsonify as json

from adapters.dbconnector import DBFetcher

app = Flask(__name__)

# -----------------------------------------------------------------------


@app.after_request
def after_request(response):

    headers = [
        'X-Country-Code',
        'X-Security-Token',
        'X-Device-Id',
        'X-Auth-Token'
    ]

    json_headers = dict()
    for h_name in headers:
        json_headers[h_name] = request.headers.get(h_name)

    req = f'REQUEST {request.method} {request.path}'
    hed = f'HEADERS {json_headers}'
    bod_g = f'BODY -> {request.get_json()}'
    bod_p = f'BODY <- {response.get_json()}'

    print(req + '\n' + hed + '\n' + bod_g + '\n' + bod_p)

    sleep(0.5)
    return response


# -----------------------------------------------------------------------


@app.route('/form', methods=['POST'])
def request_form():

    success = {
        "token": guid().hex
    }

    error = {
        "code": 39203,
        "message": "Text"
    }

    return json(success)


@app.route('/loans', methods=['GET'])
def request_loans():

    success = {
        "data": [
            {
                "name": "Text",
                "icon_url": "https://via.placeholder.com/200/0000FF/FFFFFFFF",
                "amout": {
                    "currency": "USD",
                    "min": 1,
                    "max": 9999
                },
                "term": {
                    "min": 1,
                    "max": 99,
                    "type": "d"
                },
                "discount": True,
                "description": "Text",
                "stars": 4.2,
                "action_url": "http://"
            }
        ]
    }

    error = {
        "code": 39203,
        "message": "Text"
    }

    return json(success)


# -----------------------------------------------------------------------

@app.route('/<option>')
def index(option=None):

    static = {
        'favicon.ico': 'image/vnd.microsoft.icon',
        '.well-known/assetlinks.json': 'application/json'
    }

    if static.get(option) is not None:
        static_path = os.path.join(app.root_path, 'static')
        return send_from_directory(static_path, option, mimetype=static.get(option))

    return render_template(f'{option}.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
