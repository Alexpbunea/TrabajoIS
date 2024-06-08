USE datoscofermotor;

SHOW TABLES;
#insert into plantillatrabajadores(IDtrabajador, Contrasenia, Nombre, Apellido1, Apellido2, Sueldo, Rol, Concesionario)
#VALUES ("71479447R", 1234, "Nain", "Miguel", "Sanchez", 1200, "administrador", "Cofermotor1"); 
#select * FROM plantillatrabajadores;
SELECT * FROM pago;	
#SELECT * FROM concesionario;
#DROP TABLE plantillatrabajadores;
#DESCRIBE vehiculos;

#DROP TABLE vehiculos;
#ALTER TABLE clientes MODIFY COLUMN Contrasenia VARCHAR(65) NOT NULL;
#ALTER TABLE plantillaTrabajadores DROP CONSTRAINT plantillatrabajadores_chk_1;


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
    Email VARCHAR(50) NULL,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT Check_ID CHECK(
        CHAR_LENGTH(IDcliente) = 9 AND
        IDcliente REGEXP '[0-9][A-Z]'
    ),
    CONSTRAINT ClienteConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre) ON UPDATE CASCADE ON DELETE CASCADE
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
    CONSTRAINT VehiculoConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre) ON UPDATE CASCADE ON DELETE CASCADE
);
*/
#DROP TABLE pago;
#DROP TABLE ventas;
/*
CREATE TABLE ventas (
    IDventa INT AUTO_INCREMENT PRIMARY KEY,
    FechaVenta DATE NOT NULL,
    IDvehiculo VARCHAR(18) NULL,
    Repara varchar(2) NULL,
    IDcliente VARCHAR(9) NOT NULL,
    Piezas TEXT NULL,
    Cantidad TEXT NULL,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT VentasConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre) ON UPDATE CASCADE ON DELETE CASCADE
);
*/
#DROP TABLE almacen
/*
CREATE TABLE almacen (
    Pieza varchar(150) PRIMARY KEY,
    Cantidad int NOT NULL,
    PrecioPieza DECIMAL(10,2) NOT NULL,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT AlmacenConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre) ON UPDATE CASCADE ON DELETE CASCADE
);
*/
#DROP TABLE taller
/*
CREATE TABLE taller (
    IDmaquinaria INT AUTO_INCREMENT PRIMARY KEY,
    Maquinaria TEXT,
    Cantidad Int NOT NULL,
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT TallerConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre) ON UPDATE CASCADE ON DELETE CASCADE
);
*/
/*
CREATE TABLE plantillaTrabajadores (
    IDtrabajador VARCHAR(9) PRIMARY KEY NOT NULL,
    Contrasenia VARCHAR(65) NOT NULL,
    Nombre VARCHAR(20) NOT NULL,
    Apellido1 VARCHAR(20) NOT NULL,
    Apellido2 VARCHAR(20) NOT NULL,
    Sueldo DECIMAL(10, 2) NOT NULL,
    Rol VARCHAR(20) NOT NULL CHECK (Rol IN ('administrador', 'jefeZona', 'jefeDepartamento', 'personal')),
    Concesionario VARCHAR(20) NOT NULL,
    CONSTRAINT TrabajadorConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre) ON UPDATE CASCADE ON DELETE CASCADE
);
*/
#DROP TABLE pago
/*
CREATE TABLE pago (
    IDpago INT AUTO_INCREMENT PRIMARY KEY,
    #FacturaPDF LONGBLOB,
    Precio DECIMAL(10, 2) NOT NULL,
    IDventa INT NOT NULL,
    CONSTRAINT VentaPago FOREIGN KEY (IDventa) REFERENCES ventas(IDventa) ON UPDATE CASCADE ON DELETE CASCADE,
	Concesionario varchar(20),
	CONSTRAINT FK_PagoConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre) ON UPDATE CASCADE ON DELETE CASCADE

);
*/