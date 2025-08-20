from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Mastur"

@app.route("/signin")
def sing_in():
    print("intentando loguear")
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)
