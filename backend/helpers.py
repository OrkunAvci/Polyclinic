from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import jwt

from models import Doctor

def create_session(DATABASE_URL):
    engine = create_engine(DATABASE_URL, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def is_login(session, token):
    try:
        decoded = jwt.decode(token, "secret", algorithms=["HS256"])
        username = decoded['username']
    except: 
        return False

    doctor = session.query(Doctor).filter_by(username=username).first()
    if doctor and doctor.token == token:
        return doctor
    else:
        return False
