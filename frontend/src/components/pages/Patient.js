import axios from 'axios';
import React, { useState } from 'react';
import useFetch from "@ahmetelgun/usefetch";

import PatientNote from "../PatientNote";

function Patient() {
    const [patientTc, setPatientTc] = useState(0);
    const [patient, setPatient] = useState(null);
    const [patientNotes, setPatientNotes] = useState(null);
    const [response, loading, error, callFetch] = useFetch();
    const [patientNoteUpdateResponse, patientNoteUpdateLoading, patientNoteUpdateError, patientNoteUpdateCallFetch] = useFetch();

    const getPatient = (e) => {
        e.preventDefault();

        const options = {
            method: "GET",
            mode: "cors",
            cache: "no-cache",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
        };

        callFetch(`http://localhost:5000/patients/${patientTc}`, options);
    };
    let patientError = "";
    if (loading) {
        return <div>loading</div>;
    } else if (error || (response && response.status != 200)) {
        patientError = "not found"
    } else if (response) {
        if (response.status == 200 && response.data != patient) {
            setPatient(response.data)
            setPatientNotes(response.data.data.patient.notes);
        }
    }
    
    function handlePatientNotesUpdate(e) {
        e.preventDefault();

        const options = {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({tc: patientTc, "notes": patientNotes})
        };
        patientNoteUpdateCallFetch("/patients/update", options);
    }
    let message = "";
    if (patientNoteUpdateResponse && patientNoteUpdateResponse.status == 200) {
        message="Success"
    }

    return (
        <div style={wrapperStyle}>
            <h4 style={errorClass}>{patientError}</h4>
            <div style={searchContainerStyle}>
                <form style={formStyle}>
                    <input
                        type="number"
                        name="patient_tc"
                        onChange={(e) => setPatientTc(e.target.value)}
                        style={formItemStyle}
                        placeholder="tc"
                    />
                    <button type="submit" onClick={(e) => getPatient(e)} style={formItemStyle}>
                        Getir
                    </button>
                </form>
            </div>

            <div style={patient === null ? controlledStyle : patientContainerStyle}>
                {message}
                <h2>{patient ? patient.data.patient.name : ""}</h2>
                <form>
                    <textarea name="text_field" style={patientDetailStyle} value={patientNotes} onChange={e => { setPatientNotes(e.target.value) }} />

                    <button style={buttonStyle} type="submit" onClick={e => handlePatientNotesUpdate(e)}>
                        Update Patient's Notes
                    </button>
                </form>
            </div>
            {patient === null
                ? ""
                : patient.data.patient.appointments.map((appointment, index) => {
                    return <PatientNote key={index} appointment={appointment} />;
                })}
        </div>
    );
}

const formStyle = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
}

const formItemStyle = {
    marginBottom: "10px"
}

const searchContainerStyle = {
    height: "auto",
    width: "480px",
    margin: "auto",
    marginTop: "50px",
    marginBottom: "50px",
    padding: "30px",
    background: "#85CCC9",
    color: "white",
};

const patientContainerStyle = {
    width: "720px",
    margin: "auto",
    marginTop: "50px",
    padding: "50px",
    background: "#85CCC9",
    color: "white",
};

const wrapperStyle = {

}

const buttonStyle = {

}

let controlledStyle = {
    display: "none"
}

export default Patient;

const errorClass = {
    color: "red"
}

const patientDetailStyle = {
    width: "100%",
    height: "75px"
}