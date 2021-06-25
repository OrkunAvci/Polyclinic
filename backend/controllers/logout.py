from flask import make_response

from helpers import is_login

def logout_controller(session, request):
    token = request.cookies.get('token')
    doctor = is_login(session, token)
    print(doctor)
    if doctor:
        doctor.token = ''
        session.add(doctor)
        session.commit()
        resp = make_response({"status": "success"})
        resp.set_cookie("token", "")
        return resp, 200
    else:
        resp = make_response({"status": "fail"})
        return resp, 400