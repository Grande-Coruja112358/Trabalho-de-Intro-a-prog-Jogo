import math
import pandas as pd
import numpy as np
import pygames
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Tela Inicial"

@app.route("/nova-janela")
def nova_janela():
    return "<h1>Esta é a nova janela do programa</h1>"
    # Para usar um arquivo HTML, substitua a linha acima por:
    # return render_template("nova_janela.html")

if __name__ == "__main__":
    app.run(debug=True)
