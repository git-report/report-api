from flask import Blueprint, jsonify, request
from os.path import join, dirname, realpath
from requests.exceptions import HTTPError
from project import db
import json
import sys
import requests

from project.api.models import Issue

gitlab_data_blueprint = Blueprint('gitlab_data', __name__)

# regex=http+s?:\/\/.*gitlab.*\.com.*\/

host = "https://gitlab.com"
api_path = "/api/v4/projects/"
headers = {'PRIVATE-TOKEN': 'faighHd8DEgVxBFVfxTU'}
# project_id = "9363838"
# parameters = "issues?scope=all"

def make_request_url(project_id, parameters):
    return host+api_path+project_id+'/'+parameters

@gitlab_data_blueprint.route("/get_issues", methods=["GET"])
def get_issues():
    request_url = make_request_url("9363838", "issues?scope=all")
    issues = requests.get(request_url, headers=headers, verify=False)
    issues_json = issues.json()
    print("issues json")
    print(issues_json)
    insert_issues(issues_json)
    return jsonify(issues_json), 200

def insert_issues(issues_json):
    for i in issues_json:
        # atributos do request
        id_result = i['id']
        issue_id = i['iid']
        title = i['title']
        description = i['description']
        project_id = i['project_id']
        labels = i['labels']

        db.session.add(Issue(issue_id=issue_id,
                            labels=labels,
                            title=title,
                            description=description,
                            project_id=project_id))
        db.session.commit()
