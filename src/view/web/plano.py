from flask import Blueprint, render_template, request

blueprint = Blueprint( "plano", __name__, "templates" )

import sys
sys.path.append("src")
from model.Usuario import Usuario
from src.controller.tarjetas_controller import TarjetasController


@blueprint.route("/")
def hola():
    return render_template("hola.html")

@blueprint.route('/buscar')
def buscar():
    return render_template('buscar.html')

@blueprint.route('/lista_tarjetas')
def lista_tarjetas():
    resultado = TarjetasController.BuscarPorCedula(request.args["cedula"])
    return render_template('lista_tarjetas.html', cedula=request.args["cedula"], tarjetas=resultado  )

if __name__ == "__main__":
    blueprint.run(debug=True)