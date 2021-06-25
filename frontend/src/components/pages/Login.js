import React, { useState } from 'react';
import axios from "axios";
import useFetch from "@ahmetelgun/usefetch";
import {Redirect} from 'react-router-dom'

export default function Login(props) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [response, loading, error, callFetch] = useFetch();

    function loginRequest(e) {
        e.preventDefault();
        const options = {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({username, password})
        };
        callFetch("/login", options);
    }
    let loginError = "";
    if(loading) {
        return "loading";
    }
    if(response && response.status == 200) {
        return <Redirect to="/" />
    }
    if(error || (response && response.status != 200)){
        loginError = "Username or Password wrong";
    }

    return (
        <div style={containerStyle}>
            <h2 style={headingStyle}>Enter your credentials</h2>
            <form style={formStyle}>
                <h3 style={errorClass}>{loginError ?? ""}</h3>
                <label>Username</label>
                <input
                    style={formItemStyle}
                    type="text"
                    name="username"
                    onChange={(e) => setUsername(e.target.value)}
                />

                <label>Password</label>
                <input
                    style={formItemStyle}
                    type="password"
                    name="password"
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button
                    type="submit"
                    onClick={loginRequest}
                >
                    Login to your account
                </button>
            </form>
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

const containerStyle = {
    height: "auto",
    width: "auto",
    margin: "auto",
    padding: "70px",
    background: "#85CCC9",
    color: "white",
}

const headingStyle = {

}

const errorClass = {
    color: "red"
}
