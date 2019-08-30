from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Channel(db.Model):
    __tablename__ = "channel"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    link = db.Column(db.String())
    atom = db.Column(db.String())
    description = db.Column(db.String())
    language = db.Column(db.String())
    copyright = db.Column(db.String())
    lastBuildDate = db.Column(db.String())
    img_title = db.Column(db.String())
    img_url = db.Column(db.String())
    img_link = db.Column(db.String())



class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    link = db.Column(db.String())
    atom = db.Column(db.String())
    description = db.Column(db.String())
    creator = db.Column(db.String())
    pubDate = db.Column(db.String())
    category = db.Column(db.String())
    media_content = db.Column(db.String())
    media_credit = db.Column(db.String())
    media_description = db.Column(db.String())
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship(Channel)
