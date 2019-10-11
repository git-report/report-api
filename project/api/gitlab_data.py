from flask import Blueprint, jsonify, request
from os.path import join, dirname, realpath
from requests.exceptions import HTTPError
from project import db
import json
import sys


from project.api.models import Hand, Card

gitlab_data_blueprint = Blueprint('gitlab_data', __name__)

host = "https://gitlab.com"
api_path = "/api/v4/projects/"

# https://gitlab.com/api/v4/projects/9363838/issues?scope=all
# project_id = "9363838"
# parameters = "issues?scope=all"

def make_request_url(project_id, parameters):
    return host+api_path+project_id+'/'+parameters

@gitlab_data_blueprint.route("/get_issues", methods=["GET"])
def get_issues():
    request_url = make_request_url("9363838", "issues?scope=all")
    issues = requests.get(request_url, headers=headers, verify=False)
    issues_json = issues.json()
    insert_issues(issues_json)

def insert_issues(issues_json):
    for i in result:
        # atributos do request
        id_result = i['id']
        issue_id = i['iid']
        title = i['title']
        description = i['description']
        project_id = i['project_id']
        labels = i['labels']
        #link = repository + "issues" + "/" + str(issue_id)

        label = Label.query.filter_by(name=name).first()
        db.session.add(Issue(issue_id=issue_id,
                            labels=labels,
                            title=title,
                            description=description,
                            project_id=project_id))
        db.session.commit()

    return lista_retorno


@hands_blueprint.route("/post_hands", methods=["POST"])
def post_hands():
    try:
        hands_json = json.loads(request.get_json())

        for hand in hands_json:
            player_id = hand['player_id']
            round_id = hand['round_id']
            cards = hand['cards']

            for card in cards:
                value = card['value']
                suit = card['suit']

                card = Card.query.filter_by(value=value, suit=suit).first()
                db.session.add(Hand(player_id=player_id, card_id=card.id, round_id=round_id))

        db.session.commit()

    except HTTPError:
        return jsonify({"message": "NOT FOUND"}), 404
    else:
        return jsonify({"message": "Hands Recived"}), 200
