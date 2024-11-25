from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])
        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro
        descuento = 0

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento * (1 - descuento)
        return render_template(
            "ejercicio1.html",
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            monto_descuento=monto_descuento,
            total_con_descuento=total_con_descuento,
        )
    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        if usuario == "juan" and contraseña == "admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario == "pepe" and contraseña == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("ejercicio2.html", mensaje=mensaje)
    return render_template("ejercicio2.html")

import webbrowser

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)