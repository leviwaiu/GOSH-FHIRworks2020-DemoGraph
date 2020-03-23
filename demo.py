from flask import Flask
from flask import render_template, redirect
from asyncio import get_event_loop

import graphing
import os

app = Flask(__name__, static_url_path='/static')
finished = False


@app.route("/")
@app.route("/index")
def index():
    if finished:
        return render_template('index.html', finished=finished)
    else:
        return render_template('index.html')


@app.route("/age")
def getage():
    if not os.path.exists(os.path.join("static", "age.png")):
        plt = graphing.agegraph()
        plt.savefig(os.path.join("static", "age.png"))

    source = {"src": os.path.join("static", "age.png")}
    return render_template("index.html", source=source, finished=finished)


@app.route("/gender")
def getgender():
    if not os.path.exists(os.path.join("static", "gender.png")):
        plt = graphing.gendergraph()
        plt.savefig(os.path.join("static", "gender.png"))
    source = {"src": os.path.join("static", "gender.png")}
    return render_template("index.html", source = source, finished=finished)


@app.route("/marital")
def getmarital():
    if not os.path.exists(os.path.join("static", "marital.png")):
        plt = graphing.maritalgraph()
        plt.savefig(os.path.join("static", "marital.png"))
    source = {"src": os.path.join("static", "marital.png")}
    return render_template("index.html", source = source, finished=finished)


@app.route("/language")
def getlanguage():
    if not os.path.exists(os.path.join("static", "language.png")):
        plt = graphing.languagegraph()
        plt.savefig(os.path.join("static", "language.png"))
    source = {"src": os.path.join("static", "language.png")}
    return render_template("index.html", source = source, finished=finished)


@app.route("/state")
def getstate():
    if not os.path.exists(os.path.join("static", "state.png")):
        plt = graphing.stategraph()
        plt.savefig(os.path.join("static", "state.png"))
    source = {"src": os.path.join("static", "state.png")}
    return render_template("index.html", source = source, finished=finished)


@app.route("/country")
def getcountry():
    if not os.path.exists(os.path.join("static", "country.png")):
        plt = graphing.countrygraph()
        plt.savefig(os.path.join("static", "country.png"))
    source = {"src": os.path.join("static", "country.png")}
    return render_template("index.html", source = source, finished=finished)


@app.route("/process")
def initfhir():
    global finished
    print("Initialising")
    graphing.initialise()
    finished = True
    print("Finished")
    return redirect("/")
