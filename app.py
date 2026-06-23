# app.py
from flask import Flask, render_template, request

from calculadora import calcular

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operacao = request.form["operacao"]
            resultado = calcular(a, b, operacao)
        except (ValueError, KeyError) as e:
            erro = str(e)
    return render_template("index.html", resultado=resultado, erro=erro)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
