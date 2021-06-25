import React from "react";

export default function PatientNote(props) {
    const appointment = props.appointment;

    return (
        <div style={containerStyle}>
            <h1>Randevu</h1>
            <p>Doktor: {appointment.doctor}</p>
            <p>Tarih: {new Date(Date.parse(appointment.start_date)).toString()}</p>
            <p>Tanı: {appointment.notes}</p>
        </div>
    );
}

const containerStyle = {
    height: "auto",
    width: "720px",
    margin: "auto",
    marginTop: "50px",
    marginBottom: "50px",
    padding: "40px",
    background: "#85CCC9",
    color: "white",
};

const headerStyle = {};

const paraStyle = {};

