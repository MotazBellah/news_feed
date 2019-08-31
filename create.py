import os
import csv
from urllib.request import urlopen
from flask import Flask
from database_setup import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def load_channel(file_name):
    with open(r'{}'.format(file_name), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(len(row))
            channel = Channel(title=row[0], link=row[1],
                              atom=row[2], description=row[3],
                              language=row[4], copyright=row[5],
                              lastBuildDate=row[6], img_title=row[7],
                              img_url=row[8], img_link=row[9])
            db.session.add(channel)
            db.commit()

def load_channel2():
    url = 'https://github.com/MotazBellah/news_feed/blob/master/news.csv'
    response = urlopen(url, 'r')
    reader = csv.reader(response)
    next(reader)
    for row in reader:
        channel = Channel(title=row[0], link=row[1],
                              atom=row[2], description=row[3],
                              language=row[4], copyright=row[5],
                              lastBuildDate=row[6], img_title=row[7],
                              img_url=row[8], img_link=row[9])
        db.session.add(channel)
        db.commit()



def load_item(file_name):
    with open(r'{}'.format(file_name), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            item = Item(title=row[0], link=row[1],
                        atom=row[2], description=row[3],
                        creator=row[4], pubDate=row[5],
                        category=row[6], media_content=row[7],
                        media_credit=row[8], media_description=row[9])
            db.session.add(item)
            db.commit()

def load_data():
    load_channel('https://github.com/MotazBellah/news_feed/blob/master/news.csv')
    load_channel('news2.csv')
    load_item('item.csv')
    load_item('item2.csv')

def main():
    db.create_all()
    # load_data()
    load_channel2()

if __name__ == "__main__":
    with app.app_context():
        main()
