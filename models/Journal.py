from . import db
from datetime import datetime

class Journal(db.Model):
    __tablename__ = 'journal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    journalInput = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.Text)
    themes = db.Column(db.Text)
    empathy = db.Column(db.Text)
    inputTimestamp = db.Column(db.DateTime, default=datetime.utcnow)
