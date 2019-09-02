from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
from flask import session as login_session
from database_setup import db as d
import os
import atexit
import logging
from datetime import datetime
from pytz import utc
import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
logging.basicConfig()


app = Flask(__name__)
app.secret_key="sdfdsuperfdlkngflkjnlkbgirlsdessexyasspussyfucfgfgfhhyah!!!!!dfghhm;glhjkhjl,.jk"
app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"

# app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

schedule_app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_channel():
    channels = Channel.query.all()
    for i in set(channels):
        print(i.title)
    return render_template('channel.html', channels=channels[:2])


@app.route('/news/<int:channel_id>', methods=['GET', 'POST'])
def show_news(channel_id):
    news = Item.query.filter_by(channel_id=channel_id).all()
    # if request.method == 'POST':
    #     id = int(request.form['id'])
    #     print(id)
    #     if request.form['rate']:
    #         id = int(request.form['id'])
    #         selected_item = Item.query.filter_by(id=id).first()
    #         selected_item.rate = request.form['rate']
    #         print(Item_rating.rate)
    #         db.session.add(selected_item)
    #         db.session.commit()
    return render_template('news.html', news=news)


@app.route('/news/rate/<int:news_id>', methods=['GET','POST'])
def rate(news_id):
    selected_item = Item.query.filter_by(id=news_id).first()
    channel_id = selected_item.channel_id
    if request.method == 'POST':
        if request.form['rate']:
            selected_item.rate = request.form['rate']
            # db.session.add(selected_item)
            db.session.merge(selected_item)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            db.session.close()
        return redirect(url_for('show_news', channel_id=channel_id))
    return render_template('rate.html', news_id=news_id)


@app.route('/best-news/JSON')
def best_news():
    with open('static/best_news.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(best_news=data)
    # tweets = []
    # for line in open('static/best_news.json', 'r'):
    #     tweets.append(json.loads(line))
    #     print(json.loads(line))
    # return json.dumps([tweets])
    # return json.load(([json.loads(line) for line in open('static/best_news.json', 'r')]))
    # best = []
    # filename = os.path.join(app.static_folder, 'best_news.json')
    # with open(filename) as best_news:
    #     for i in best_news:
    #         print(i)
    #         best.append(json.loads(i))

    # return jsonify(tweets)
# @app.route('/best-news/JSON')
# def best_news():
#     news = Item.query.order_by(Item.rate.desc()).limit(5).all()
#     x=[i.serialize for i in news]
#     print(x)
#     return jsonify(news=[i.serialize for i in news])


# jobstores = {
#     'default': SQLAlchemyJobStore(url='sqlite:///news.db')
# }
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(5)
# }
# job_defaults = {
#     'coalesce': True,
#     'max_instances': 1
#     # 'replace_existing':True,
#
# }
#
# scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
# global x
# def testJob():
#
#     # print('x')
#     with app.app_context():
#         s = []
#         news = Item.query.order_by(Item.rate.desc()).limit(5).all()
#         x=[i.serialize for i in news]
#         # print(x)
#         # db.session.rollback()
#         # for new in news:
#     # best_news = CornJob(title=new.title,
#     #                                          link=new.link,
#     #                                          description=new.description,
#     #                                          creator=new.creator,
#     #                                          pubDate=new.pubDate,
#     #                                          category=new.category,
#     #                                          media_content=new.media_content,
#     #                                          media_credit=new.media_credit,
#     #                                          media_description=new.media_description,
#     #                                          rate=new.rate
#     #                                          )
#     # db.session.add(best_news)
#     # db.session.commit()
#
#         # s.append(new.title)
#         # print(new.title)
#         # print(s)
#
#

# job = scheduler.add_job(testJob, 'interval', seconds=7)
# scheduler.start()
# # job = scheduler.add_job(testJob, 'interval', seconds=3)
# print(x)


if __name__ == '__main__':
    x = []
    # app.secret_key = 'super_secret_key'
    PORT = int(os.environ.get('PORT', 5000))
    app.debug = True
    jobstores = {
        'default': SQLAlchemyJobStore(url='sqlite:///news.db')
    }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    job_defaults = {
        'coalesce': True,
        'max_instances': 1
        # 'replace_existing':True,

    }

    scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

    def testJob():
        # print('x')
        with app.app_context():
            s = []
            news = Item.query.order_by(Item.rate.desc()).limit(5).all()
            x=[i.serialize for i in news]
            with open('static/best_news.json', 'w') as json_file:
                # for i in x:
                json.dump(x, json_file)




    job = scheduler.add_job(testJob, 'interval', seconds=7)
    # scheduler.start()
    # job = scheduler.add_job(testJob, 'interval', seconds=3)
    # print(x)
    app.run(host='0.0.0.0', port=PORT)
