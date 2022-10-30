from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self, infoMesa):
        mesa = Mesa(infoMesa)
        return self.repositorioMesa.save(mesa)
    def update(self, id, infoMesa):
        mesa = Mesa(self.repositorioMesa.findById(id))
        mesa.numero = infoMesa['numero']
        mesa.cantidad_inscritos = infoMesa['cantidad_inscritos']
        return self.repositorioMesa.save(mesa)
    def delete(self, id):
        return self.repositorioMesa.delete(id)
    def show(self, id):
        mesa = Mesa(self.repositorioMesa.findById(id))
        return mesa.__dict__