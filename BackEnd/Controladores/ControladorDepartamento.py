from Modelos import Departamento
from Repositorios import RepositorioDepartamento
from main import repo_departamento


class ControladorDepartamento():
    def __init__(self):
        self.repositorioDepartamento = RepositorioDepartamento()

    def crear_departamento(self, data):
        nuevo_departamento = Departamento(data.get('id_departamento'), data.get('nombre'), data.get('area'))
        new_id = self.repositorioDepartamento.create(nuevo_departamento)
        return new_id

    def obtener_departamento(self, id_departamento):
        departamento = self.repositorioDepartamento.read(id_departamento)
        return departamento.serialize() if departamento else None

    def actualizar_departamento(self, id_departamento, data):
        departamento_actualizado = Departamento(id_departamento, data.get('nombre'), data.get('area'))
        return self.repositorioDepartamento.update(departamento_actualizado)

    def eliminar_departamento(self, id_departamento):
        return self.repositorioDepartamento.delete(id_departamento)
