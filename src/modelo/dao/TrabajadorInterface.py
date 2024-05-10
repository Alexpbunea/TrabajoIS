# -*- coding: utf-8 -*-

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.PlantillaTrabajadorVO import PlantillaTrabajadorVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class PagoInterface(ABC):
    @abstractmethod
    def getTrabajadores(self) -> List[PlantillaTrabajadorVO]:
        raise NotImplementedError("Método getTrabajadores no implementado")
    
    @abstractmethod
    def insertTrabajador(self, almacen: PlantillaTrabajadorVO):
        raise NotImplementedError("Método insertTrabajador no implementado")