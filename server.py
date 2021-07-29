#!/usr/bin/python3

import flask
import flask_login as fl
import argparse

from pages_standard import standardPages
from pages_api import pagesApi
from subpages_dashboard import subpagesDashboard
from pages_loginmanagement import pagesLoginManagement

import database as db

app = flask.Flask("OH-MY-Nemesis")
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
loginManager = fl.LoginManager()

@loginManager.user_loader
def load_user(userName):
    '''Setup the user/login manager'''
    return db.getUserByName(userName)

#@app.route('/static/<path:path>')
#def static(path):
#    '''Configure sending of static files'''
#    return flask.send_from_directory('static', path)

@app.before_first_request
def init():
    '''Do nessesary initialization jobs'''
    loginManager.init_app(app)
    app.register_blueprint(standardPages)
    app.register_blueprint(pagesApi)
    app.register_blueprint(subpagesDashboard)
    app.register_blueprint(pagesLoginManagement)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='None',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--interface', default="localhost",
                help='Interface on which flask (this server) will take requests on')
    parser.add_argument('--port', default="5000",
                help='Port on which flask (this server) will take requests on')
    args = parser.parse_args()
    app.run(host=args.interface, port=args.port)
