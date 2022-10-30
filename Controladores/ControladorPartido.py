from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioPartido.findAll()
    def create(self, infoPartido):
        partido = Partido(infoPartido)
        return self.repositorioPartido.save(partido)
    def update(self, id, infoPartido):
        partido = Partido(self.repositorioPartido.findById(id))
        partido.nombre = infoPartido['nombre']
        partido.lema = infoPartido['lema']
        return self.repositorioPartido.save(partido)
    def delete(self, id):
        return self.repositorioPartido.delete(id)
    def show(self, id):
        partido = Partido(self.repositorioPartido.findById(id))
        return partido.__dict__
