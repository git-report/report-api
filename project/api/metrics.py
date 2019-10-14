from flask import Blueprint, jsonify, request
from os.path import join, dirname, realpath
from requests.exceptions import HTTPError
from project import db
import json
import sys
import requests

from project.api.models import Issue

metrics_blueprint = Blueprint('metrics', __name__)



@metrics_blueprint.route("/metrics/issues/average_time", methods=["GET"])
def get_issues_average_time():
    return jsonify({
                'message': 'Rota criada com sucesso'
            }), 200
