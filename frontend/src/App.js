import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, useLocation } from "react-router-dom";

import Header from "./components/layout/Header";
import Homepage from "./components/pages/Homepage";
import Login from "./components/pages/Login";
import Patient from "./components/pages/Patient";
import Logout from "./components/pages/Logout";
import './App.css';

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

export default function App() {
    const [isLogin, setIsLogin] = useState(false);
    let location = useLocation();
    useEffect(() => {
        let token = getCookie("token");
        if(token) {
            setIsLogin(true);
        }
        else{
            setIsLogin(false);
        }
    }, [location])
    return (
            <div className="App">
                <div className="container">
                    <Header isLogin={isLogin} />

                    <Route
                        exact={true}
                        path="/"><Homepage isLogin={isLogin}></Homepage></Route>

                    <Route
                        exact={true}
                        path="/login"
                    ><Login isLogin={isLogin}></Login></Route>

                    <Route
                        exact={true}
                        path="/patient"
                        component={Patient}
                    />
                    
                    <Route
                        exact={true}
                        path="/logout"
                        component={Logout}
                    />
                </div>
            </div>
    )
}
