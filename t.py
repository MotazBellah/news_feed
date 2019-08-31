import csv
from flask import Flask
from database_setup import *

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def load_item(file_name, channel_id):
    with open(r'{}'.format(file_name), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row)
            item = Item(channel_id=channel_id)
            db.session.add(item)
            db.session.commit()
load_item('item.csv', 1)
load_item('item2.csv', 2)
