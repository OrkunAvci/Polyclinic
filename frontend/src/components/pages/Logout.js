import React, { useEffect, useState } from 'react';
import useFetch from "@ahmetelgun/usefetch";
import { Redirect } from 'react-router-dom'

export default function Logout() {
    const [response, loading, error, callFetch] = useFetch();
    const options = {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
        },
    };
    callFetch("/logout", options);

    function setCookie(cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }
    setCookie("token", "", 1);
    return <Redirect to="/" />
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

const labelStyle = {

}

const inputStyle = {

}

const buttonStyle = {

}

