# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:44:47 2024

@author: ricar
"""

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.PagoVO import Pago

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class PagoInterface(ABC):
    @abstractmethod
    def getPagos(self) -> List[Pago]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertPago(self, almacen: Pago):
        raise NotImplementedError("Método insertUsuario no implementado")