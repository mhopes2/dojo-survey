from flask import Flask, session
app = Flask(__name__)
app.secret_key = "Dojo survey with validations is a secret"