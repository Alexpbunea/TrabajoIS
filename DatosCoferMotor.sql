USE datoscofermotor;

#SHOW TABLES;
#insert into plantillatrabajadores(IDtrabajador, Contrasenia, Nombre, Apellido1, Apellido2, Sueldo, Rol, Concesionario)
#VALUES ("71479447R", 1234, "Nain", "Miguel", "Sanchez", 1200, "administrador", "Cofermotor1"); 
#select * FROM plantillatrabajadores;
#SELECT * FROM clientes;
SELECT * FROM concesionario;

/*
CREATE TABLE concesionario (
    Nombre VARCHAR(20) PRIMARY KEY NOT NULL,
    Direccion VARCHAR(200) NOT NULL,
    Ciudad VARCHAR(20) NOT NULL,
    FechaInauguracion DATE NOT NULL
);
*/
/*
CREATE TABLE clientes (
    IDcliente VARCHAR(9) PRIMARY KEY NOT NULL,
    Contrasenia VARCHAR(50) NOT NULL,
    Nombre VARCHAR(30) NOT NULL,
    Apellido1 VARCHAR(30) NOT NULL,
    Apellido2 VARCHAR(30) NOT NULL,
    Direccion VARCHAR(200) NOT NULL,
    Email VARCHAR(50),
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT Check_ID CHECK(
        CHAR_LENGTH(IDcliente) = 9 AND
        IDcliente REGEXP '[0-9][A-Z]'
    ),
    CONSTRAINT ClienteConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)
);
*/
/*
CREATE TABLE vehiculos (
    IDvehiculo VARCHAR(18) PRIMARY KEY NOT NULL,
    Marca VARCHAR(20) NOT NULL,
    Modelo VARCHAR(30) NOT NULL,
    Año INT NOT NULL,
    Combustible VARCHAR(10) NOT NULL CHECK (Combustible IN ('gasolina', 'electrico', 'diesel', 'hibrido')),
    Kilometros INT NOT NULL CHECK (Kilometros >= 0 AND Kilometros <= 2000000),
    Precio DECIMAL(10, 2) NOT NULL,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT VehiculoConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)
);

CREATE TABLE ventas (
    IDventa INT AUTO_INCREMENT PRIMARY KEY,
    FechaVenta DATE NOT NULL,
    IDvehiculo VARCHAR(18) NULL,
    IDcliente VARCHAR(9) NOT NULL,
    Piezas TEXT NULL,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT VentasConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)
);

CREATE TABLE almacen (
    Capacidad INT DEFAULT 50 NOT NULL,
    Piezas TEXT,
    PorcentajeOcupado INT NOT NULL,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT AlmacenConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)
);

CREATE TABLE taller (
    horario VARCHAR(20) NOT NULL,
    Maquinaria TEXT,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT TallerConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)
);
*/
/*
CREATE TABLE plantillaTrabajadores (
    IDtrabajador VARCHAR(9) PRIMARY KEY NOT NULL,
    Contrasenia VARCHAR(50) NOT NULL,
    Nombre VARCHAR(20) NOT NULL,
    Apellido1 VARCHAR(20) NOT NULL,
    Apellido2 VARCHAR(20) NOT NULL,
    Sueldo DECIMAL(10, 2) NOT NULL,
    Rol VARCHAR(20) NOT NULL CHECK (Rol IN ('administrador', 'jefeZona', 'jefeDepartamento', 'personal')),
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT TrabajadorConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)
);
*/
/*
CREATE TABLE administrador (
    IDadmin VARCHAR(9) PRIMARY KEY NOT NULL,
    CONSTRAINT FK_IDtrabajador FOREIGN KEY (IDadmin) REFERENCES plantillaTrabajadores(IDtrabajador)
);

CREATE TABLE jefeZona (
    IDjefeZona VARCHAR(9) PRIMARY KEY NOT NULL,
    CONSTRAINT FK_IDtrabajador1 FOREIGN KEY (IDjefeZona) REFERENCES plantillaTrabajadores(IDtrabajador)
);

CREATE TABLE jefeDepartamento (
    IDjefeDepart VARCHAR(9) PRIMARY KEY NOT NULL,
    JefeZona VARCHAR(9) NOT NULL,
    CONSTRAINT FK_IDtrabajador2 FOREIGN KEY (IDjefeDepart) REFERENCES plantillaTrabajadores(IDtrabajador),
    CONSTRAINT JefeZonaJefeDepartamento FOREIGN KEY (JefeZona) REFERENCES jefeZona(IDjefeZona)
);

CREATE TABLE personal (
    IDpersonal VARCHAR(9) PRIMARY KEY NOT NULL,
    JefeDepartamento VARCHAR(9) NOT NULL,
    CONSTRAINT FK_IDtrabajador3 FOREIGN KEY (IDpersonal) REFERENCES plantillaTrabajadores(IDtrabajador),
    CONSTRAINT JefeDepartamentoPersonal FOREIGN KEY (JefeDepartamento) REFERENCES jefeDepartamento(IDjefeDepart)
);

CREATE TABLE pago (
    IDpago INT PRIMARY KEY NOT NULL,
    FacturaPDF LONGBLOB,
    CONSTRAINT VentaPago FOREIGN KEY (IDpago) REFERENCES ventas(IDventa),
	Concesionario varchar(20),
	CONSTRAINT FK_PagoConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)

);
*/