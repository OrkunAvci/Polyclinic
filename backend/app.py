from flask import Flask, g, request
from dotenv import load_dotenv
import os
import jwt
from controllers import login_controller, logout_controller, get_patient, create_patient, update_patient, create_appointment

from helpers import create_session

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

session = create_session(DATABASE_URL)

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = os.getenv('FRONTEND_URL')
    response.headers["Access-Control-Allow-Headers"] = "content-type"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

@app.route('/login', methods=['POST'])
def login():
    return login_controller(session, request)

@app.route('/logout', methods=['POST'])
def logout():
    return logout_controller(session, request)

@app.route('/patients/<tc>', methods=['GET'])
def patient_get(tc):
    return get_patient(session, request, tc)

@app.route('/patients/create', methods=['POST'])
def patient_create():
    return create_patient(session, request)

@app.route('/patients/update', methods=['POST'])
def patient_update():
    return update_patient(session, request)

@app.route('/patients/create_appointment', methods=['POST'])
def appointment_add():
    return create_appointment(session, request)


if __name__ == "__main__":
    print(os.getenv("FRONTEND_DOMAIN"))
    app.run()