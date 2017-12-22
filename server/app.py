"""This module contains basic functions to instantiate the BigchainDB API.

The application is implemented in Flask and runs using Gunicorn.
"""
import os

from flask import (
    Flask, request, render_template, redirect, url_for,
)
from flask.ext.cors import CORS

from server.lib.api.views import api_views



# password_hash_dict = {
#     '0':'1f489582f7ea4c208b70219a2bb6a322227a7516630530a10ed7f2710cfbe447',
#     '1':'0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e',
# }


def create_app(debug):
    """Return an instance of the Flask application.

    Args:
        debug (bool): a flag to activate the debug mode for the app
            (default: False).
    """
    app = Flask(__name__)
    hostname = os.environ.get('DOCKER_MACHINE_IP', 'localhost')
    if not hostname:
        hostname = 'localhost'
    origins = ('^(https?://)?(www\.)?({}|0|0.0.0.0|dimi-bat.local|'
               'localhost|127.0.0.1)(\.com)?:\d{{1,5}}$').format(hostname),
    CORS(app,
         origins=origins,
         headers=(
            'x-requested-with',
            'content-type',
            'accept',
            'origin',
            'authorization',
            'x-csrftoken',
            'withcredentials',
            'cache-control',
            'cookie',
            'session-id',
            ),
         supports_credentials=True,
         )

    app.debug = debug

    app.register_blueprint(api_views, url_prefix='/api')
    return app


# @app.route('/authorize', methods=['GET', 'POST'])
# def get_password():
#     if request.method == 'GET':
#         return render_template('password_form.html')
#     elif request.method == 'POST':
#         if 'password' in request.form:
#             user = request.form['user'].strip()
#             password = request.form['password'].strip().encode('utf-8')
#             password_hash = hashlib.sha256(password).hexdigest()
#             if user in password_hash_dict and password_hash == password_hash_dict[user]:
#                 os.environ['USER'] = user
#
#                 return 'success!'
#             else:
#                 return 'wrong password!'
#         else:
#             return 'you should enter password'


def run_flask_server():
    app = create_app(debug=True)
    app.run(host=os.environ.get('FLASK_HOST', '127.0.0.1'), port=int(os.environ.get('FLASK_PORT', 8000)))
    app.run(use_reloader=False)

if __name__ == '__main__':
    run_flask_server()
