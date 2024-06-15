from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import json

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorUsuario import ControladorUsuario
miControladorUsuario = ControladorUsuario()

@app.route("/usuario", methods=['GET'])
def getUsuarios():
    return jsonify(miControladorUsuario.index())

@app.route("/usuario", methods=['POST'])
def crearUsuario():
    data = request.get_json()
    return jsonify(miControladorUsuario.create(data))

@app.route("/usuario/<string:id>", methods=['GET'])
def getUsuario(id):
    return jsonify(miControladorUsuario.show(id))

@app.route("/usuario/<string:id>", methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    return jsonify(miControladorUsuario.update(id, data))

@app.route("/usuario/<string:id>", methods=['DELETE'])
def eliminarUsuario(id):
    return jsonify(miControladorUsuario.delete(id))

@app.route("/", methods=['GET'])
def test():
    return jsonify({"message": "Server running ..."})

def loadFileConfig():
    with open('config.json') as f:
        return json.load(f)

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
