import React from 'react'

class Homepage extends React.Component {
	render() {
		return (
			<div style={containerStyle}>
				<h1>Şifa Polikliniği Bilgi Sistemi</h1>
				<h2>Hoşgeldiniz</h2>
				<p>Sayfalar arasında geçiş yapmak için üstteki araç çubuğunu kullanınız.</p>
			</div>
		)
	}
}

const containerStyle = {
	height: "auto",
	width: "auto",
	margin: "auto",
	padding: "270px",
	background: "#85CCC9",
	color: "white",
}

export default Homepage;