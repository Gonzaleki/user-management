from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Mastur"

@app.route("/login")
def login():
    var1= "now loading"
    print(var1)
    return var1


if __name__ == "__main__":
    app.run(debug=True)
