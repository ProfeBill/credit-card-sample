from flask import Flask
from flask import render_template, request
import sys

sys.path.append("src")
from src.controller.tarjetas_controller import TarjetasController
from src.view.web import plano

app = Flask(__name__)

app.register_blueprint( plano.blueprint )

if __name__ == "__main__":
    app.run()