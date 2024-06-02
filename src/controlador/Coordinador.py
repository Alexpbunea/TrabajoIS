from src.modelo.vo.ClienteVO import Cliente
from src.vista.RegistroClienteVentana import RegistroClienteVentana

from src.modelo.vo.ConcesionarioVO import Concesionario
from src.vista.RegistroConcesionarioVentana import RegistroConcesionarioVentana

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



    def getViewRegistroCliente(self):
        return self._viewRegistroCliente

    def setViewRegistroCliente(self, view):
        self._viewRegistroCliente = view

    def getViewRegistroConcesionario(self):
        return self._viewRegistroConcesionario

    def setViewRegistroConcesionario(self, view):
        self._viewRegistroConcesionario = view
    
    ##############################################
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


    def registrarTrabajador(self):
       a = self._model.validar_registro_trabajador()
       return a


    def registrarCliente(self, usuario: Cliente) -> None:
       self._model.validar_registro_cliente(usuario)