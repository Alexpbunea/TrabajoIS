# -*- coding: utf-8 -*-

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.VentasVO import Venta

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class PagoInterface(ABC):
    @abstractmethod
    def getVentas(self) -> List[Venta]:
        raise NotImplementedError("Método getVentas no implementado")
    
    @abstractmethod
    def insertVenta(self, almacen: Venta):
        raise NotImplementedError("Método insertVenta no implementado")