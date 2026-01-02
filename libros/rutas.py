from flask import Blueprint, redirect, render_template, url_for, abort, request, make_response
import json

libros_bp= Blueprint("libros_bp",__name__,template_folder='templates')



def lista_cokis():
    libros_cookie = request.cookies.get("libros")
    if libros_cookie:
        try:
            return json.loads(libros_cookie)
        except json.JSONDecodeError:
            return []
    return []



@libros_bp.route("/mostrar")
def mostrar():
    if request.cookies.get("cliente") is not None:
        lista = lista_cokis()
        print(lista)
        return render_template("libros/catalogo.html", libros=lista)
    else:
        abort(401, description="deves logearte")

@libros_bp.route("/libros", methods= ["POST","GET"])
def agregar_libro():
    titulo=request.form.get("titulo")
    descrp=request.form.get("descripcion")

    if request.method == "GET":
        return render_template("libros/añadir.html")
    elif request.method == "POST":
        lista= lista_cokis()
        if titulo not in [libro["titulo"] for libro in lista ]:
            lista.append({"titulo":titulo, "descripcion":descrp})
            resp=  make_response(redirect(url_for('libros_bp.mostrar')))
            resp.set_cookie("libros", json.dumps(lista))
            return resp
        else:
            return render_template('libros/catalogo.html', libros=lista, agregado="Este libro ya esta dentro")


@libros_bp.route("/borrar", methods= ["POST","GET"])
def borrar_libro():
    lista= lista_cokis()
    if request.method == "GET":
        return render_template("libros/borrar.html")
    elif request.method == "POST":
         titulo= request.form.get("titulo")
         for ind ,libro in enumerate(lista):
            if libro["titulo"] == titulo:
                del lista[ind]
                resp=  make_response(redirect(url_for('libros_bp.mostrar')))
                resp.set_cookie("libros", json.dumps(lista))
                return resp
            else:
                return render_template('libros/catalogo.html', libros=lista, agregado="Libro no encontrado")
                
            
    
             
