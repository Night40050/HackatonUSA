from pymongo import MongoClient
from bson import ObjectId
from Modelos import Departamento

class ControladorDepartamento:
    def __init__(self):
        super().__init__()
        self.collection = self.baseDatos["departamentos"]

    def crear_departamento(self, data):
        nuevo_departamento = Departamento(data.get('_id'), data.get('nombre'), data.get('area'))
        new_id = self.repositorio_departamento.create(nuevo_departamento)
        return new_id

    def obtener_departamento(self, id_departamento):
        departamento = self.repositorio_departamento.read(id_departamento)
        return departamento.serialize() if departamento else None

    def actualizar_departamento(self, id_departamento, data):
        departamento_actualizado = Departamento(id_departamento, data.get('nombre'), data.get('area'))
        return self.repositorio_departamento.update(departamento_actualizado)

    def eliminar_departamento(self, id_departamento):
        return self.repositorio_departamento.delete(id_departamento)

    def delete(self, id_departamento):
        result = self.collection.delete_one({'_id': ObjectId(id_departamento)})
        return result.deleted_count > 0
