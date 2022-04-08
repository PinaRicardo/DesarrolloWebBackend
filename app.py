from crypt import methods
from flask import Flask, render_template, request, session


# FlASK
#############################################################
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "super secret key"
#############################################################


@app.route('/')
def home():
    email = None
    if "email" in session:
        email = session["email"]
        return render_template('index.html', data=email)
    else:
        return render_template('Login.html', data=email)

@app.route('/pruebacodigo')
def pruebacodigo():
   return (" nombres=[]     nombres.append(nombre:ruben,   Semestre01:[{       matematicas: 10,        español10    }]    Semestre02:[{        matematicas: 10,        español:10   }]    })")
import email
from flask import Flask, redirect, render_template, request, session, url_for
import datetime

@app.route('/signup')
def signup():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    email = None    
    if "email" in session:
        return render_template('index.html', data=session["email"])
    else:
        if (request.method == "GET"):
            return render_template("Login.html", data="email")
        else:
            email = request.form["email"]
            password = request.form["password"]
            session["email"] = email
            return render_template("index.html", data=email)

@app.route('/prueba')
def prueba():
    return ("A01746551 Prueba")