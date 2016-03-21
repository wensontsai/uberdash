# import os
# # from flask.ext.sqlalchemy import SQLAlchemy
# from logging import StreamHandler
# from sys import stdout
# from flask import Flask

# # db = SQLAlchemy()

# def create_app():
#     from api.commands import commands_api
#     from views.index import index_view

#     app = Flask(__name__)
#     # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

#     app.register_blueprint(commands_api.blueprint, url_prefix='/api')
#     app.register_blueprint(index_view)

#     db.init_app(app)

#     handler = StreamHandler(stdout)
#     app.logger.addHandler(handler)
#     return app

#!/usr/bin/python
# 
# Gulliver
#
# Demo application for Gulliver's Gate management system

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, json

from flask_restful import Resource, Api
import types

app = Flask(__name__, static_url_path='')
api = Api(app)

#
# main() function
#

#
# views SERVED BY FLASK
#
@app.route('/')
def root():
    return app.send_static_file('index.html')




#
# API routes
#
@app.route('/api/queryAllDisplays', methods=['GET'])
def queryAllDisplays():
    # query DB
    displays = ''

    # send back to client-side
    return json.dumps({ 'displays' : displays })


@app.route('/api/sendCommand', methods=['POST'])
def sendCommand():
    # read the posted values from the UI
    display = request.json['display']
    command = request.json['command']

    # persist to MYSQL database

    # send back to client-side
    return json.dumps({ 'display' : display, 'command' : command})







if __name__ == '__main__':
        app.run(debug=True, port=3001)