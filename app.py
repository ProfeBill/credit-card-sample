from flask import Flask
from flask import render_template, request
import sys

sys.path.append("src")
from src.controller.tarjetas_controller import TarjetasController


app = Flask(__name__)

@app.route("/")
def hola():
    return render_template("hola.html")

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/lista_tarjetas')
def lista_tarjetas():
    resultado = TarjetasController.BuscarPorCedula(request.args["cedula"])
    return render_template('lista_tarjetas.html', cedula=request.args["cedula"], tarjetas=resultado  )

if __name__ == "__main__":
    app.run(debug=True)