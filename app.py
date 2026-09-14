from flask import Flask, render_template, request

from calculadora import somar, subtrair, multiplicar, dividir

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():

    resultado = None

    if request.method == "POST":

        numero1 = float(request.form["numero1"])
        numero2 = float(request.form["numero2"])
        operacao = request.form["operacao"]

        if operacao == "somar":
            resultado = somar(numero1, numero2)

        elif operacao == "subtrair":
            resultado = subtrair(numero1, numero2)

        elif operacao == "multiplicar":
            resultado = multiplicar(numero1, numero2)

        elif operacao == "dividir":
            resultado = dividir(numero1, numero2)

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)