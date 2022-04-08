from crypt import methods
from flask import Flask, render_template, request

# FlASK
#############################################################
app = Flask(__name__)
#############################################################

@app.route('/pruebacodigo')
def pruebacodigo():
   return (" nombres=[]     nombres.append(nombre:ruben,   Semestre01:[{       matematicas: 10,        español10    }]    Semestre02:[{        matematicas: 10,        español:10   }]    })")
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/login', methods=["GET","POST"])
def login():
    if (request.methods == "GET"):
        return render_template("login.html", error=email)
    else:
        email=request.form["email"]
        password=request.form["password"]
        return render_template("index.html", error=email)

@app.route('/prueba')
def prueba():
    return ("A01746551 Prueba")