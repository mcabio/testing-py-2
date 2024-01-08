from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    # print("FIXME")
    Game.query.delete()

    gttr = Game(game_id=1, name='Ticket to Ride', description='a cross-country train adventure')
    gpg = Game(game_id=2, name='Power Grid', description='supply the most cities with power')
    gal = Game(game_id=3, name='Amazing Labyrinth', description='move around the shifting paths of the labyrinth in a race to collect various treasures')
    gpof = Game(game_id=4, name='Princes of Florence', description='attract artists and scholars trying to become the most prestigious family in Florence')
    ga = Game (game_id=5, name='Agricola', description='farmers sow, plow the fields, collect wood, and feed their families')
    
    db.session.add_all([gttr, gpg, gal, gpof, ga])
    db.session.commit()

def connect_to_db(app, db_uri="postgresql:///games"):
# def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
