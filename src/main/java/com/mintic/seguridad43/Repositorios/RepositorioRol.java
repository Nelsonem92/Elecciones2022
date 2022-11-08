package com.mintic.seguridad43.Repositorios;

import com.mintic.seguridad43.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}
