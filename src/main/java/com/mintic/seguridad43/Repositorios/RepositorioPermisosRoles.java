package com.mintic.seguridad43.Repositorios;

import com.mintic.seguridad43.Modelos.PermisosRoles;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles, String> {
}
