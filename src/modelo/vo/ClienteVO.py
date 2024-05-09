class Cliente:
    def __init__(self, IDcliente=None, Contrasenia=None, Nombre=None, Apellido1=None, Apellido2=None, Direccion=None, Email=None, Concesionario=None):
        self.IDcliente = IDcliente
        self.Contrasenia = Contrasenia
        self.Nombre = Nombre
        self.Apellido1 = Apellido1
        self.Apellido2 = Apellido2
        self.Direccion = Direccion
        self.Email = Email
        self.Concesionario = Concesionario

    def getIDcliente(self):
        return self.IDcliente

    def setIDcliente(self, ID):
        self.IDcliente = ID

    def getContrasenia(self):
        return self.Contrasenia

    def setContrasenia(self, contrasenia):
        self.Contrasenia = contrasenia

    def getNombre(self):
        return self.Nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getApellido1(self):
        return self.Apellido1

    def setApellido1(self, apellido1):
        self.Apellido1 = apellido1

    def getApellido2(self):
        return self.Apellido2

    def setApellido2(self, apellido2):
        self.Apellido2 = apellido2

    def getDireccion(self):
        return self.Direccion

    def setDireccion(self, direccion):
        self.Direccion = direccion

    def getEmail(self):
        return self.Email

    def setEmail(self, email):
        self.Email = email

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, concesionario):
        self.Concesionario = concesionario

    def toString(self):
        return f"IDcliente = {self.getIDcliente()}, Contraseña = {self.getContrasenia()}, Nombre = {self.getNombre()}, Apellido1 = {self.getApellido1()}, Apellido2 = {self.getApellido2()}, Direccion = {self.getDireccion()}, Email = {self.getEmail()}, Concesionario = {self.getConcesionario()}"

    def __str__(self):
        return self.toString()
