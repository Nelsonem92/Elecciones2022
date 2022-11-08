package com.mintic.seguridad43.Repositorios;

import com.mintic.seguridad43.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso extends MongoRepository<Permiso, String> {
}
