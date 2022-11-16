from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests
import re

app = Flask(__name__)
cors = CORS(app)

from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios/validate"
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(identity=user, expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        return jsonify({"mensaje": "Usuario y/o contraseña incorrecta"})

@app.route("/", methods=['GET'])
def test():
    json = {}
    json['message'] = "Servidor ejecutandose...."
    return jsonify(json)

#######################################
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/candidatos"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def createCandidatos():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/candidatos"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def updateCandidatos(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/candidatos/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def deleteCandidatos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/candidatos/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def showCandidatos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/candidatos/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partido/<string:id_partido>", methods=['PUT'])
def setPartidoCandidatos(id_candidato, id_partido):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/candidatos/" + id_candidato + "/partido/" + id_partido
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

########################
@app.route("/partidos", methods=['GET'])
def getPartidos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/partidos"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def createPartidos():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/partidos"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def updatePartidos(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/partidos/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE'])
def deletePartidos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/partidos/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET'])
def showPartidos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/partidos/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

############
@app.route("/mesas", methods=['GET'])
def getMesas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/mesas"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def createMesas():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/mesas"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def updateMesas(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/mesas/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def deleteMesas(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/mesas/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def showMesas(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/mesas/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

########################
@app.route("/resultados", methods=['GET'])
def getResultados():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/resultados"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def createResultados(id_candidato, id_mesa):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/resultados/candidato/" + id_candidato + "/mesa/" + id_mesa
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['PUT'])
def updateResultados(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/resultados/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def deleteResultados(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/resultados/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def showResultados(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-registry'] + "/resultados/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

########################
@app.route("/usuarios", methods=['GET'])
def getUsuarios():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios", methods=['POST'])
def createUsuarios():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios/<string:id>", methods=['PUT'])
def updateUsuarios(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios/<string:id>", methods=['DELETE'])
def deleteUsuarios(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios/<string:id>", methods=['GET'])
def showUsuarios(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios/<string:id_usuario>/rol/<string:id_rol>", methods=['PUT'])
def setRolUsuarios(id_usuario, id_rol):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios/" + id_usuario + "/rol/" + id_rol
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios/validate", methods=['POST'])
def validateUsuarios():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/usuarios/validate"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)




#########################
@app.route("/roles", methods=['GET'])
def getRoles():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/roles"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/roles", methods=['POST'])
def createRoles():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/roles"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/roles/<string:id>", methods=['PUT'])
def updateRoles(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/roles/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/roles/<string:id>", methods=['DELETE'])
def deleteRoles(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/roles/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/roles/<string:id>", methods=['GET'])
def showRoles(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/roles/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

########################
@app.route("/permisos", methods=['GET'])
def getPermisos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/permisos", methods=['POST'])
def createPermisos():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/permisos/<string:id>", methods=['PUT'])
def updatePermisos(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/permisos/<string:id>", methods=['DELETE'])
def deletePermisos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/permisos/<string:id>", methods=['GET'])
def showPermisos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security' ] + "/permisos/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

############
@app.route("/permisos-roles", methods=['GET'])
def getPermisosRoles():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos-roles"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles", methods=['POST'])
def createPermisosRoles():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos-roles"
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/<string:id>", methods=['PUT'])
def updatePermisosRoles(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos-roles/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/<string:id>", methods=['DELETE'])
def deletePermisosRoles(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos-roles/" + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/<string:id>", methods=['GET'])
def showPermisosRoles(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos-roles/" + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/validar-permiso/rol/<string:id>", methods=['GET'])
def validarPermisosRoles(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig['url-backend-security'] + "/permisos-roles/validar-permiso/rol/" + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


###################
@app.before_request
def before_request():
    endPoint = limpiarUrl(request.path)
    excludedRoutes = ["/login", "/register", "/change-password"]
    if (excludedRoutes.__contains__(request.path)):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            tienePermiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            if tienePermiso:
                pass
            else:
                return jsonify({"message": "Permiso denegado"})
        else:
            return jsonify({"message": "Permiso denegado, no se ha asignado el rol"})


def validarPermiso(endPoint, metodo, rol):
    url = dataConfig['url-backend-security'] + "/permisos-roles/validar-permiso/rol/" + str(rol)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    tienePermiso = False
    response = requests.get(url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso




def limpiarUrl(url):
    partes = url.split("/")
    for parte in partes:
        if re.search('\\d', parte):
            url = url.replace(parte, "?")
    return url



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Servidor ejecutandose... http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])