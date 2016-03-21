# -*- coding: utf-8 -*-
from flask import Blueprint, Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, json

import types


commands_api = Api(Blueprint('commands_api', __name__)) # pylint: disable=invalid-name


@app.route('/sendCommand', methods=['POST'])
def sendCommand():

    # read the posted values from the UI
    display = request.json['display']
    command = request.json['command']
    return json.dumps({ "display" : display, "command" : command})