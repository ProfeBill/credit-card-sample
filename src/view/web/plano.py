from flask import Blueprint, render_template, request


blueprint = Blueprint( "plano", __name__, "templates" )

import sys
sys.path.append("src")
from model.Usuario import Usuario
from model.tarjeta import Tarjeta
from src.controller.tarjetas_controller import TarjetasController


@blueprint.route("/")
def hola():
    return render_template("index.html")

@blueprint.route('/buscar')
def buscar():
    return render_template('buscar.html')

@blueprint.route('/tarjetas_encontradas')
def lista_tarjetas():
    resultado = TarjetasController.BuscarPorCedula(request.args["cedula"])
    return render_template('tarjetas_encontradas.html', cedula=request.args["cedula"], tarjetas=resultado  )

@blueprint.route('/insertar')
def insertar():
    return render_template('insertar.html')

@blueprint.route('/tarjeta_insertada')
def tarjeta_insertada():
    TarjetasController.Insertar(Tarjeta(
        numero_tarjeta=request.args["numero_tarjeta"],
        cedula=request.args["cedula"],
        franquicia=request.args["franquicia"],
        codigo_banco=request.args["codigo_banco"],
        fecha_vencimiento=request.args["fecha_vencimiento"],
        cupo=float(request.args["cupo"]),
        tasa_interes=float(request.args["tasa_interes"]),
        cuota_manejo=float(request.args["cuota_manejo"])
    ))
    return render_template('tarjeta_insertada.html', numero_tarjeta=request.args["numero_tarjeta"],
        cedula=request.args["cedula"],
        franquicia=request.args["franquicia"],
        codigo_banco=request.args["codigo_banco"],
        fecha_vencimiento=request.args["fecha_vencimiento"],
        cupo=float(request.args["cupo"]),
        tasa_interes=float(request.args["tasa_interes"]),
        cuota_manejo=float(request.args["cuota_manejo"]))


@blueprint.route("/eliminar")
def eliminar():
    return render_template("eliminar.html")

@blueprint.route("/tarjeta_eliminada")
def tarjeta_eliminada():
    numero_tarjeta = request.args["numero_tarjeta"]
    TarjetasController.EliminarTarjeta(numero_tarjeta)
    return render_template('tarjeta_eliminada.html', numero_tarjeta=request.args["numero_tarjeta"] )

if __name__ == "__main__":
    blueprint.run(debug=True)