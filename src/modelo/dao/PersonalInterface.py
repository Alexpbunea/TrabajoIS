# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:46:50 2024

@author: ricar
"""

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.PersonalVO import Personal

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class PersonalInterface(ABC):
    @abstractmethod
    def getPersonal(self) -> List[Personal]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertPersonal(self, almacen: Personal):
        raise NotImplementedError("Método insertUsuario no implementado")