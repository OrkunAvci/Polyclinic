from models import Patient, Date, Appointment
from helpers import is_login
from flask import jsonify
from datetime import datetime

def is_patient_exist(session, tc):
    patient = session.query(Patient).filter_by(tc=tc).first()
    if patient:
        return patient
    return False

def get_patient_data(session, tc):
    patient = is_patient_exist(session, tc)
    if patient:
        data = {
            "patient": {
                "name": patient.name,
                "notes": patient.notes,
                "tc": patient.tc
            }
        }
        appointments = []
        for i in patient.appointments:
            appointments.append({
                "start_date": i.date.start_date,
                "end_date": i.date.end_date,
                "notes": i.notes,
                "doctor": i.doctor.name
            })
        data['patient']['appointments'] = appointments
        return data
    else:
        return False

def update_patient_data(session, tc, notes):
    patient = is_patient_exist(session, tc)
    if patient:
        patient.notes = notes
        return True
    return False


def create_appointment_data(session, tc, doctor, date, notes):
    patient = is_patient_exist(session, tc)
    if patient:
        appointment = Appointment(notes=notes, date=date, doctor=doctor, patient=patient)
        return appointment
    return False


def get_patient(session, request, tc):
    token = request.cookies.get('token')
    doctor = is_login(session, token)
    if not doctor:
        return {"status": "fail"}, 401

    data = get_patient_data(session, tc)
    if data:
        return {"status": "success", "data": data}, 200
    return {"status": "not found"}, 404

def create_patient(session, request):
    token = request.cookies.get('token')
    doctor = is_login(session, token)
    if not doctor:
        return {"status": "fail"}, 401

    try:
        data = request.json
        tc = data['tc']
        name = data['name']
        if name == "" or tc == "":
            return {"status": "fail"}, 400
    except:
        return {"status": "fail"}, 400

    if session.query(Patient).filter_by(tc=tc).first():
        return {"status": "duplicate"}, 409
    
    patient = Patient(tc=tc, name=name)
    session.add(patient)
    session.commit()
    return {"status": "success"}, 200

def update_patient(session, request):
    token = request.cookies.get('token')
    doctor = is_login(session, token)
    if not doctor:
        return {"status": "fail"}, 401

    try:
        data = request.json
        tc = data['tc']
        notes = data['notes']
    except:
        return {"status": "fail"}, 400

    if update_patient_data(session, tc, notes):
        return {"status": "success"}, 200
    
    return {"status": "patient not found"}, 404

def create_appointment(session, request):
    token = request.cookies.get('token')
    doctor = is_login(session, token)
    if not doctor:
        return {"status": "fail"}, 401

    try:
        data = request.json
        tc = data['tc']
        start_date = data['start_date']
        end_date = data['end_date']

        start_date = datetime.fromtimestamp(int(start_date))
        end_date = datetime.fromtimestamp(int(end_date))

        date = Date(start_date=start_date, end_date=end_date)
    except Exception as e:
        print(e)
        return {"status": "fail"}, 400

    try:
        notes = data['notes']
    except:
        notes = ""


    appointment = create_appointment_data(session, tc, doctor, date, notes)
    if appointment:
        session.add(apppointment)
        session.commit()
        return {"status": "success"}, 200
    else:
        return {"status": "patient not found"}, 404

