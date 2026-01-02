from flask import Flask, redirect, url_for, render_template
import os
from config import Config, Development, Testing
from clientes.rutas import cliente_bp
from libros.rutas import libros_bp

app= Flask(__name__)

app.register_blueprint(cliente_bp)
app.register_blueprint(libros_bp)




entorno = os.getenv("development", "development")

if entorno == "development":
    app.config.from_object(Development)
elif entorno == "Testing":
    app.config.from_object(Testing)
elif entorno == "production":
    app.config.from_object(Config)

@app.route("/")
def inicio():
   return redirect(url_for('cliente_bp.login'))

@app.errorhandler(401)
def usuario_no_logeado(error):
    return render_template('error.html', error=error), 401

@app.errorhandler(403)
def usuario_no_logeado(error):
    return render_template('error.html', error=error),403

@app.errorhandler(500)
def usuario_no_logeado(error):
    return render_template('error.html', error=error), 500
