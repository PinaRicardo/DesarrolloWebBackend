from flask import Flask, render_template

# FlASK
#############################################################
app = Flask(__name__)
#############################################################

@app.route('/prueba')
def home():
    return ("A01746551 Prueba")