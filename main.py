from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado
miControladorPartido = ControladorPartido()
miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["mensaje"] = "Servidor Corriendo ....."
    return jsonify(json)

#Rutas de PARTIDO
@app.route("/partidos", methods=['GET'])
def indexPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def createPartidos():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def updatePartidos(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE'])
def deletePartidos(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET'])
def showPartidos(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

#Rutas de CANDIDATOS
@app.route("/candidatos", methods=['GET'])
def indexCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def createCandidatos():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def updateCandidatos(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def deleteCandidatos(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def showCandidatos(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partido/<string:id_partido>", methods=['PUT'])
def setPartidoCandidatos(id_candidato, id_partido):
    json = miControladorCandidato.setPartido(id_candidato, id_partido)
    return jsonify(json)

#Rutas para MESAS
@app.route("/mesas", methods=['GET'])
def indexMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def createMesas():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def updateMesas(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def showMesas(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def deleteMesas(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

# Rutas de RESULTADOS
@app.route("/resultados", methods=['GET'])
def indexResultados():
    json = miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def createResultados(id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.create(data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def updateResultados(id_resultado, id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado, data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def deleteResultados(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def showResultados(id):
    json = miControladorResultado.show(id)
    return jsonify(json)
############################################################


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()

    ca = certifi.where()
    client = pymongo.MongoClient(
        dataConfig['data-db-connection'], tlsCAFile=ca)
    db = client.test
    dataBase = client[dataConfig['name-db']]
    print(dataBase.list_collection_names())

    print("Servidor corriendo..... http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])

