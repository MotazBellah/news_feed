from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import TypeDecorator, Unicode

db = SQLAlchemy()



class CoerceUTF8(TypeDecorator):
    """Safely coerce Python bytestrings to Unicode
    before passing off to the database."""

    impl = Unicode

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            value = value.decode('utf-8')
        return value

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
    title = db.Column(db.String(250))
    link = db.Column(db.String(250))
    guid = db.Column(db.String(250))
    atom = db.Column(db.String(250))
    description = db.Column(db.String(250))
    creator = db.Column(db.String(250))
    pubDate = db.Column(db.String(250))
    category = db.Column(db.String(250))
    media_content = db.Column(db.String(250))
    media_credit = db.Column(db.String(250))
    media_description = db.Column(db.String(250))
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship(Channel)
