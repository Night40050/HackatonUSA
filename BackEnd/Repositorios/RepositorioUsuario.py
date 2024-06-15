# RepositorioUsuario.py
from pymongo import MongoClient
from bson.objectid import ObjectId
from Modelos.Usuarios import Usuarios
from Repositorios.InterfaceRepositorio import InterfaceRepositorio, T


class RepositorioUsuario(InterfaceRepositorio[Usuarios]):
    def __init__(self):
        super().__init__()
        self.collection = self.baseDatos["usuarios"]

    def findAll(self):
        return list(self.collection.find())

    def findById(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def save(self, item: T) -> T:
        laColeccion = self.baseDatos[self.coleccion]
        elId = ""
        item = self.transformRefs(item)

        if hasattr(item, "_id") and item._id:
            elId = item._id
            _id = ObjectId(elId)
            delattr(item, "_id")
            item = item.__dict__
            updateItem = {"$set": item}
            x = laColeccion.update_one({"_id": _id}, updateItem)
            # Devuelve el objeto actualizado, convirtiendo _id a str
            return self.findById(elId)
        else:
            # Asigna un nuevo _id si no está definido
            item._id = ObjectId()
            _id = laColeccion.insert_one(item.__dict__)
            elId = _id.inserted_id.__str__()
            # Devuelve el objeto recién insertado, convirtiendo _id a str
            return self.findById(elId)

    def delete(self, id):
        return self.collection.delete_one({"_id": ObjectId(id)})

