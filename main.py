from flask import Flask, render_template, request,jsonify
import model
import json
from logger import logger
from dotenv import load_dotenv
import os
from utils.encryption_utils import set_encryption_key

set_encryption_key()
load_dotenv() #load env file

from models import db #load the ORM
from services.journals_service import save_journal_entry, get_journal_list, get_summary_sentiment, get_summary_themes, get_summary_input_streak

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") #reading DB config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    daily = request.form.get('daily')
    logger.debug(f"Output which you entered: {daily}")
    json_payload = {"entries": [daily]}
    logger.debug(f"json_payload : {json_payload}")
    emotions = model.analyze_journal(json_payload )
    logger.info(f"emotions : {emotions}")

    save_journal_entry(daily, emotions)

    return render_template('result.html', name=daily)

@app.route('/journalList', methods=['GET'])
def journalList():
    getAllJournalInput = get_journal_list()
    print(getAllJournalInput)
    return jsonify(getAllJournalInput)

@app.route('/summarySentiment', methods=['GET'])
def summarySentiment():
    sentimentAllTime = get_summary_sentiment()
    countSentiment = dict(sentimentAllTime)
    print(countSentiment)
    return jsonify(countSentiment)

@app.route('/summaryThemes', methods=['GET'])
def summaryThemes():
    themesAllTime = get_summary_themes()
    countThemes = dict(themesAllTime)
    print(countThemes)
    return jsonify(countThemes)

@app.route('/summaryInputStreak', methods=['GET'])
def summaryInputStreak():
    listDateInputStreak = get_summary_input_streak()
    date_list = [int(day) for day in listDateInputStreak]
    print(date_list)
    return jsonify(date_list)

if __name__ == '__main__':
    app.run(debug=True)