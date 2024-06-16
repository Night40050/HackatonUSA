from bson import ObjectId

class Departamento:
    def __init__(self, _id, nombre, area):
        self._id = _id
        self.nombre = nombre
        self.area = area

    def serialize(self):
        return {
            '_id': str(self._id),
            'nombre': self.nombre,
            'area': self.area
        }

    @staticmethod
    def deserialize(data):
        return Departamento(
            _id=data.get('_id'),
            nombre=data.get('nombre'),
            area=data.get('area')
        )