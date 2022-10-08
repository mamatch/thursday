from . import db


class Tweet(db.Model):
    __tablename__ = "tweets"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    image = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime)

    def __repr__(self):
        return self.text
