package com.mintic.seguridad43.Repositorios;

import com.mintic.seguridad43.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario, String> {
}
