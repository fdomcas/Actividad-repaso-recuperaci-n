from . import *
from flask import Flask, redirect, url_for, abort, request, render_template

@cliente_bp.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return render_template("login.html")
    elif request.method == "GET":
        return render_template("login.html")