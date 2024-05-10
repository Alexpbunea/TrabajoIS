# -*- coding: utf-8 -*-

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.VehiculosVO import Vehiculo

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class VehiculoInterface(ABC):
    @abstractmethod
    def getVehiculos(self) -> List[Vehiculo]:
        raise NotImplementedError("Método getVehiculos no implementado")
    
    @abstractmethod
    def insertVehiculo(self, almacen: Vehiculo):
        raise NotImplementedError("Método insertVehiculo no implementado")