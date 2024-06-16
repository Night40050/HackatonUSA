from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import json

from Controladores.ControladorDepartamento import ControladorDepartamento
from Modelos.Departamento import Departamento
from Repositorios.RepositorioDepartamento import RepositorioDepartamento

app = Flask(__name__)
cors = CORS(app)
repo_departamento = RepositorioDepartamento()

from Controladores.ControladorUsuario import ControladorUsuario
miControladorUsuario = ControladorUsuario()
miControladorDepartamento=ControladorDepartamento()

#######################################################################################
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
#######################################################################################

@app.route('/departamento', methods=['POST'])
def crear_departamento_handler():
    data = request.get_json()
    new_id = miControladorDepartamento.crear_departamento(data)
    return jsonify({'_id': new_id}), 201

@app.route('/departamento/<id_departamento>', methods=['GET'])
def obtener_departamento_handler(id_departamento):
    departamento = miControladorDepartamento.obtener_departamento(id_departamento)
    if departamento:
        return jsonify(departamento), 200
    else:
        return jsonify({'error': 'Departamento no encontrado'}), 404

@app.route('/departamento/<id_departamento>', methods=['PUT'])
def actualizar_departamento_handler(id_departamento):
    data = request.get_json()
    if miControladorDepartamento.actualizar_departamento(id_departamento, data):
        return jsonify({'message': 'Departamento actualizado correctamente'}), 200
    else:
        return jsonify({'error': 'No se pudo actualizar el departamento'}), 404

@app.route('/departamento/<id_departamento>', methods=['DELETE'])
def eliminar_departamento_handler(id_departamento):
    if miControladorDepartamento.eliminar_departamento(id_departamento):
        return jsonify({'message': 'Departamento eliminado correctamente'}), 200
    else:
        return jsonify({'error': 'No se pudo eliminar el departamento'}), 404
#######################################################################################

#######################################################################################
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
