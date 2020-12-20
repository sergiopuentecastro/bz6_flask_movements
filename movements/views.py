from movements import app
from flask import render_template


@app.route("/")
def listaIngresos():
    fIngresos = open(movements/data/basededatos.csv, "r")
    csvReader = csv.reader(fIngresos, delimiter=",", quotechar="\"")
    ingresos = list(csvReader)
    print(ingresos)
    return render_template("movementsList.html", miTexto="Ya veremos si hay movimientos o no")
