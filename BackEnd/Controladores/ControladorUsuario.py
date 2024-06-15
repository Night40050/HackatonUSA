from Repositorios.RepositorioUsuario import RepositorioUsuario
from Modelos.Usuarios import Usuarios
from bson import ObjectId

class ControladorUsuario():
    def __init__(self):
        self.repositorioUsuario = RepositorioUsuario()

    def index(self):
        return [usuario.__dict__ for usuario in self.repositorioUsuario.findAll()]

    def create(self, data):
        nuevoUsuario = Usuarios(data)
        usuarioGuardado = self.repositorioUsuario.save(nuevoUsuario)

        # Convierte el _id a str si es ObjectId
        if '_id' in usuarioGuardado:
            usuarioGuardado['_id'] = str(usuarioGuardado['_id'])

        return usuarioGuardado

    def show(self, id):
        elUsuario = Usuarios(self.repositorioUsuario.findById(id))
        return elUsuario.__dict__

    def update(self, id, infoUsuario):
        usuarioActual = Usuarios(self.repositorioUsuario.findById(id))
        if usuarioActual:
            usuarioActual.nombre = infoUsuario.get("nombre", usuarioActual.nombre)
            usuarioActual.nacionalidad = infoUsuario.get("nacionalidad", usuarioActual.nacionalidad)
            usuarioActual.idioma = infoUsuario.get("idioma", usuarioActual.idioma)
            usuarioActual.edad = infoUsuario.get("edad", usuarioActual.edad)
            usuarioActual.email = infoUsuario.get("email", usuarioActual.email)
            usuarioActual.contrasena = infoUsuario.get("contrasena", usuarioActual.contrasena)
            usuarioActualizado = self.repositorioUsuario.save(usuarioActual)
            return usuarioActualizado.__dict__
        return {}

    def delete(self, id):
        return {"deleted": self.repositorioUsuario.delete(id)}

