from sqlalchemy.sql import func
from project import db

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    issue_id = db.Column(db.Integer, nullable=False)
    labels =  db.Column(db.String(2000))
    title = db.Column(db.String(250),  nullable=False)
    description = db.Column(db.String(2000))
    project_id = db.Column(db.Integer, nullable=False)

    def __init__(self, issue_id, labels, title, description, project_id):
        self.issue_id = issue_id
        self.labels = labels
        self.title = title
        self.description = description
        self.project_id = project_id

# class Label(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(100),  nullable=False)
#     issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'),nullable=False)
#
#     def __init__(self, name):
#         self.name = name
#
# issue_labels = db.Table('issue_labels',
#                db.Column('issue_id', db.Integer, db.ForeignKey('issue.id'), primary_key=True),
#                db,Column('label_id', db.Integer, db.ForeignKey('label.id'), primary_key=True)
#             )
#
# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))
#
# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
