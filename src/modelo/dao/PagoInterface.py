# -*- coding: utf-8 -*-

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.PagoVO import Pago

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class PagoInterface(ABC):
    @abstractmethod
    def getPagos(self) -> List[Pago]:
        raise NotImplementedError("Método getPagos no implementado")
    
    @abstractmethod
    def insertPago(self, almacen: Pago):
        raise NotImplementedError("Método insertPago no implementado")