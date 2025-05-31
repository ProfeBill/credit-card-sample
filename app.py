from flask import Flask
import sys

sys.path.append("src")
from src.view.web import plano
from src.controller.tarjetas_controller import TarjetasController

app = Flask(__name__)


app.register_blueprint( plano.blueprint )

if __name__ == "__main__":
    app.run()