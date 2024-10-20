from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# Inscripcion en curso
@app.route("/inscripciones.html")
def inscripciones():
    return render_template("inscripciones.html")


@app.route("/inscripcion", methods=["POST"])
def inscripcion():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    curso = request.form.get("curso")
    return render_template(
        "salida_inscripciones.html", nombre=nombre, apellidos=apellidos, curso=curso
    )


# Registro de usuarios
@app.route("/registro_usuarios.html")
def usuarios():
    return render_template("registro_usuarios.html")


@app.route("/usuario", methods=["POST"])
def usuario():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template(
        "salida_usuarios.html",
        nombre=nombre,
        apellidos=apellidos,
        email=email,
        password=password,
    )

#Registro de productos
@app.route("/registro_productos.html")
def productos():
    return render_template("registro_productos.html")

@app.route("/producto", methods = ["POST"])
def producto():
    producto = request.form.get("producto")
    categoria = request.form.get("categoria")
    existencia = request.form.get("existencia")
    precio = int(request.form.get("precio"))
    return render_template("salida_productos.html", producto = producto, categoria = categoria, existencia = existencia, precio = precio)

#Registro de libros
@app.route("/registro_libros.html")
def libros():
    return render_template("/registro_libros.html")

@app.route("/libro", methods=["POST"])
def libro():
    titulo = request.form.get("titulo")
    autor = request.form.get("autor")
    resumen = request.form.get("resumen")
    medio = request.form.get("medio")
    return render_template(
        "salida_libros.html", titulo = titulo, autor=autor, resumen=resumen, medio=medio)

if __name__ == "__main__":
    app.run(debug=True)
