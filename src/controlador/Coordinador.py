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
    def getViewRegistro(self):
       return self._viewRegistro
    
    def setViewRegistro(self, view):
       self._viewRegistro = view
    
    ##############################################

    def registrarConcesionario(self, usuario: Concesionario) -> None:
       self._model.validar_registro_concesionario(usuario)


    #def registrarCliente(self, usuario: Cliente) -> None:
    #   self._model.validar_registro(usuario)