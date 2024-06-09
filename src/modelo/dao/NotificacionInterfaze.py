from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.NotificacionesVO import NotificacionVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class NotificacionInterface(ABC):
    @abstractmethod
    def getNotificaciones(self) -> List[NotificacionVO]:
        raise NotImplementedError("Método getNotificaciones no implementado")
    
    @abstractmethod
    def insertNotificacion(self, almacen: NotificacionVO):
        raise NotImplementedError("Método insertNotificacion no implementado")