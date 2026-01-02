from flask import Blueprint, Flask
from flask import Flask, redirect, url_for, abort, request, render_template, make_response
import json

datos= [
]




cliente_bp= Blueprint("cliente_bp",__name__, template_folder="templates/login")

@cliente_bp.route("/login", methods=["POST", "GET"])
def login():
    nombre= request.form.get("nombre")
    pas= request.form.get("contraseña")
    if request.method == "GET":
        return render_template("usuarios/login.html", login="login")
    elif request.method == "POST":
        if not nombre:
            return render_template("usuarios/login.html", login="login")
        elif [nombre, pas] in [[cliente["usuario"], cliente["contraseña"]] for cliente in datos]:
            reps= make_response(redirect(url_for('libros_bp.mostrar')))
            reps.set_cookie("cliente", nombre, max_age=60*60*24*7)
            return reps
        else:
            return render_template("usuarios/login.html", login="login", error="Usuario o contraseña  erroneos")

@cliente_bp.route("/registrar", methods=["POST", "GET"])
def registro():
    if request.method == "POST":
        cliente={"usuario":request.form.get("nombre"), "contraseña":request.form.get("contraseña1")} 
        datos.append(cliente)
        print(datos)
        return redirect(url_for("cliente_bp.login"))
    
    elif request.method == "GET":
        return render_template("usuarios/login.html", registrar="registrar")

@cliente_bp.route("/cerrar sesion")
def cerrar_sesion():
    cooki= request.cookies.get("cliente")
    if cooki:
        resp= make_response(redirect(url_for("cliente_bp.login")))
        resp.delete_cookie("cliente")
        return resp 