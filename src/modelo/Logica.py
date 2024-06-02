# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:40:11 2024

@author: Dell XPS 9510
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import bcrypt

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

    #DEVUELVE TRUE SI ES VALIDO, FALSE SI NO LO ES
    def funcionInsertarDNI(self, dni):
        if len(dni) != 9:
            return False
        if not dni[:8].isdigit() or not dni[-1].isalpha():
            return False
        
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = int(dni[:8])
        letra = dni[-1].upper()

        # Calcular la letra correcta
        letra_correcta = letras[numeros % 23]

        # Comparar la letra proporcionada con la letra calculada
        return letra == letra_correcta

    #ENCRIPTAR Y DEENCRIPTAR CONTRASENIA
    def encriptar_contrasenia(self, contrasenia) -> str:
        #print("Hola")
        salt = bcrypt.gensalt()
        # Hashea la contraseña con el salt
        hashed = bcrypt.hashpw(contrasenia.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verificar_contrasenia(self, contrasenia, hashed_contrasenia) -> bool:
        return bcrypt.checkpw(contrasenia.encode('utf-8'), hashed_contrasenia.encode('utf-8'))
    
    #COMPROBAR EL FORMATO DEL NOMBRE DEL CONCESIONARIO
    def comprobarFormatoConcesionario(self, concesionario):
        if concesionario[:10] == "Cofermotor":
            print("Nombre concesionario correcto")
            return ("Correcto", concesionario)
        elif concesionario[:10] == "cofermotor":
            print("Falta mayuscula en la inicial nombre del concesionario. Corrigiendo")
            concesionario = "Cofermotor" + concesionario[10:]
            return ("Corregido", concesionario)
        else:
            print("Formato incorrecto del nombre del concesionario")
            return ("Error", "Formato incorrecto del concesionario")
    
    #COMPROBAR SI EL CONCESIONARIO EXISTE EN LA BASE DE DATOS
    def comprobarExistenciaConcesionario(self, concesionario):
        tablaConcesionarios = ConcesionarioDao()
        concs = tablaConcesionarios.getConcesionarios()
        for conc in concs:
            if conc.getNombre() == concesionario:
                return True
        print("El concesionario no existe")
        return False


#################################################################################################################################################
#################################################################################################################################################


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
                    print(f"Bienvenido/a cliente --> {cliente.getNombre()}")
                    return ('cliente',cliente.getNombre())

            for trab in trabajadores:
                if trab.getIDtrabajador() == mi_trabajador.getIDtrabajador() and self.verificar_contrasenia(mi_trabajador.getContrasenia(), trab.getContrasenia()):
                    print(f"Bienvenido/a trabajador/a --> {trab.getNombre()}")
                    return (trab.getRol(),trab.getNombre())
            
            else:
                print("No existe ningun trabajador ni ningun cliente con esas credenciales")
                return 'invalido'
        except:    
            messagebox.showwarning("Advertencia", "Error al iniciar sesion")


#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

    #FUNCIONES PARA LA VENTANA CONCESIONARIO    
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

                #print(mi_concesionario)
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

                comprueba = self.comprobarExistenciaConcesionario(nombre)
                if comprueba:
                    print(f"Eliminando concesionario --> {nombre}")
                    mi_concesionario_dao.deleteConcesionario(nombre)
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

                conc = self.comprobarFormatoConcesionario(nombre)
                if conc[0] == "Error":
                    return conc
                elif conc[0] == "Corregido":
                    nombre = conc[1]
                else:
                    pass #Esto significa que es correcto el formato del nombre
                
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
            return None



##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################


    #FUNCIONES PARA LA VENTANA TRABAJADOR
    def validar_registro_trabajador(self, mi_trabajador: PlantillaTrabajadorVO, queHago):
        if queHago == "aniadir":
            try:
                IDtrabajador = mi_trabajador.getIDtrabajador()
                contrasenia = str(mi_trabajador.getContrasenia())
                nombre = mi_trabajador.getNombre()
                apellido1 = mi_trabajador.getApellido1()
                apellido2 = mi_trabajador.getApellido2()
                sueldo = mi_trabajador.getSueldo()
                rol = mi_trabajador.getRol()
                concesionario = mi_trabajador.getConcesionario()
                
                #Comprobando si el dni es correcto o no
                if self.funcionInsertarDNI(IDtrabajador) is False:
                    print("El IDtrabajador es incorrecto, compruebalo")
                    return ("Error", "El IDtrabajador es incorrecto")
                
                
                try:
                    #Encripto la contrasenia
                    contrasenia2 = self.encriptar_contrasenia(contrasenia)
                    mi_trabajador.setContrasenia(contrasenia2)
                except:
                    messagebox.showwarning("Advertencia", "Error en la libreria bcrypt o en sus funciones")

                #Compruebo el rol
                if rol not in ['administrador', 'jefeZona', 'jefeDepartamento', 'personal']:
                    print("El rol escrito no es posible en la empresa")
                    return ("Error", "El rol escrito no es posible en la empresa")

                #Comprobando el formato del nombre del concesionario
                conc = self.comprobarFormatoConcesionario(concesionario)
                if conc[0] == "Error":
                    return conc
                elif conc[0] == "Corregido":
                    concesionario = conc[1]
                    mi_trabajador.setConcesionario(concesionario)
                else:
                    pass #Esto significa que es correcto el formato del nombre

                #compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if conc is False:
                    return ("Error", "El concesionario no existe")

                mi_trabajador_dao = TrabajadorDao()
                mi_trabajador_dao.insertTrabajador(mi_trabajador)
                return ("Correcto", "Has introducido bien los datos")
            except:
                messagebox.showwarning("Advertencia", "Error al insertar el trabajador")

        elif queHago == "eliminar":
            try:
                ID = mi_trabajador.getIDtrabajador()
        
                mi_trabajador_dao = TrabajadorDao()
                trabajadores = mi_trabajador_dao.getTrabajadores()

                for trab in trabajadores:
                    if trab.getIDtrabajador() == ID:
                        print(f"Eliminando trabajador --> {trab.getIDtrabajador()}, {trab.getNombre()}")
                        mi_trabajador_dao.deleteTrabajador(ID)
                        return ("Correcto", "Has introducido bien los datos")
                    
                return ("Error", "Ese trabajador no esta registrado")
            except:
                messagebox.showwarning("Advertencia", "Error al eliminar el trabajador")
        
        elif queHago == "modificar":
            try:
                IDtrabajador = mi_trabajador.getIDtrabajador()
                contrasenia = mi_trabajador.getContrasenia()
                nombre = mi_trabajador.getNombre()
                apellido1 = mi_trabajador.getApellido1()
                apellido2 = mi_trabajador.getApellido2()
                sueldo = mi_trabajador.getSueldo()
                rol = mi_trabajador.getRol()
                concesionario = mi_trabajador.getConcesionario()
                
                try:
                #Encripto la contrasenia
                     # Encripto la contrasenia solo si ha cambiado
                    contrasenia = self.encriptar_contrasenia(contrasenia)
                    mi_trabajador.setContrasenia(contrasenia)
                except:
                    messagebox.showwarning("Advertencia", "Error en la libreria bcrypt o en sus funciones")

                #Compruebo el rol
                if rol not in ['administrador', 'jefeZona', 'jefeDepartamento', 'personal']:
                    print("El rol escrito no es posible en la empresa")
                    return ("Error", "El rol escrito no es posible en la empresa")

                #Comprobando el formato del nombre del concesionario
                conc = self.comprobarFormatoConcesionario(concesionario)
                if conc[0] == "Error":
                    return conc
                elif conc[0] == "Corregido":
                    concesionario = conc[1]
                    mi_trabajador.setConcesionario(concesionario)
                else:
                    pass #Esto significa que es correcto el formato del nombre

                #compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if conc is False:
                    return ("Error", "El concesionario no existe")


                mi_trabajador_dao = TrabajadorDao()
                trabajadores = mi_trabajador_dao.getTrabajadores()

                for trab in trabajadores:
                    if trab.getIDtrabajador() == IDtrabajador:
                        trab.setContrasenia(mi_trabajador.getContrasenia())
                        trab.setNombre(mi_trabajador.getNombre())
                        trab.setApellido1(mi_trabajador.getApellido1())
                        trab.setApellido2(mi_trabajador.getApellido2())
                        trab.setSueldo(mi_trabajador.getSueldo())
                        trab.setRol(mi_trabajador.getRol())
                        trab.setConcesionario(mi_trabajador.getConcesionario())
                        mi_trabajador_dao.updateTrabajador(trab)
                        mi_trabajador_dao.updateTrabajador(trab)
                        print(f"Modificado correctamente el trabajador --> {IDtrabajador}, {nombre}")
                        return ("Correcto", "Concesionario modificado correctamente")
            
                return ("Error", "El trabajador no esta registrado")
            except:
                messagebox.showwarning("Advertencia", "Error al modificar el trabajador")
    
    def obtener_todos_trabajadores(self):
        try:
            mi_trabajador_dao = TrabajadorDao()
            trabajadores = mi_trabajador_dao.getTrabajadores()
            trabajadores_data = []
            for trab in trabajadores:
                trabajadores_data.append({
                    "IDtrabajador": trab.getIDtrabajador(),
                    "Contrasenia": trab.getContrasenia(),
                    'Nombre': trab.getNombre(),
                    'Apellido1': trab.getApellido1(),
                    'Apellido2': trab.getApellido2(),
                    'Sueldo': str(trab.getSueldo()),
                    'Rol': trab.getRol(),
                    'Concesionario': trab.getConcesionario()
                })
            return trabajadores_data
        except Exception as e:
            print(f"Error al obtener trabajadores: {e}")



    #FUNCIONES PARA LA VENTANA CLIENTES
    def validar_registro_cliente(self, mi_persona: Cliente):
        if '@' in mi_persona.getEmail():
            mi_persona_dao = ClienteDao()
            mi_persona_dao.insertCliente(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")
    
    

