#!/usr/bin/env python
# -*- coding: utf-8 -*-
# heroku logs -a api-onlineloans -t --source app

import os
from uuid import uuid4 as guid

from random import choice, randint
from time import sleep
from datetime import datetime

from flask import Flask
from flask import request, Response
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

    header = request.headers
    form = request.get_json()

    user = dict(
        name = form.get('name'),
        phone = form.get('phone'),
        email = form.get('email'),
        device_id = header.get('X-Device-Id'),
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    utm_source = form.get('utm').get('utm_source')
    utm_medium = form.get('utm').get('utm_medium')

    if utm_source:
        user['utm_source'] = utm_source

    if utm_medium:
        user['utm_medium'] = utm_medium


    keys = user.keys()
    values = list(map(lambda k: user[k] ,keys))
    values_str = "\'" + "\', \'".join(values) + "\'"
    sql = f"INSERT INTO users ({', '.join(keys)}) VALUES ({values_str})"
    DBFetcher().execute(sql)

    success = json(
        token = guid().hex
    ), 200

    error404 = json(
        code = 404,
        message = "Проблемы сервака с кодом 404. Для проверки накидываю еще текстик"
    ), 404

    return choice([success, success, success, error404])


@app.route('/loans', methods=['GET'])
def request_loans():

    sql = "SELECT * FROM loans ORDER BY id ASC"
    data = DBFetcher().fetch(sql)

    success = json(
        data = data[0:randint(0, len(data))+1]
    ), 200

    error404 = json(
        code = 404,
        message = "Проблемы сервака с кодом 404. Для проверки накидываю еще текстик"
    ), 404

    error401 = json(
        code = 401,
        message = "Вылогин по коду 401. Для проверки еще текстик"
    ), 401

    return choice([success, success, success, success, error404, error401])


# -----------------------------------------------------------------------

@app.route('/<path:option>')
def index(option=None):

    # appstore/.well-known/assetlinks.json

    static = {
        'favicon.ico': 'image/vnd.microsoft.icon',
        'assetlinks.json': 'application/json',
        'cashwagon.png': 'image/png',
        'kreditpintar.png': 'image/png'
    }

    option = option.split('/')[-1]
    if static.get(option) is not None:    
        static_path = os.path.join(app.root_path, 'static')
        return send_from_directory(static_path, option, mimetype=static.get(option))

    return render_template(f'{option}.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
