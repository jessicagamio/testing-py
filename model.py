from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    Game.query.delete()

    game1 = Game(name="Game One", description="This is Game One")
    game2 = Game(name="Game Two", description="This is Game Two")
    game3 = Game(name="Game Three", description="This is Game Three")

    db.session.add_all([game1, game2, game3])
    db.session.commit()



if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
