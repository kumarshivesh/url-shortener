from sqlalchemy.orm import Session
from . import models
import random
import string

def get_url_by_short_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()

def create_short_url(db: Session, long_url: str):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    db_url = models.URL(long_url=long_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
