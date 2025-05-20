from flask import Flask, render_template, request,jsonify
import model
import json
from logger import logger
from dotenv import load_dotenv #load env file
from models import db, Journal #load the ORM
import os
from datetime import datetime

load_dotenv() #load env file

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

    #get data from payload
    sentiment = emotions.get("sentiment")
    themes = ", ".join(emotions.get("themes", []))
    empathy = emotions.get("empathy")
    
    #map to the ORM
    journal = Journal(
        journalInput=daily,
        sentiment=sentiment, 
        themes=themes, 
        empathy=empathy,
        inputTimestamp=datetime.utcnow())
    
    db.session.add(journal)
    db.session.commit()

    return render_template('result.html', name=daily)


if __name__ == '__main__':
    app.run(debug=True)