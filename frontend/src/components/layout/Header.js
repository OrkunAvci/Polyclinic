import React from 'react';
import { Link } from "react-router-dom";

export default function Header(props) {
    console.log(props.isLogin)
    return (
        <header style={headerStyle}>

            <Link style={linkStyle} to="/">
                Anasayfa
            </Link>
            {props.isLogin ?<>
                <Link style={linkStyle} to="/patient">Hasta</Link> 
                <Link style={linkStyle} to="/logout">Çıkış Yap</Link> 
                </>
                :
                <Link style={linkStyle} to="/login">Login</Link>
            }
        </header>
    );

}



const headerStyle = {
    width: "100vw",
    height: "48px",
    position: "relative",
    textDecoration: "none",
    background: "#41B3A3"
}

const linkStyle = {
    display: "block",
    float: "left",
    position: "relative",

    color: "white",
    margin: "10px",
    textDecoration: "none",
}
/*
const linkStyle*hover = {
    background: "#2B2D42"
}*/

