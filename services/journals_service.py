from models import db, Journal
from datetime import datetime
from utils.encryption_utils import EncryptionManager

encryption = EncryptionManager()

def save_journal_entry(daily_text: str, emotions: dict):
    sentiment = emotions.get("sentiment", "")
    themes = ", ".join(emotions.get("themes", []))
    empathy = emotions.get("empathy", "")

    journal = Journal(
        journal_input=encryption.encrypt(daily_text),
        sentiment=encryption.encrypt(sentiment),
        themes=encryption.encrypt(themes),
        empathy=encryption.encrypt(empathy),
        input_timestamp=datetime.utcnow()
    )

    db.session.add(journal)
    db.session.commit()
