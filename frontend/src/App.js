import React, { useState, useEffect } from 'react';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        // Hacer una solicitud a la API Flask
        fetch('/api/hello')
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div className="App">
            <h1>Reactsss App</h1>
            <p>{message}</p>
        </div>
    );
}

export default App;
