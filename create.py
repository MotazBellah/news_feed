import os
import csv
from flask import Flask
from database_setup import *

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def load_channel(file_name):
    with open(r'{}'.format(file_name), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            # print(len(row))
            channel = Channel(title=row[0], link=row[1],
                              atom=row[2], description=row[3],
                              language=row[4], copyright=row[5],
                              lastBuildDate=row[6], img_title=row[7],
                              img_url=row[8], img_link=row[9])
            # print(channel.title)
            db.session.add(channel)
            db.session.commit()

# def load_channel2():
#     url = 'https://github.com/MotazBellah/news_feed/blob/master/news.csv'
#     response = urlopen(url, 'r')
#     reader = csv.reader(response)
#     next(reader)
#     for row in reader:
#         channel = Channel(title=row[0], link=row[1],
#                               atom=row[2], description=row[3],
#                               language=row[4], copyright=row[5],
#                               lastBuildDate=row[6], img_title=row[7],
#                               img_url=row[8], img_link=row[9])
#         db.session.add(channel)
#         db.commit()



def load_item(file_name):
    with open(r'{}'.format(file_name), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row)
            item = Item(title=row[0], link=row[1], guid=row[2],
                        atom=row[3], description=row[4],
                        creator=row[5], pubDate=row[6],
                        category=row[7], media_content=row[8],
                        media_credit=row[9], media_description=row[10])
            db.session.add(item)
            db.session.commit()

def load_data():
    load_channel('news.csv')
    load_channel('news2.csv')
    load_item('item.csv')
    load_item('item2.csv')

def main():
    db.create_all()
    load_data()
    # load_channel2()

if __name__ == "__main__":
    with app.app_context():
        main()
        # load_data()
