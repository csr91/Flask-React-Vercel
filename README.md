# Este proyecto sirve como modelo para correr una app de React con Flask de backend en Vercel.
# Es una maqueta 100% inicial y basica para poder desplegar tu proyecto con un backend y frontend bajo el mismo dominio.

# Deploy
Lo mas importante esta en el script de react
"scripts": {
"flask-dev": "FLASK_DEBUG=1 pip3 install -r requirements.txt && python3 -m flask --app api/index run -p 5328",
"start": "react-scripts start",
"build": "react-scripts build",
"test": "react-scripts test",
"eject": "react-scripts eject"
},

La linea genera al momento de la build el lanzamiento de la app de flask
"flask-dev": "FLASK_DEBUG=1 pip3 install -r requirements.txt && python3 -m flask --app api/index run -p 5328",

# Routes

Y las routes del archivo vercel.json 

{
"env": {
"PYTHONPATH": "api/"
},
"functions": {
"api/index.py": {
"includeFiles": "api/**",
"memory": 1024,
"maxDuration": 10
}
},
"routes": [
{
"src": "/api",
"dest": "/api/index.py"
},
{
"src": "/api/(.*)",
"dest": "/api/index.py"
},
{
"src": "/(.*)",  
"dest": "/$1"   
}
]
}

Que permiten redirigir las solicitudes necesarias hacia la API.

# API

La API de flask es muy simple, contiene varias URLs para consultar respuesta hacia /api incluyendo hasta consulta hacia otro archivo en la misma carpeta.

# Front

El front es solo el app.js de react, con un fetch a /API para chequear en la consola la respuesta

https://pruebabckfr.vercel.app/
https://pruebabckfr.vercel.app/api
https://pruebabckfr.vercel.app/api/hello
https://pruebabckfr.vercel.app/api/otroarchivo
https://pruebabckfr.vercel.app/rct