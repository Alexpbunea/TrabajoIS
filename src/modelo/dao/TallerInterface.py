# -*- coding: utf-8 -*-

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.TallerVO import Taller

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class VehiculoInterface(ABC):
    @abstractmethod
    def getTalleres(self) -> List[Taller]:
        raise NotImplementedError("Método getTalleres no implementado")
    
    @abstractmethod
    def insertTaller(self, almacen: Taller):
        raise NotImplementedError("Método insertTaller no implementado")