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

    def comprobar_Dni_contrasenia(self, mi_persona, mi_trabajador):
        #print(mi_persona)
        #print(type(mi_persona))
        mi_persona_dao = ClienteDao()
        clientes = mi_persona_dao.getClientes()

        mi_trabajador_dao = TrabajadorDao()
        trabajadores = mi_trabajador_dao.getTrabajadores()
            
        try:   
            for cliente in clientes:
                if cliente.getIDcliente() == mi_persona.getIDcliente() and cliente.getContrasenia() == mi_persona.getContrasenia():
                    print(f"Bienvenido cliente --> {cliente.getNombre()}")
                    return ('cliente',cliente.getNombre())

            for trab in trabajadores:
                if trab.getIDtrabajador() == mi_trabajador.getIDtrabajador() and trab.getContrasenia() == mi_trabajador.getContrasenia():
                    print(f"Bienvenido trabajador --> {trab.getNombre()}")
                    return (trab.getRol(),trab.getNombre())
            
            else:
                print("No existe ningun trabajador ni ningun cliente con esas credenciales")
                return 'invalido'
        except:    
            messagebox.showwarning("Advertencia", "Error al iniciar sesion")

    
    def validar_registro_concesionario(self, mi_concesionario: Concesionario, queHago):
        #if '@' in mi_persona.getEmail():
        
        if queHago == "aniadir":
            try:
                nombre = mi_concesionario.getNombre()
                direccion = mi_concesionario.getDireccion()
                ciudad = mi_concesionario.getCiudad()
                fecha_str = mi_concesionario.getFechaInauguracion()
                
                #Comprobando el formato del nombre
                if nombre[:10] == "Cofermotor":
                    print("Nombre correcto")
                elif nombre[:10] == "cofermotor":
                    print("Falta mayuscula en la inicial nombre. Corrigiendo")
                    nombre = "Cofermotor" + nombre[10:]
                    mi_concesionario.setNombre(nombre)
                else:
                    print("Formato incorrecto del nombre")
                    return ("Error", "Formato incorrecto del nombre")
                
                #comprobando el formato de la ciudad
                if ciudad[0].isupper() is True:
                    print("Ciudad con formato correcto")
                elif ciudad[0].isupper() is False:
                    c = ciudad[0].upper()
                    iudad = ciudad[1:]
                    ciudad = c + iudad
                    mi_concesionario.setCiudad(ciudad)
                else:
                    print("Formato incorrecto de la ciudad")
                    return ("Error", "Formato incorrecto de la ciudad")


                #paso la fecha al formato correcto
                fecha_obj = datetime.strptime(fecha_str, '%d-%m-%Y')
                fecha_mysql = fecha_obj.strftime('%Y-%m-%d')
                mi_concesionario.setFechaInauguracion(fecha_mysql)

                print(mi_concesionario)
                mi_concesionario_dao = ConcesionarioDao()
                mi_concesionario_dao.insertConcesionario(mi_concesionario)
                return ("Correcto", "Has introducido bien los datos")
            except:
                messagebox.showwarning("Advertencia", "Error al insertar el concesionario")

        elif queHago == "eliminar":
            try:
                nombre = mi_concesionario.getNombre()
                
                #Comprobando el formato del nombro
                mi_concesionario_dao = ConcesionarioDao()
                concesionarios = mi_concesionario_dao.getConcesionarios()

                for conc in concesionarios:
                    if conc.getNombre() == mi_concesionario.getNombre():
                        print(f"Eliminando concesionario --> {conc.getNombre()}")
                        mi_concesionario_dao.deleteConcesionario(mi_concesionario.getNombre())
                        return ("Correcto", "Has introducido bien los datos")
                    
                return ("Error", "Ese concesionario no existe")
            except:
                messagebox.showwarning("Advertencia", "Error al eliminar el concesionario")
        
        elif queHago == "modificar":
            try:
                nombre = mi_concesionario.getNombre()
                direccion = mi_concesionario.getDireccion()
                ciudad = mi_concesionario.getCiudad()
                fecha_str = mi_concesionario.getFechaInauguracion()

                fecha_obj = datetime.strptime(fecha_str, '%d-%m-%Y')
                fecha_mysql = fecha_obj.strftime('%Y-%m-%d')
                
                mi_concesionario_dao = ConcesionarioDao()
                concesionarios = mi_concesionario_dao.getConcesionarios()

                for conc in concesionarios:
                    if conc.getNombre() == nombre:
                        # Modificar los datos del concesionario
                        mi_concesionario.setDireccion(direccion)
                        mi_concesionario.setCiudad(ciudad)
                        mi_concesionario.setFechaInauguracion(fecha_mysql)
                        mi_concesionario_dao.updateConcesionario(mi_concesionario)
                        print(f"Modificado correctamente el concesionario --> {nombre}")
                        return ("Correcto", "Concesionario modificado correctamente")
            
                return ("Error", "El concesionario no existe")
            except:
                messagebox.showwarning("Advertencia", "Error al modificar el concesionario")

    def validar_registro_cliente(self, mi_persona: Cliente):
        if '@' in mi_persona.getEmail():
            mi_persona_dao = ClienteDao()
            mi_persona_dao.insertCliente(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")
    
    def obtener_todos_concesionarios(self):
        try:
            mi_concesionario_dao = ConcesionarioDao()
            concesionarios = mi_concesionario_dao.getConcesionarios()
            concesionarios_data = []
            for conc in concesionarios:
                concesionarios_data.append({
                    'nombre': conc.getNombre(),
                    'direccion': conc.getDireccion(),
                    'ciudad': conc.getCiudad(),
                    'fecha_inauguracion': conc.getFechaInauguracion()
                })
            return concesionarios_data
        except Exception as e:
            print(f"Error al obtener concesionarios: {e}")
            #return None

