from .db import db

# ItemDetail = db.Table('games_gamejams',
#                       db.Column('id', db.Integer, primary_key=True),
#                       db.Column('gameId', db.Integer, db.ForeignKey('Item.id')),
#                       db.Column('gamejamId', db.Integer, db.ForeignKey('Detail.id')),
#                       db.column('gamePlacement'))


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    blurb = db.Column(db.Text(1028))
    avatarUrl = db.Column(db.Text(1028))
    githubUrl = db.Column(db.Text(1028))
    websiteUrl = db.Column(db.Text(1028))
    # gameJams = db.relationship('Gamejam', secondary=ItemDetail, backref='Game')

    def to_dict(self):
        return {
            "id": self.id,
            "gameJamId": self.username,
            "name": self.email,
            "blurb": self.blurb,
            "avatarUrl": self.avatarUrl,
            "githubUrl": self.githubUrl,
            "websiteUrl": self.websiteUrl
        }
