from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import Card
from project.api.fake_data.seed import seed_database

app = create_app()

cli = FlaskGroup(create_app=create_app)

# Recreates Database
@cli.command()
def recreatedb():
    db.drop_all()
    db.create_all()
    seed_database(db)
    db.session.commit()
    



if __name__ == '__main__':
    cli()   