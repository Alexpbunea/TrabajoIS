# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:40:11 2024

@author: Dell XPS 9510
"""

import tkinter as tk
from tkinter import messagebox
from src.modelo.vo.ClienteVO import Cliente
from src.modelo.dao.ClienteDao import ClienteDao
from src.controlador.Coordinador import Coordinador

class Logica:
    def __init__(self):
        self._mi_coordinador = None

    def set_coordinador(self, mi_coordinador: Coordinador) -> None:
        self._mi_coordinador = mi_coordinador

    def validar_registro(self, mi_persona: Cliente):
        if '@' in mi_persona.getEmail():
            mi_persona_dao = ClienteDao()
            mi_persona_dao.insertUsuario(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")

