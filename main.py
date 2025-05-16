from flask import Flask, render_template, request,jsonify
import model
import json
from logger import logger

app = Flask(__name__)

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
    return render_template('result.html', name=daily)

if __name__ == '__main__':
    app.run(debug=True)