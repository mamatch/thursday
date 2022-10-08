from . import db


class Tweet:
    text = db.Column(db.String(255))
    image = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime)

    def __repr__(self):
        return self.text
