from flask import Flask, redirect, url_for 
import os
from config import Config, Development, Testing


app= Flask(__name__)

entorno = os.get_env("development", "development")

if entorno == "development":
    app.config.from_object(Development)
elif entorno == "Testing":
    app.config.from_object(Testing)
elif entorno == "production":
    app.config.from_object(Config)