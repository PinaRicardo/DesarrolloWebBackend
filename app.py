import email
from flask import Flask, redirect, render_template, request, session, url_for
import datetime
import pymongo
from decouple import config



# FlASK
#############################################################
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "super secret key"
#############################################################

# MONGODB
#############################################################
mongodb_key = "mongodb+srv://desarrollowebuser:desarrollowebpassword@cluster0.dfh7g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(
    mongodb_key, tls=True, tlsAllowInvalidCertificates=True)
db = client.Escuela
cuentas = db.alumno
#############################################################

# Twilio
#############################################################
account_sid = ""
auth_token = ""
TwilioClient = Client(account_sid, auth_token)
#############################################################
comogusten = TwilioClient.messages.create(
            from_="whatsapp:+14155238886",
            body="El usuario %s se agregó a tu pagina web" % (
                request.form["nombre"]),
            to="whatsapp:+5215514200581"
        )
        print(comogusten.sid)


@app.route('/')
def home():
    email = None
    if "email" in session:
        email = session["email"]
        return render_template('index.html', data=email)
    else:
        return render_template('login.html', data=email)

@app.route('/pruebacodigo')
def pruebacodigo():
   return (" nombres=[]     nombres.append(nombre:ruben,   Semestre01:[{       matematicas: 10,        español10    }]    Semestre02:[{        matematicas: 10,        español:10   }]    })")


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
            return render_template("login.html", data="email")
        else:
            email = request.form["email"]
            password = request.form["password"]
            session["email"] = email
            return render_template("index.html", data=email)
            
@app.route('/logout')
def logout():
    if "email" in session:
        session.clear()
        return redirect(url_for("home"))

@app.route('/prueba')
def prueba():
    return ("A01746551 Prueba")

@app.route("/usuarios")
def usuarios():
    cursor = cuentas.find({})
    users = []
    for doc in cursor:
        users.append(doc)
    return render_template("usuarios.html", data=users)

@app.route("/insert")
def insertUsers():
    user={
        "matricula":"1",
        "nombre":"Ruben Raya",
        "correo":"rraya@tec.mx",
        "contraseña":"1234"
    }
    try:
        cuentas.insert_one(user)
        return redirect(url_for("usuarios"))
    except Exception as e:
        return "<p>El servicio no esta disponible =>: %s %s"% type(e),e

@app.route("/delete_one/<matricula>")
def delete_one(matricula):
    try:
        user = cuentas.delete_one({"matricula": (matricula)})
        if user.deleted_count == None:
            return "<p>La matricula %s nó existe</p>" % (matricula)
        else:
            return "<p>Eliminamos %d matricula: %s </p>" % (user.deleted_count, matricula)
    except Exception as e:
        return "%s" % e

@app.route("/update", methods=["POST"])
def update():
    try:
        filter = {"matricula": request.form["matricula"]}
        user = {"$set": {
            "nombre": request.form["nombre"]
        }}
        cuentas.update_one(filter, user)
        return redirect(url_for("usuarios"))

    except Exception as e:
        return "error %s" % (e)

@app.route('/create')
def create():
    return render_template('Create.html')
