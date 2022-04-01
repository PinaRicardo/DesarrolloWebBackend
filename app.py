from flask import Flask, render_template

# FlASK
#############################################################
app = Flask(__name__)
#############################################################

@app.route('/prueba')
def prueba():
    return ("A01746551 Prueba")
@app.route('/')
def home():
    return render_template("index.html")
