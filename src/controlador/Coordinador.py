from src.modelo.vo.ClienteVO import Cliente

from src.modelo.vo.ConcesionarioVO import Concesionario

from src.modelo.vo.AlmacenVO import AlmacenVO
#from src.modelo.dao.AlmacenDao import AlmacenDao

from src.modelo.vo.PagoVO import Pago
#from src.modelo.dao.PagoDao import PagoDao

from src.modelo.vo.PlantillaTrabajadorVO import PlantillaTrabajadorVO
#from src.modelo.dao.PlantillaTrabajadorDAO import TrabajadorDao

from src.modelo.vo.TallerVO import Taller
#from src.modelo.dao.TallerDao import TallerDao

from src.modelo.vo.VehiculosVO import Vehiculo
#from src.modelo.dao.VehiculosDao import VehiculoDao

from src.modelo.vo.VentasVO import Venta
#from src.modelo.dao.VentasDao import VentaDao

class Coordinador:
    def __init__(self):
      self._model = None
      #Puede tener tantas referencias a ventanas como controle
      self._viewRegistro = None
      
    def getModel(self):
       return self._model
    
    def setModel(self, model):
       self._model = model
    
    #Se añade para cada ventana
    def getViewVentanaPrincipal(self):
       return self._viewVentanaPrincipal
    def setViewVentanaPrincipal(self, view):
       self._viewVentanaPrincipal = view


    def getViewVentanaIniciarSesion(self):
       return self._viewVentanaIniciarSesion
    def setViewVentanaIniciarSesion(self, view):
       self._viewVentanaIniciarSesion = view


    def getViewVentanaAdmin(self):
       return self._viewVentanaAdmin
    def setViewVentanaAdmin(self, view):
       self._viewVentanaAdmin = view


    def getViewVentanaConcesionario(self):
       return self._viewVentanaConcesionario
    def setViewVentanaConcesionario(self, view):
       self._viewVentanaConcesionario = view


    def getViewVentanaTrabajadores(self):
       return self._viewVentanaTrabajadores
    def setViewVentanaTrabajadores(self, view):
       self._viewVentanaTrabajadores = view



    def getViewVentanaCliente(self):
        return self._viewRegistroCliente

    def setViewVentanaClientes(self, view):
        self._viewVentanaClientes = view

    
    def getViewVentanaVehiculos(self):
       return self._viewVentanaVehiculos
    
    def setViewVentanaVehiculos(self, view):
       self._viewVentanaVehiculos = view


    def getViewRegistroConcesionario(self):
        return self._viewRegistroConcesionario

    def setViewRegistroConcesionario(self, view):
        self._viewRegistroConcesionario = view

    
    def getViewRegistroVentas(self):
        return self._ViewRegistroVentas

    def setViewRegistroVentas(self, view):
        self._viewRegistroVentas = view


    def getViewVentanaAlmacen(self):
        return self._ViewVentanaAlmacen

    def setViewVentanaAlmacen(self, view):
        self._ViewVentanaAlmacen = view

    
    def getViewVentanaTaller(self):
        return self._ViewVentanaTaller

    def setViewVentanaTaller(self, view):
        self._ViewVentanaTaller = view


    def getViewVentanaPago(self):
        return self._ViewVentanaPago

    def setViewVentanaPago(self, view):
        self._ViewVentanaPago = view


    def getViewVentanaParaCliente(self):
        return self._viewRegistroCliente

    def setViewVentanaParaClientes(self, view):
        self._viewVentanaParaClientes = view
      

    def getViewVentanaParaJefeZona(self):
        return self._viewRegistroCliente

    def setViewVentanaParaJefeZona(self, view):
        self._viewVentanaParaClientes = view
    
    def getViewVentanaParaPersonal(self):
       return self._viewVentanaPersonal
    
    def setViewVentanaParaPersonal(self, view):
       self._viewVentanaPersonal = view
       
    
    ##########################################################################################################################################
    ##########################################################################################################################################
    ##########################################################################################################################################
    ##########################################################################################################################################
    ##########################################################################################################################################
    ##########################################################################################################################################


    def comprobarIniciarSesion(self, usuario, usuario2):
       a = self._model.comprobar_Dni_contrasenia(usuario, usuario2)
       return a


    def registrarConcesionario(self, usuario, queHago) -> None:
       a = self._model.validar_registro_concesionario(usuario, queHago)
       #print(a)
       return a
    def obtenerConcesionarios(self):
       a = self._model.obtener_todos_concesionarios()
       return a


    def registrarTrabajador(self, usuario, queHago):
       a = self._model.validar_registro_trabajador(usuario, queHago)
       return a
    def obtenerTrabajadores(self):
       a = self._model.obtener_todos_trabajadores()
       return a


    def registrarCliente(self, usuario, queHago):
       a = self._model.validar_registro_cliente(usuario, queHago)
       return a
    def obtenerClientes(self):
       a = self._model.obtener_todos_clientes()
       return a
    

    def registrarVehiculo(self, usuario, queHago):
       a = self._model.validar_registro_vehiculos(usuario, queHago)
       return a
    def obtenerVehiculos(self):
       a = self._model.obtener_todos_vehiculos()
       return a
    
    def registrarPieza(self, usuario, queHago):
        a = self._model.validar_registro_piezas(usuario, queHago)
        return a
    def obtenerPiezas(self):
       a = self._model.obtener_todas_piezas()
       return a
    

    def registrarMaquinaria(self, usuario, queHago):
        a = self._model.validar_registro_maquinaria(usuario, queHago)
        return a
    def obtenerMaquinaria(self):
       a = self._model.obtener_todas_maquinas()
       return a
  

    def registrarVenta(self, usuario, queHago, quienSoy=None):
        a = self._model.validar_registro_ventas(usuario, queHago, quienSoy)
        return a
    def obtenerVentas(self):
       a = self._model.obtener_todas_ventas()
       return a
    

    def registrarPago(self, usuario, queHago):
        a = self._model.validar_registro_pagos(usuario, queHago)
        return a
    def obtenerPagos(self):
       a = self._model.obtener_todos_pagos()
       return a


    def obtenerNotificaciones(self):
       a = self._model.obtenerTodasNotificaciones()
       return a
    
   #AQUI LOS CLIENTES ENVIARAN LA NOTIFICACION DE COMPRA AL PERSONAL
    def registrarNotificacionCompra(self, usuario, queHago, dondeEstoy, quienSoy):
       a = self._model.comprarReparaVehiculoCliente(usuario, queHago, dondeEstoy, quienSoy)
       return a