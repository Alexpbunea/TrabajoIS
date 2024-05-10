# -*- coding: utf-8 -*-

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.ConcesionarioVO import Concesionario

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ConcesionarioInterface(ABC):
    @abstractmethod
    def getConcesionarios(self) -> List[Concesionario]:
        raise NotImplementedError("Método getConcesionarios no implementado")
    
    @abstractmethod
    def insertConcesionario(self, almacen: Concesionario):
        raise NotImplementedError("Método insertConcesionario no implementado")