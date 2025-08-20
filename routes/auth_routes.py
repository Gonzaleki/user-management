from flask import Blueprint
# Blueprint es una Class de flask, que permite dividir la app en mini apps
# para evitar tener todo en app.py, ejemplo las rutas

# Llamamos a la Class Blueprint y le pasamos dos argumentos, el primero
# es el nombre, puede ser cualquier cosa y el segundo es la variable 
# built_in the python para representar el nombre del modulo
auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
    return "This would return the method that creates the user"

@auth.route("/login")
def signin():
    return "This would return the method that logs the user in"

@auth.route("/logout")
def signin():
    return "This would return the method that logs the user out"