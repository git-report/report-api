from sqlalchemy.sql import func
from project import db

class Issue(db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    issue_id = db.Column(db.Integer, nullable=False)
    labels =  db.Column(db.relationship('Label', backref='issue', lazy=True))
    title = db.Column(db.String(250),  nullable=False)
    description = db.Column(db.String(2000))
    project_id = db.Column(db.Intege, nullable=False)

    def __init__(self, id, title, project_id):
        self.id = id
        self.title = title
        self.project_id = project_id

class Label(db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100),  nullable=False)

    def __init__(self, name):
        self.name = name
