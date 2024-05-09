class Vehiculo:
    def __init__(self, IDvehiculo=None, Marca=None, Modelo=None, Anio=None, Combustible=None, Kilometros=None, Precio=None, Concesionario=None):
        self.IDvehiculo = IDvehiculo
        self.Marca = Marca
        self.Modelo = Modelo
        self.Anio = Anio
        self.Combustible = Combustible
        self.Kilometros = Kilometros
        self.Precio = Precio
        self.Concesionario = Concesionario

    def getIDvehiculo(self):
        return self.IDvehiculo

    def setIDvehiculo(self, ID):
        self.IDvehiculo = ID

    def getMarca(self):
        return self.Marca

    def setMarca(self, marca):
        self.Marca = marca

    def getModelo(self):
        return self.Modelo

    def setModelo(self, modelo):
        self.Modelo = modelo

    def getAnio(self):
        return self.Anio

    def setAnio(self, anio):
        self.Anio = anio

    def getCombustible(self):
        return self.Combustible

    def setCombustible(self, combustible):
        self.Combustible = combustible

    def getKilometros(self):
        return self.Kilometros

    def setKilometros(self, kilometros):
        self.Kilometros = kilometros

    def getPrecio(self):
        return self.Precio

    def setPrecio(self, precio):
        self.Precio = precio

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, concesionario):
        self.Concesionario = concesionario

    def isPrimeraMano(self):
        return self.Kilometros == 0

    def toString(self):
        return f"IDvehiculo = {self.getIDvehiculo()}, Marca = {self.getMarca()}, Modelo = {self.getModelo()}, Año = {self.getAnio()}, Combustible = {self.getCombustible()}, Kilometros = {self.getKilometros()}, Precio = {self.getPrecio()}, Concesionario = {self.getConcesionario()}"

    def __str__(self):
        return self.toString()
