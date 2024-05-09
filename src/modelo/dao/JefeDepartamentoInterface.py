# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:38:50 2024

@author: ricar
"""

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.JefeDepartamentoVO import JefeDepartamento

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class JefeDepartamentoInterface(ABC):
    @abstractmethod
    def getJefesDepartamento(self) -> List[JefeDepartamento]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertJefeDepartamento(self, almacen: JefeDepartamento):
        raise NotImplementedError("Método insertUsuario no implementado")