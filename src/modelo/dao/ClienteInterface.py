# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:15:37 2024

@author: ricar
"""

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.ClienteVO import Cliente

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ClienteInterface(ABC):
    @abstractmethod
    def getClientes(self) -> List[Cliente]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertCliente(self, almacen: Cliente):
        raise NotImplementedError("Método insertUsuario no implementado")