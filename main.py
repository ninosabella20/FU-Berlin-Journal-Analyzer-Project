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
from services.journals_service import save_journal_entry

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") #reading DB config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/journal',methods=['GET', 'POST'])
def journal():
    return render_template('journal.html')

@app.route('/index',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print("submit ")
    data = request.get_json()
    journal_text = data.get('text', '')
    # Do something with the journal_text, e.g., save it to a database
    print("Journal received:", journal_text)
    json_payload = {"entries": [journal_text]}
    logger.debug(f"json_payload : {json_payload}")
    emotions = model.analyze_journal(json_payload )
    logger.info(f"emotions : {emotions}")

    save_journal_entry(journal_text, emotions)

    return jsonify(status="success")


if __name__ == '__main__':
    app.run(debug=True)