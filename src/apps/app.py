#!/usr/bin/env python3

from flask import Flask, request, render_template
from src.components.db import DBConnection, Counts, Pokemon, Names
from prometheus_flask_exporter import PrometheusMetrics
import datetime

app = Flask(__name__, template_folder='../templates')
db=DBConnection()
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Poke App', version='24.1.0.1')

@app.route("/")
def home():
    contenders = db.getDateChamps(datetime.datetime.today().date())
    champ = contenders[0][0]
    return render_template('home.jinja', champ=champ, contenders=contenders)

@app.route("/search", methods=["POST"])
@metrics.counter('invocation_by_type', 'queries',
         labels={'query': lambda: request.form.get("pokename", "")})
def search():
    input_text = request.form.get("pokename", "").strip()
    if len(input_text) > 2:
        pokelist=db.findAll(input_text)
        return render_template('search.jinja', pokelist=pokelist)
    else:
        return Flask.redirect('/')

@app.route("/id/<int:id>")
def get_by_id(id):
    pokemon:Pokemon=db.getById(id)
    if not pokemon:
      return Flask.redirect('/404')
    return render_template('pokemon.jinja', pokemon=pokemon)

@app.route("/vs/<int:id>")
def vs(id):
    pokemon:Pokemon=db.getById(id)
    rival:Pokemon=db.getRandom()

    rh= rival.counts[0].hits if rival.counts else 0
    ph= pokemon.counts[0].hits if pokemon.counts else 0
    return render_template('vs.jinja', pokemon=pokemon, rival=rival, rh=rh, ph=ph)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.jinja')