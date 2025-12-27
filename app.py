from flask import Flask, redirect, url_for 
import os
from config import Config, Development, Testing, production
from clientes import cliente_bp

app= Flask(__name__)

app.register_blueprint(cliente_bp)




entorno = os.get_env("development", "development")

if entorno == "development":
    app.config.from_object(Development)
elif entorno == "Testing":
    app.config.from_object(Testing)
elif entorno == "production":
    app.config.from_object(Config)

@app.route("/")
def inicio():
    redirect(url_for(cliente_bp.login))