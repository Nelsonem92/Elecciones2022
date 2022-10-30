from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioResultado = RepositorioResultado()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self, infoResultado, id_candidato, id_mesa):
        resultado = Resultado(infoResultado)
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultado.candidato = candidato
        resultado.mesa = mesa
        return self.repositorioResultado.save(resultado)
    def update(self, id_resultado, infoResultado, id_candidato, id_mesa):
        resultado = Resultado(self.repositorioResultado.findById(id_resultado))
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultado.numero_votos = infoResultado['numero_votos']
        resultado.candidato = candidato
        resultado.mesa = mesa
        return self.repositorioResultado.save(resultado)
    def delete(self, id):
        return self.repositorioResultado.delete(id)
    def show(self, id):
        resultado = Resultado(self.repositorioResultado.findById(id))
        return resultado.__dict__
