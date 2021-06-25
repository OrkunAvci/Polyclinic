from datetime import datetime
import unittest
from controllers import patients
from dotenv import load_dotenv
import os
from models import create_session, Doctor, Date

DATABASE_URL = os.getenv('DATABASE_URL')


class TestGetPatientData(unittest.TestCase):
    def setUp(self):
        self.session = create_session(DATABASE_URL)

    def test_get_patient_data(self):
        patient = patients.get_patient_data(self.session, 123)
        self.assertFalse(patient)

        data = patients.get_patient_data(self.session, 12345678901)
        self.assertEqual(data['patient']['tc'], "12345678901")

    def test_is_patient_exist(self):
        is_exist = patients.is_patient_exist(self.session, 123)
        self.assertFalse(False)

        patient = patients.is_patient_exist(self.session, 12345678901)
        self.assertEqual(patient.tc, "12345678901")

    def test_update_patient_data(self):
        result = patients.update_patient_data(self.session, 123, "Asd")
        self.assertFalse(result)

        result = patients.update_patient_data(self.session, 12345678901, "Asd")
        self.assertTrue(result)

    def test_create_appintment_data(self):
        doc = self.session.query(Doctor).first()
        start_date = datetime.fromtimestamp(1622388667)
        end_date = datetime.fromtimestamp(1622398967)

        date = Date(start_date=start_date, end_date=end_date)

        appointment = patients.create_appointment_data(self.session, 123, doc, date, "ASD")
        self.assertFalse(appointment)

        appointment = patients.create_appointment_data(self.session, 12345678901, doc, date, "ASD")
        self.assertEqual(appointment.doctor.id, doc.id)
if __name__ == '__main__':
    unittest.main()
