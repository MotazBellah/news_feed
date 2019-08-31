from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
from flask import session as login_session
from database_setup import db as d
import os


app = Flask(__name__)
app.secret_key="sdfdsuperfdlkngflkjnlkbgirlsdessexyasspussyfucfgfgfhhyah!!!!!dfghhm;glhjkhjl,.jk"
app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"

# app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route('/', methods=['GET', 'POST'])
def show_channel():
    channels = Channel.query.all()
    for i in set(channels):
        print(i.title)
    return render_template('channel.html', channels=channels[:2])


@app.route('/news/<int:channel_id>', methods=['GET', 'POST'])
def show_news(channel_id):
    news = Item.query.filter_by(channel_id=channel_id).all()
    if request.method == 'POST':
        if request.form['rate']:
            id = int(request.form['id'])
            selected_item = Item.query.filter_by(id=id).first()
            selected_item.rate = request.form['rate']
            print(Item_rating.rate)
            db.session.add(selected_item)
            db.session.commit()
    return render_template('news.html', news=news)


if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    PORT = int(os.environ.get('PORT', 8000))
    app.debug = True
    app.run(host='0.0.0.0', port=PORT)
