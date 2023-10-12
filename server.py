from flask import Flask, render_template

app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Глоссарий", "URL": "/glossary" },
    { "title": "Обо мне", "URL": "/aboutme" },
]

@app.route("/")
def index():
    return render_template("index.html", name="Главная", nav=nav)

@app.route("/metallica")
def Metallica():
    return render_template("Metallica.html", name="Metallica", nav=nav)

@app.route("/scorpions")
def Scorpions():
    return render_template("Scorpions.html", name="Scorpions", nav=nav)

@app.route("/slipknot")
def Slipknot():
    return render_template("Slipknot.html", name="Slipknot", nav=nav)

@app.route("/glossary")
def Glossary():
    return render_template("Glossary.html", name="Глоссарий", nav=nav)

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html", name="Обо мне", nav=nav)

#http://127.0.0.1:5000/