from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table, create_engine
import datetime
import os

load_dotenv()

Base = declarative_base()
DATABASE_URL = os.getenv('DATABASE_URL')


def create_session(DATABASE_URL):
    engine = create_engine(DATABASE_URL, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_database(DATABASE_URL, testing=False):
    try:
        engine = create_engine(DATABASE_URL, echo=False)
        if testing:
            Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(engine)
        return engine
    except Exception as e:
        print(e)

class Clinic(Base):
    __tablename__ = 'clinics'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    doctors = relationship("Doctor", back_populates="clinic")

    def __repr__(self):
        return repr({'id': self.id, 'name': self.name})


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), nullable=False)
    password = Column(String(128), nullable=False)
    token = Column(String(32))
    clinic_id = Column(Integer, ForeignKey('clinics.id'))
    clinic = relationship("Clinic", back_populates="doctors")

    appointments = relationship("Appointment", back_populates="doctor")

    def __repr__(self):
        return repr({'id': self.id, 'name': self.name, 'clinic': self.clinic.name})


class Date(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    appointments = relationship("Appointment", back_populates="date")

    def __repr__(self):
        return repr({'id': self.id, 'start_date': self.start_date, 'end_date': self.end_date})


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    notes = Column(Text)
    tc = Column(String(11), nullable=False, unique=True)
    appointments = relationship("Appointment", back_populates="patient")


class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    notes = Column(Text)

    date_id = Column(Integer, ForeignKey('dates.id'))
    date = relationship("Date", back_populates="appointments")

    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    doctor = relationship("Doctor", back_populates="appointments")

    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship("Patient", back_populates="appointments")


if __name__ == "__main__":
    create_database(DATABASE_URL)
    session = create_session(os.getenv('DATABASE_URL'))

    eye = Clinic(id=0, name='eye')
    urology = Clinic(id=1, name='urology')
    orthopedy = Clinic(id=2, name='orthopedy')
    psychiatry = Clinic(id=3, name='psychiatry')

    ali = Doctor(name="Ali", username="ali", password="12345678", clinic=eye)
    ayse = Doctor(name="Ayşe", username="ayse", password="12345678", clinic=urology)
    veli = Doctor(name="Veli", username="veli", password="12345678", clinic=orthopedy)
    gamze = Doctor(name="Gamze", username="gamze", password="12345678", clinic=psychiatry)

    patient1 = Patient(name="Patient 1", tc="12345678901", notes="qeweqwe")


    appointment1 = Appointment(notes="astim", doctor=ali, patient=patient1)
    appointment2 = Appointment(notes="sitma", doctor=veli, patient=patient1)

    date1 = Date(start_date=datetime.datetime.now(), end_date=datetime.datetime.now())
    date2 = Date(start_date=datetime.datetime.now(), end_date=datetime.datetime.now())

    appointment1.date = date1
    appointment2.date = date2

    try:
        session.add_all([eye, urology, orthopedy, psychiatry, patient1, ali, 
        ayse, veli, gamze, patient1, appointment1, appointment2, date1, date2])
        session.commit()
    except:
        pass
 