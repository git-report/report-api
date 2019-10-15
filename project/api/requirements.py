from flask import Blueprint, jsonify, request
from os.path import join, dirname, realpath
from requests.exceptions import HTTPError
from project import db
import json
import sys
import requests

from project.api.models import Issue

requirements_blueprint = Blueprint('requirements', __name__)



@requirements_blueprint.route("/requirements/stories", methods=["GET"])
def get_stories():
    return jsonify({
                'message': 'Rota criada com sucesso'
            }), 200
