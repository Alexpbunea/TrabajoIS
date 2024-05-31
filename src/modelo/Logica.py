# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:40:11 2024

@author: Dell XPS 9510
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from src.controlador.Coordinador import Coordinador

from src.modelo.vo.ConcesionarioVO import Concesionario
from src.modelo.dao.ConcesionarioDao import ConcesionarioDao

from src.modelo.vo.ClienteVO import Cliente
from src.modelo.dao.ClienteDao import ClienteDao

from src.modelo.vo.AlmacenVO import AlmacenVO
from src.modelo.dao.AlmacenDao import AlmacenDao

from src.modelo.vo.PagoVO import Pago
from src.modelo.dao.PagoDao import PagoDao

from src.modelo.vo.PlantillaTrabajadorVO import PlantillaTrabajadorVO
from src.modelo.dao.PlantillaTrabajadorDAO import TrabajadorDao

from src.modelo.vo.TallerVO import Taller
from src.modelo.dao.TallerDao import TallerDao

from src.modelo.vo.VehiculosVO import Vehiculo
from src.modelo.dao.VehiculosDao import VehiculoDao

from src.modelo.vo.VentasVO import Venta
from src.modelo.dao.VentasDao import VentaDao


class Logica:
    def __init__(self):
        self._mi_coordinador = None

    def set_coordinador(self, mi_coordinador: Coordinador) -> None:
        self._mi_coordinador = mi_coordinador

    def comprobar_Dni_contrasenia(self, mi_persona):
        #print(mi_persona)
        #print(type(mi_persona))

        if isinstance(mi_persona, Cliente):
            mi_persona_dao = ClienteDao()
            clientes = mi_persona_dao.getClientes()
            
            for cliente in clientes:
                if cliente.getIDcliente() == mi_persona.getIDcliente() and cliente.getContrasenia() == mi_persona.getContrasenia():
                    print(f"Bienvenido cliente --> {cliente.getNombre()}")
                    return ('cliente',cliente.getNombre())
            #return 'invalido'

        elif isinstance(mi_persona, PlantillaTrabajadorVO):
            mi_persona_dao = TrabajadorDao()
            trabajadores = mi_persona_dao.getTrabajadores()
            
            for trab in trabajadores:
                if trab.getIDtrabajador() == mi_persona.getIDtrabajador() and trab.getContrasenia() == mi_persona.getContrasenia():
                    print(f"Bienvenido trabajador --> {trab.getNombre()}")
                    return (trab.getRol(),trab.getNombre())
            #return 'invalido'
        else:
            print("No existe ningun trabajador ni ningun cliente con esas credenciales")
            return 'invalido'
        #except:    
            #messagebox.showwarning("Advertencia", "Error al intertar acceder a la base de datos")

    
    def validar_registro_concesionario(self, mi_persona: Concesionario, queHago):
        #if '@' in mi_persona.getEmail():
        
        
        
        if queHago == "aniadir":
            try:
                nombre = mi_persona.getNombre()
                direccion = mi_persona.getDireccion()
                ciudad = mi_persona.getCiudad()
                fecha_str = mi_persona.getFechaInauguracion()
                
                #comprobando si son nulos
                if nombre is None or direccion is None or ciudad is None or fecha_str is None:
                    return "Error"
                
                #Comprobando el formato del nombre
                if nombre[:10] == "Cofermotor":
                    print("Nombre correcto")
                elif nombre[:10] == "cofermotor":
                    print("Falta mayuscula en la inicial nombre. Corrigiendo")
                    nombre = "Cofermotor" + nombre[10:]
                    mi_persona.setNombre(nombre)
                else:
                    print("Formato incorrecto de nombre")
                    return "Error"
                
                #comprobando el formato de la ciudad
                if ciudad[0].isupper() is True:
                    print("Ciudad con formato correcto")
                elif ciudad[0].isupper() is False:
                    c = ciudad[0].upper()
                    iudad = ciudad[1:]
                    ciudad = c + iudad
                    mi_persona.setCiudad(ciudad)
                else:
                    print("Formato incorrecto de la ciudad")
                    return "Error"


                #paso la fecha al formato correcto
                
                fecha_obj = datetime.strptime(fecha_str, '%d-%m-%Y')
                fecha_mysql = fecha_obj.strftime('%Y-%m-%d')
                mi_persona.setFechaInauguracion(fecha_mysql)

                mi_persona_dao = ConcesionarioDao()
                mi_persona_dao.insertConcesionario(mi_persona)
                return True
            except:
                messagebox.showwarning("Advertencia", "Error al insertar concesionario")

        elif queHago == "eliminar":
            try:
                nombre = mi_persona.getNombre()
                #Comprobando el formato del nombre
                if nombre[:10] == "Cofermotor":
                    print("Nombre correcto")
                elif nombre[:10] == "cofermotor":
                    print("Falta mayuscula en la inicial nombre. Corrigiendo")
                    nombre = "Cofermotor" + nombre[10:]
                    mi_persona.setNombre(nombre)
                else:
                    print("Formato incorrecto de nombre")
                    return "Error"

                mi_persona_dao = ConcesionarioDao()
                mi_persona_dao.deleteConcesionario(mi_persona)
                return True
            except:
                messagebox.showwarning("Advertencia", "Error al eliminar concesionario")



    def validar_registro_cliente(self, mi_persona: Cliente):
        if '@' in mi_persona.getEmail():
            mi_persona_dao = ClienteDao()
            mi_persona_dao.insertCliente(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")

