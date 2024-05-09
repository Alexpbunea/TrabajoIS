
/*create table concesionario(
	Nombre varchar(20) PRIMARY KEY NOT NULL,
	Direccion varchar(200) NOT NULL,
	Ciudad varchar(20) NOT NULL,
	FechaInauguracion date NOT NULL
)*/



--Modificaciones atributos de cliente: IDcliente, Nombre, Apellido1, Apellido2, Direccion, Email
/*create table clientes (
	IDcliente varchar(9) PRIMARY KEY NOT NULL,
	Contraseña varchar(50) NOT NULL,
	Nombre varchar(30) NOT NULL,
	Apellido1 varchar(30) NOT NULL,
	Apellido2 varchar(30) NOT NULL,
	Direccion varchar(200) NOT NULL,
	Email varchar(50) NULL,
	Concesionario varchar(20) NOT NULL,
	CONSTRAINT Check_ID CHECK(
		LEN(IDcliente) = 9 AND
		Idcliente LIKE '[0-9][A-Z]%'
	),
	--CONSTRAINT Check_contra CHECK (
	--	LEN(Contraseña) >= 5 AND
	--	Contraseña LIKE '%[0-9]%' AND
	--	Contraseña COLLATE Latin1_General_BIN LIKE '%[A-Z]%' AND
    --  Contraseña LIKE '%[!@#$%^&*()-_+=]%'
	--),
	CONSTRAINT ClienteConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)

)*/

--Modificaciones atributos de vehiculos: Identificador, Marca, modelo, año, combustible, kilómetros, precio, primeraMano(true/false)
/*create table vehiculos (
	IDvehiculo varchar(18) PRIMARY KEY NOT NULL,
	Marca varchar(20) NOT NULL,
	Modelo varchar(30) NOT NULL,
	Año int NOT NULL,
	Combustible varchar(10) NOT NULL CHECK (Combustible IN ('gasolina', 'electrico', 'diesel', 'hibrido')),
	Kilometros int NOT NULL CHECK (Kilometros >= 0 AND Kilometros <= 2000000),
	Precio money NOT NULL,
	PrimeraMano AS (CASE WHEN Kilometros = 0 THEN 'True' ELSE 'False' END),
	Concesionario varchar(20) NOT NULL,
	CONSTRAINT VehiculoConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre),
)*/

--Ventas: indentificador venta, fichavehiculo, fecha y hora
/*create table ventas(
	IDventa int PRIMARY KEY IDENTITY(1,1),
	FechaVenta DATE NOT NULL,
	IDvehiculo VARCHAR(18) NULL,
    IDcliente VARCHAR(9) NOT NULL,
	Concesionario varchar(20) NOT NULL,
    CONSTRAINT FK_IDvehiculo FOREIGN KEY (IDvehiculo) REFERENCES vehiculos(IDvehiculo),
    CONSTRAINT FK_IDcliente FOREIGN KEY (IDcliente) REFERENCES clientes(IDcliente),
	CONSTRAINT VentasConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre),
)*/
/*
create table almacen(
	Capacidad int DEFAULT 50 NOT NULL,
	Piezas varchar(max) DEFAULT '',
	PorcentajeOcupado int NOT NULL,
	Concesionario varchar(20) NOT NULL,
	CONSTRAINT AlmacenConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre),
)*/
/*
create table taller (
	horario varchar(20) NOT NULL,
	Maquinaria varchar(max) NULL,
	Concesionario varchar(20) NOT NULL,
	CONSTRAINT TallerConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre),
	CONSTRAINT TallerAlmacenConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre)
)*/

/*create table plantillaTrabajadores (
	IDtrabajador varchar(9) PRIMARY KEY NOT NULL,
	Contraseña varchar(50) NOT NULL,
	Nombre varchar(20) NOT NULL,
	Apellido1 varchar(20) NOT NULL,
	Apellido2 varchar(20) NOT NULL,
	Sueldo money NOT NULL,
	Concesionario varchar(20) NOT NULL,
	CONSTRAINT TrabajadorConcesionario FOREIGN KEY (Concesionario) REFERENCES concesionario(Nombre),
)*/
/*
create table administrador(
	IDadmin varchar(9) NOT NULL,
	CONSTRAINT FK_IDtrabajador FOREIGN KEY (IDadmin) REFERENCES plantillaTrabajadores(IDtrabajador)
)*/

/*create table jefeZona(
	IDjefeZona varchar(9) PRIMARY KEY NOT NULL,
	CONSTRAINT FK_IDtrabajador1 FOREIGN KEY (IDjefeZona) REFERENCES plantillaTrabajadores(IDtrabajador)
)*/

/*create table jefeDepartamento(
	IDjefeDepart varchar(9) PRIMARY KEY NOT NULL,
	JefeZona varchar(9) NOT NULL,
	CONSTRAINT FK_IDtrabajador2 FOREIGN KEY (IDjefeDepart) REFERENCES plantillaTrabajadores(IDtrabajador),
	CONSTRAINT JefeZonaJefeDepartamento FOREIGN KEY (JefeZona) REFERENCES jefeZona(IDjefeZona)
)

create table personal(
	IDpersonal varchar(9) PRIMARY KEY NOT NULL,
	JefeDepartamento varchar(9) NOT NULL,
	CONSTRAINT FK_IDtrabajador3 FOREIGN KEY (IDpersonal) REFERENCES plantillaTrabajadores(IDtrabajador),
	CONSTRAINT JefeDepartamentoPersonal FOREIGN KEY (JefeDepartamento) REFERENCES jefeDepartamento(IDjefeDepart)

)*/

/*create table pago(
	IDpago int PRIMARY KEY NOT NULL,
	FacturaPDF VARBINARY(MAX),
	CONSTRAINT VentaPago FOREIGN KEY (IDpago) REFERENCES ventas(IDventa),
)*/


--DROP TABLE jefeZona;

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';

