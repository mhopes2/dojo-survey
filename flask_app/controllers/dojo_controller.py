from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Survey

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_survey', methods=['POST'])
def create_survey():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    Survey.save(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('complete.html', survey = Survey.get_survey())

