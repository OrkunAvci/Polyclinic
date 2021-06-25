from dotenv import load_dotenv
from flask import make_response
import jwt

from models import Doctor
from helpers import is_login

load_dotenv()

def login_controller(session, request):
    token = request.cookies.get('token')
    doctor = is_login(session, token)
    if doctor:
        return {"status": "success"}, 200

    try:
        data = request.json
        username = data['username']
        password = data['password']
    except:
        return {"status": "fail"}, 401

    doctor = session.query(Doctor).filter_by(username=username, password=password).first()

    if doctor:
        encoded_jwt = jwt.encode({"username": username}, "secret", algorithm="HS256")
        resp = make_response({"status": "success"})
        resp.set_cookie("token", encoded_jwt)
        doctor.token = encoded_jwt
        session.add(doctor)
        session.commit()
        return resp, 200
    return {"status": "fail"}, 401