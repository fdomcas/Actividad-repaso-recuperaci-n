from . import cliente_bp
from flask import Flask, redirect, url_for, abort, request, render_template, make_response
import json

datos= [
]





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
        nombre= request.form.get("nombre")
        pas1= request.form.get("contraseña1")
        pas2 = request.form.get("contraseña2")
        if pas1 == pas2 and type(pas1) == type(pas2):
            cliente={"usuario":nombre, "contraseña":pas1} 
            datos.append(cliente)
            reps= make_response(redirect(url_for('libros_bp.mostrar')))
            reps.set_cookie("cliente", nombre, max_age=60*60*24*7)
            return reps
        else:
            return render_template("usuarios/login.html", registrar="registrar", error="las contraseñas no coinciden")

    
    
    elif request.method == "GET":
        return render_template("usuarios/login.html", registrar="registrar")

@cliente_bp.route("/cerrar_sesion")
def cerrar_sesion():
    cooki= request.cookies.get("cliente")
    if cooki:
        resp= make_response(redirect(url_for("cliente_bp.login")))
        resp.delete_cookie("cliente")
        return resp
    


