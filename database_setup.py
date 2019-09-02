from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import TypeDecorator, Unicode

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
    rate = db.Column(db.Float, default=0.0)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship(Channel)

    @property
    def serialize(self):
        return {
            'title': self.title,
            'id': self.id,
            'link': self.link,
            'description': self.description,
            'creator': self.creator,
            'pubDate': self.pubDate,
            'category': self.category,
            'media_content': self.media_content,
            'media_credit': self.media_credit,
            'media_description': self.media_description,
            'rate': self.rate
            }


# #
# class Corn(db.Model):
#     __tablename__ = "apscheduler_jobs"
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250))
#     link = db.Column(db.String(250))
#     description = db.Column(db.String(250))
#     creator = db.Column(db.String(250))
    # pubDate = db.Column(db.String(250))
    # category = db.Column(db.String(250))
    # media_content = db.Column(db.String(250))
    # media_credit = db.Column(db.String(250))
    # media_description = db.Column(db.String(250))
    # rate = db.Column(db.Float, default=0.0)
    #
    # @property
    # def serialize(self):
    #     return {
    #         'title': self.title,
    #         'link': self.link,
    #         'description': self.description,
    #         'creator': self.creator,
    #         'pubDate': self.pubDate,
    #         'category': self.category,
    #         'media_content': self.media_content,
    #         'media_credit': self.media_credit,
    #         'media_description': self.media_description,
    #         'rate': self.rate
    #         }
