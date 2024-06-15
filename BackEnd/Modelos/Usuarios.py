from Modelos.AbstractModelo import AbstractModelo
class Usuarios(AbstractModelo):
    def __init__(self, data):
        self._id = data.get("_id", None)
        self.nombre = data.get("nombre")
        self.nacionalidad = data.get("nacionalidad")
        self.idioma = data.get("idioma")
        self.edad = data.get("edad")
        self.email = data.get("email")
        self.contrasena = data.get("contrasena")
    pass