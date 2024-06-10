# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:40:11 2024

@author: Dell XPS 9510
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re #funcion para comrpobar el formato de contrasenia
import bcrypt #funcion para encriptar contrasenia
import time

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

from src.modelo.vo.NotificacionesVO import NotificacionVO
from src.modelo.dao.NotificacionesDao import NotificacionDao


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


    def comprobarFormatoContrasenia(self, contrasenia):
        if len(contrasenia) < 8:
            return ("Error", "La longitud de la contraseña debe ser 8 o mas")
        if not re.search(r"[A-Z]", contrasenia):
            return ("Error", "Falta mayuscula en la contra")
        if not re.search(r"[a-z]", contrasenia):
            return ("Error",  "Falta minuscula en la contra")
        if not re.search(r"[0-9]", contrasenia):
            return ("Error", "La contra debe tener al menos un digito")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasenia):
            return ("Error", "Falta caracter especial en la contra")
        
        return ("Correcto", "Formato contraseña correcto")

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
    
    #FUNCION PARA MAYUSCULA LA PRIMERA LETRA
    def mayuscula(self, palabra):
        if palabra[0].isupper():
            print(f"{palabra} tiene el formato correcto")
            return palabra
        elif palabra[0].isupper() is False:
            print(f"Corrigiendo {palabra} ---> ", end="")
            palabra_corregida = palabra.capitalize()
            print(f"Corregida: {palabra_corregida}")
            return palabra_corregida
        else:
            return "Error"


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
                if cliente.getIDcliente() == mi_persona.getIDcliente() and self.verificar_contrasenia(mi_persona.getContrasenia(), cliente.getContrasenia()):
                    print(f"Bienvenido/a cliente --> {cliente.getNombre()}, {cliente.getConcesionario()}, {cliente.getIDcliente()}")
                    return ('cliente',cliente.getNombre(), cliente.getConcesionario(), cliente.getIDcliente())

            for trab in trabajadores:                
                if trab.getIDtrabajador() == mi_trabajador.getIDtrabajador() and self.verificar_contrasenia(mi_trabajador.getContrasenia(), trab.getContrasenia()):
                    print(f"Bienvenido/a trabajador/a --> {trab.getNombre()}")
                    return (trab.getRol(),trab.getNombre(), trab.getConcesionario())
            
            else:
                print("No existe ningun trabajador ni ningun cliente con esas credenciales")
                return ("Error",'invalido')
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
                
                
                #Comprobando el formato del nombre del concesionario
                conc = self.comprobarFormatoConcesionario(nombre)
                if conc[0] == "Error":
                    return conc
                elif conc[0] == "Corregido":
                    concesionario = conc[1]
                    mi_concesionario.setConcesionario(concesionario)
                else:
                    pass #Esto significa que es correcto el formato del nombre


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
##################################################################################################################################################


    #FUNCIONES PARA LA VENTANA TRABAJADOR
    def validar_registro_trabajador(self, mi_trabajador: PlantillaTrabajadorVO, queHago):
        if queHago == "aniadir" or queHago == "modificar":
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
                
                a = self.comprobarFormatoContrasenia(contrasenia)
                if a[0] == "Error":
                    return a
                

                try:
                    #Encripto la contrasenia
                    contrasenia2 = self.encriptar_contrasenia(contrasenia)
                    mi_trabajador.setContrasenia(contrasenia2)
                except:
                    return ("Error", "CONTACTA CON LOS PROGRAMADORES")

                #Mayusculas
                try:
                    mi_trabajador.setNombre(self.mayuscula(nombre))
                    mi_trabajador.setApellido1(self.mayuscula(apellido1))
                    mi_trabajador.setApellido2(self.mayuscula(apellido2))
                except:
                    return ("Error", "Verifica nombre y apellidos")

                
                #Compruebo el rol
                if rol not in ['administrador', 'jefeZona', 'personal', 'jefeVentas', 'jefeAlmacen', 'jefeTaller', 'jefeClientes']:
                    
                    print("El rol escrito no es posible en la empresa")
                    return ("Error", "El rol escrito no es posible en la empresa")
                
                if rol == "administrador":
                    mi_trabajador.setConcesionario("CofermotorTodos")

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

                if queHago == "aniadir":
                    mi_trabajador_dao.insertTrabajador(mi_trabajador)
                    return ("Correcto", "Has introducido bien los datos")
                
                elif queHago == "modificar":
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
                            return ("Correcto", "Trabajador modificado correctamente")
                
                    return ("Error", "El trabajador no esta registrado")

            except:
                messagebox.showwarning("Advertencia", "Error al insertar o modificar el trabajador")

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



##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################



    #FUNCIONES PARA LA VENTANA CLIENTES
    def validar_registro_cliente(self, mi_cliente: Cliente, queHago):
        def arroba(email):
            if '@' in email:
                print("@ en el mail. Correcto")
                return ("Correcto", "Email contiene @")
            else:
                return ("Error", "Falta el @ en el email")    
            

        if queHago == "aniadir":
            try:
                Idcliente = mi_cliente.getIDcliente()
                contrasenia = mi_cliente.getContrasenia()
                nombre = mi_cliente.getNombre()
                apellido1 = mi_cliente.getApellido1()
                apellido2 = mi_cliente.getApellido2()
                dirreccion = mi_cliente.getDireccion()
                email = mi_cliente.getEmail()
                concesionario = mi_cliente.getConcesionario()
                
                #Comprobando si el dni es correcto o no
                if self.funcionInsertarDNI(Idcliente) is False:
                    print("El IDcliente es incorrecto, compruebalo")
                    return ("Error", "El IDcliente es incorrecto")
                
                a = self.comprobarFormatoContrasenia(contrasenia)
                if a[0] == "Error":
                    return a

                try:
                    #Encripto la contrasenia
                    contrasenia2 = self.encriptar_contrasenia(contrasenia)
                    mi_cliente.setContrasenia(contrasenia2)
                except:
                    return ("Error", "CONTACTA CON LOS PROGRAMADORES")

                #Mayusculas
                try:
                    mi_cliente.setNombre(self.mayuscula(nombre))
                    mi_cliente.setApellido1(self.mayuscula(apellido1))
                    mi_cliente.setApellido2(self.mayuscula(apellido2))
                except:
                    return ("Error", "Verifica nombre y apellidos")


                #compruebo el @
                a = arroba(email)
                if a[0] == "Error":
                    return a
            
                #Comprobando el formato del nombre del concesionario
                conc = self.comprobarFormatoConcesionario(concesionario)
                if conc[0] == "Error":
                    return conc
                elif conc[0] == "Corregido":
                    concesionario = conc[1]
                    mi_cliente.setConcesionario(concesionario)
                else:
                    pass #Esto significa que es correcto el formato del nombre

                #compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if conc is False:
                    return ("Error", "El concesionario no existe")

                mi_cliente_dao = ClienteDao()
                mi_cliente_dao.insertCliente(mi_cliente)
                return ("Correcto", "Has introducido bien los datos")
            except:
                messagebox.showwarning("Advertencia", "Error al insertar el cliente")

        elif queHago == "eliminar":
            try:
                ID = mi_cliente.getIDcliente()
        
                mi_cliente_dao = ClienteDao()
                clientes = mi_cliente_dao.getClientes()

                for cli in clientes:
                    if cli.getIDcliente() == ID:
                        print(f"Eliminando cliente --> {cli.getIDcliente()}, {cli.getNombre()}")
                        mi_cliente_dao.deleteCliente(ID)
                        return ("Correcto", "Has introducido bien los datos")
                    
                return ("Error", "Ese cliente no esta registrado")
            except:
                messagebox.showwarning("Advertencia", "Error al eliminar el cliente")
        
        elif queHago == "modificar":
            try:
                Idcliente = mi_cliente.getIDcliente()
                contrasenia = mi_cliente.getContrasenia()
                nombre = mi_cliente.getNombre()
                apellido1 = mi_cliente.getApellido1()
                apellido2 = mi_cliente.getApellido2()
                dirreccion = mi_cliente.getDireccion()
                email = mi_cliente.getEmail()
                concesionario = mi_cliente.getConcesionario()
                

                a = self.comprobarFormatoContrasenia(contrasenia)
                if a[0] == "Error":
                    return a

                try:
                #Encripto la contrasenia
                     # Encripto la contrasenia solo si ha cambiado
                    contrasenia = self.encriptar_contrasenia(contrasenia)
                    mi_cliente.setContrasenia(contrasenia)
                except:
                    return ("Error", "CONTACTA CON LOS PROGRAMADORES")


                #Mayusculas
                try:
                    mi_cliente.setNombre(self.mayuscula(nombre))
                    mi_cliente.setApellido1(self.mayuscula(apellido1))
                    mi_cliente.setApellido2(self.mayuscula(apellido2))
                except:
                    return ("Error", "Verifica nombre y apellidos")

                #compruebo el @
                a = arroba(email)
                if a[0] == "Error":
                    return a

                #Comprobando el formato del nombre del concesionario
                conc = self.comprobarFormatoConcesionario(concesionario)
                if conc[0] == "Error":
                    return conc
                elif conc[0] == "Corregido":
                    concesionario = conc[1]
                    mi_cliente.setConcesionario(concesionario)
                else:
                    pass #Esto significa que es correcto el formato del nombre

                #compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if conc is False:
                    return ("Error", "El concesionario no existe")


                mi_cliente_dao = ClienteDao()
                clientes = mi_cliente_dao.getClientes()

                for cli in clientes:
                    if cli.getIDcliente() == Idcliente:
                        cli.setContrasenia(mi_cliente.getContrasenia())
                        cli.setNombre(mi_cliente.getNombre())
                        cli.setApellido1(mi_cliente.getApellido1())
                        cli.setApellido2(mi_cliente.getApellido2())
                        cli.setDireccion(mi_cliente.getDireccion())
                        cli.setEmail(mi_cliente.getEmail())
                        cli.setConcesionario(mi_cliente.getConcesionario())
                        mi_cliente_dao.updateCliente(cli)
                        print(f"Modificado correctamente el trabajador --> {Idcliente}, {nombre}")
                        return ("Correcto", "Cliente modificado correctamente")
            
                return ("Error", "El cliente no esta registrado")
            except:
                messagebox.showwarning("Advertencia", "Error al modificar el cliente")
    
    def obtener_todos_clientes(self):
        try:
            mi_cliente_dao = ClienteDao()
            clientes = mi_cliente_dao.getClientes()
            clientes_data = []
            for cli in clientes:
                clientes_data.append({
                    "IDcliente": cli.getIDcliente(),
                    "Contrasenia": cli.getContrasenia(),
                    'Nombre': cli.getNombre(),
                    'Apellido1': cli.getApellido1(),
                    'Apellido2': cli.getApellido2(),
                    'Direccion': cli.getDireccion(),
                    'Email': cli.getEmail(),
                    'Concesionario': cli.getConcesionario()
                })
            return clientes_data
        except:
            messagebox.showwarning("Advertencia", "Error al buscar clientes")


##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################



    #FUNCIONES PARA LA VENTANA VEHICULOS
    def validar_registro_vehiculos(self, mi_vehiculo: Vehiculo, queHago):
        #comprobar combustible
        def comprobarCombustible(combus):
            #print(combus)
            if combus not in ['gasolina', 'electrico', 'diesel', 'hibrido']:
                #print("h")
                return ("Error", "El combustible no es posible")
            else:
                print("Combustible correcto")
                return ("Correcto", "Combustible correcto")
            
        def comprobarKilometros(km):
            km = int(km)
            if km < 0 or km > 2000000:
                return ("Error", "O Km negativos o demasiados Km")
            else:
                print("Kms en rango correcto")
                return ("Correcto", "Kms en rango correcto")

        mi_vehiculo_dao = VehiculoDao()

        if queHago == "aniadir" or queHago == "modificar":
            try:
                IDvehiculo = mi_vehiculo.getIDvehiculo()
                marca = mi_vehiculo.getMarca()
                modelo = mi_vehiculo.getModelo()
                anio = mi_vehiculo.getAnio()
                combustible = mi_vehiculo.getCombustible()
                kilometros = mi_vehiculo.getKilometros()
                precio = mi_vehiculo.getPrecio()
                concesionario = mi_vehiculo.getConcesionario()
                
                if not IDvehiculo:
                    return ("Error", "Falta el ID")
                elif int(IDvehiculo) <= 0:
                    return ("Error", "IDvehiculo menor a 0")

            
                #Mayusculas
                try:
                    mi_vehiculo.setMarca(self.mayuscula(marca))
                    mi_vehiculo.setModelo(self.mayuscula(modelo))
                    
                except:
                    return ("Error", "Verifica marca y modelo")

                a = comprobarCombustible(combustible)
                if a[0] == "Error":
                    return a
                
                a = comprobarKilometros(kilometros)
                if a[0] == "Error":
                    return a

                #pasamos a int los necesarios


                #Comprobando el formato del nombre del concesionario
                conc = self.comprobarFormatoConcesionario(concesionario)
                if conc[0] == "Error":
                    return conc
                elif conc[0] == "Corregido":
                    concesionario = conc[1]
                    mi_vehiculo.setConcesionario(concesionario)
                else:
                    pass #Esto significa que es correcto el formato del nombre

                #compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if conc is False:
                    return ("Error", "El concesionario no existe")
                
                #####################################################################################
                if queHago == "aniadir":
                    mi_vehiculo_dao.insertVehiculo(mi_vehiculo)
                    return ("Correcto", "Has introducido bien los datos")
                
                #####################################################################################
                elif queHago == "modificar":
                    vehiculos = mi_vehiculo_dao.getVehiculos()

                    for veh in vehiculos:
                        if veh.getIDvehiculo() == IDvehiculo:
                            veh.setMarca(mi_vehiculo.getMarca())
                            veh.setModelo(mi_vehiculo.getModelo())
                            veh.setAnio(mi_vehiculo.getAnio())
                            veh.setCombustible(mi_vehiculo.getCombustible())
                            veh.setPrecio(mi_vehiculo.getPrecio())
                            veh.setKilometros(mi_vehiculo.getKilometros())
                            veh.setConcesionario(mi_vehiculo.getConcesionario())
                            mi_vehiculo_dao.modificarVehiculo(veh)
                            print(f"Modificado correctamente el vehiculo --> {IDvehiculo}, {marca}, {modelo}")
                            return ("Correcto", "Vehiculo modificado correctamente")
                
                    return ("Error", "El vehiculo no esta registrado")

            except:
                messagebox.showwarning("Advertencia", "Error al insertar o modificar el vehiculo")
                return ("Error", "Error al insertar o modificar el vehiculo")

        elif queHago == "eliminar":
            try:
                ID = mi_vehiculo.getIDvehiculo()
                vehiculos = mi_vehiculo_dao.getVehiculos()

                for veh in vehiculos:
                    if veh.getIDvehiculo() == ID:
                        print(f"Eliminando vehiculo --> {veh.getIDvehiculo()}, {veh.getMarca(), {veh.getModelo()}}")
                        mi_vehiculo_dao.deteteVehiculo(ID)
                        return ("Correcto", "Has introducido bien los datos")
                    
                return ("Error", "Ese vehiculo no esta registrado")
            except:
                messagebox.showwarning("Advertencia", "Error al eliminar el vehiculo")
                return ("Error", "Error al insertar o modificar el vehiculo")
    
    def obtener_todos_vehiculos(self):
        try:
            mi_vehiculo_dao = VehiculoDao()
            vehiculos = mi_vehiculo_dao.getVehiculos()
            
            vehiculos_data = []
            for veh in vehiculos:
                vehiculos_data.append({
                    "IDvehiculo": veh.getIDvehiculo(),
                    "Marca": veh.getMarca(),
                    'Modelo': veh.getModelo(),
                    'Año': veh.getAnio(),
                    'Combustible': veh.getCombustible(),
                    'Kilometros': veh.getKilometros(),
                    'Precio': veh.getPrecio(),
                    'Concesionario': veh.getConcesionario()
                })
            return vehiculos_data
        except:
            messagebox.showwarning("Advertencia", "Error al buscar vehiculos")




##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################



    #FUNCIONES PARA LA VENTANA VENTAS
    def validar_registro_ventas(self, mi_venta: Venta, queHago, quienSoy=None):
        
        mi_vehiculo_dao = VehiculoDao()
        mis_vehiculos = Vehiculo()
        vehiculos = mi_vehiculo_dao.getVehiculos()
        mi_venta_dao = VentaDao()
        mi_notifacion_dao = NotificacionDao()
        mi_notificacion = NotificacionVO()
        notifiaciones = mi_notifacion_dao.getNotificaciones()
        mis_clientes = Cliente()
        mis_clientes_dao = ClienteDao()
        clientes = mis_clientes_dao.getClientes()
        mis_piezas_dao = AlmacenDao()        
        mis_piezas = AlmacenVO()
        piezas1 = mis_piezas_dao.getAlmacenes()

        def comprobarPieza(Pieza, cantidad ,concesionario):
            for a in piezas1:
                if a.getPieza() == Pieza and a.getConcesionario() == concesionario:#compruebo que la pieza este en el concesionario indicado
                    if int(a.getCantidad()) < int(cantidad):#si la cantidad del almacen es menor => error 
                        return ("Error", "No hay suficientes piezas")
                    else:#si no, hay piezas suficientes, hacemos la resta
                        mis_piezas.setPieza(a.getPieza())
                        mis_piezas.setCantidad(int(a.getCantidad()) - int(cantidad))#la resta
                        mis_piezas.setPrecioPieza(a.getPrecioPieza())
                        mis_piezas.setConcesionario(a.getConcesionario())
                        mis_piezas_dao.updateAlmacen(mis_piezas) #actualizo la informacion en la base de datos
                        return ("Correcto", "Se ha hecho correctamente la resta de las piezas")
            return ("Error", "La pieza no esta registrada en el almacen")

        def comprobarVehiculo(idvehiculo):
            for a in vehiculos:
                if a.getIDvehiculo() == idvehiculo:
                    return ("Correcto", "Esta en la base de datos")
            return ("Error", "El vehiculo no esta registrado")
        
        def comprobarClientes(IDcliente):
            for a in clientes:
                if a.getIDcliente() == IDcliente:
                    return ("Correcto", "Esta en la base de datos")
            return ("Error", "El cliente no esta registrado")
        

        if queHago == "aniadir" or queHago == "modificar":
            try:
                IDventa = mi_venta.getIDventa()
                IDvehiculo = mi_venta.getIDvehiculo()
                repara = mi_venta.getRepara()
                IDcliente = mi_venta.getIDcliente()
                piezas = mi_venta.getPiezas()
                cantidad = mi_venta.getCantidad()
                fecha = mi_venta.getFechaVenta()
                concesionario = mi_venta.getConcesionario()
                
                #ESTO ES PARA QUE NO DE ERROR CON EL TEXTO "SE ASIGNA AUTOMATICAMENTE"
                

                if not IDvehiculo:
                    return ("Error", "Falta el id del vehiculo")
                elif IDvehiculo == "Reparado":
                    pass
                elif IDvehiculo != "0":
                    c = comprobarVehiculo(IDvehiculo)
                    if c[0] == "Error":
                        return c
                elif IDvehiculo == "0":
                    pass #se repara
                    
                # Paso la fecha al formato correcto
                fecha_obj = datetime.strptime(fecha, '%d-%m-%Y')
                fecha_mysql = fecha_obj.strftime('%Y-%m-%d')
                mi_venta.setFechaVenta(fecha_mysql)

                #compruebo que el cliente este
                c = comprobarClientes(IDcliente)
                if c[0] == "Error":
                    return c

               
                # Compruebo números negativos
                if cantidad and int(cantidad) < 0:
                    return ("Error", "Cantidad menor a 0")

                # Mayúsculas
                if repara:
                    repara = self.mayuscula(repara)
                    if repara == "Error":
                        return ("Error", "Error en repara")
                    elif repara not in ["Si", "No"]:
                        return ("Error", "Repara solo es 'Si' o 'No'")
                    elif repara == "No" and not IDvehiculo:
                        return ("Error", "Estas comprando un vehiculo?")
                    elif repara == "Si" and (not piezas or not cantidad or IDvehiculo not in ["0", "Reparado"]):
                        return ("Error", "Estas reparando un vehiculo")
                    mi_venta.setRepara(repara)

                # Comprobando el formato del nombre del concesionario
                if concesionario:
                    conc = self.comprobarFormatoConcesionario(concesionario)
                    if conc[0] == "Error":
                        return conc
                    elif conc[0] == "Corregido":
                        concesionario = conc[1]
                        mi_venta.setConcesionario(concesionario)

                # Compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if not conc:
                    return ("Error", "El concesionario no existe")
                    

                #Comprobar si hay suficientes piezas y si no, retornar un error antes de hacer ninguna venta
                if piezas:
                    c = comprobarPieza(piezas, cantidad, concesionario)
                    if c[0] == "Error":
                        return c


                ##########################################################################################
                if queHago == "aniadir":
                    IDventa = ""
                    mi_venta.setIDventa("")
                    

                    mi_venta_dao.insertVenta(mi_venta)
                    

                    mis_ventas = mi_venta_dao.getVentas()
                    #GENERA AUTOMATICAMENTE EL PAGO
                    
                    for i in mis_ventas:
                        if i.getIDvehiculo() == IDvehiculo: #la venta se ha generado por la tanto debe existir
                            mi_venta.setIDventa(i.getIDventa())
                            mi_venta.setConcesionario(i.getConcesionario())
                            break
                    
                        
                    pago = Pago(
                        IDpago="",
                        Precio="",
                        IDventa=mi_venta.getIDventa(),
                        Concesionario=mi_venta.getConcesionario()
                    )
                    self.validar_registro_pagos(pago, "aniadir")
                    
                    #si el vehiculo esta en la base de datos y lo vendemos se modifica su id a vendido mas su numero de bastidor
                    if IDvehiculo != "0" and IDvehiculo != "Reparado": #vehiculo a la venta, no reparado
                        if quienSoy is not None and (quienSoy=="personal" or quienSoy=="jefeVentas"):
                        #PERSONAL VALIDA LA COMPRA SE MODIFICA EN NOTIFICACIONES
                            for i in notifiaciones:
                                if i.getID() == IDvehiculo:
                                    #print("Hola2")
                                    mi_notificacion.setID(i.getID())
                                    mi_notificacion.setIDcliente(i.getIDcliente())
                                    mi_notificacion.setTipo(i.getTipo())
                                    mi_notificacion.setConcesionario(i.getConcesionario())
                                    mi_notificacion.setEstado("Procesado")
                                    mi_notifacion_dao.updateNotificacion(mi_notificacion)


                        for a in vehiculos:
                            if IDvehiculo == a.getIDvehiculo():
                                mis_vehiculos.setIDvehiculo("Vendido " + a.getIDvehiculo())
                                mis_vehiculos.setMarca(a.getMarca())
                                mis_vehiculos.setModelo(a.getModelo())
                                mis_vehiculos.setAnio(a.getAnio())
                                mis_vehiculos.setCombustible(a.getCombustible())
                                mis_vehiculos.setPrecio(a.getPrecio())
                                mis_vehiculos.setKilometros(a.getKilometros())
                                mis_vehiculos.setConcesionario(a.getConcesionario())
                                mi_vehiculo_dao.deteteVehiculo(IDvehiculo)
                                mi_vehiculo_dao.insertVehiculo(mis_vehiculos)
                                print("Modificado correctamente el vehiculo")
                                return ("Correcto", "Modificado a vendido correctamente")
                        
                        
                        return ("Error", "Error al cambiar a vendido")
                    elif IDvehiculo == "0":
                        if quienSoy is not None and (quienSoy=="personal" or quienSoy=="jefeVentas"):
                            #PERSONAL VALIDA LA COMPRA SE MODIFICA EN NOTIFICACIONES
                            contador = 1
                            nom = "Vehiculo desconocido " + str(contador)
                            print("Hola1")
                            #esto es para que no me de errores
                            for i in notifiaciones:
                                if nom == i.getID():
                                    print("Hola2")
                                    contador += 1
                                    nom = "Vehiculo desconocido " + str(contador)

                            for i in notifiaciones:
                                if i.getID() == IDvehiculo:
                                    print("Hola3")
                                    #la borro primero porque quiero cambiar el id
                                    mi_notifacion_dao.deleteNotificacion(i.getID())

                                    mi_notificacion.setID(nom)
                                    mi_notificacion.setIDcliente(i.getIDcliente())
                                    mi_notificacion.setTipo(i.getTipo())
                                    mi_notificacion.setConcesionario(i.getConcesionario())
                                    mi_notificacion.setEstado("Procesado")
                                    mi_notifacion_dao.insertNotificacion(mi_notificacion)

                        #si se repara un vehiculo, su id inicial sera 0 pero hay que convertila en Reparado para que no de error
                        venta = Venta()
                        for ven in mis_ventas:
                            if ven.getIDventa() == int(mi_venta.getIDventa()):
                                venta.setIDventa(ven.getIDventa())
                                venta.setFechaVenta(ven.getFechaVenta())
                                venta.setIDvehiculo("Reparado")
                                venta.setRepara(ven.getRepara())
                                venta.setIDcliente(ven.getIDcliente())
                                venta.setPiezas(ven.getPiezas())
                                venta.setCantidad(ven.getCantidad())
                                venta.setConcesionario(ven.getConcesionario())
                                mi_venta_dao.updateVenta(venta)
                        

                    return ("Correcto", "Has introducido bien los datos")
                ##################################################################################################
                elif queHago == "modificar":
                    ventas = mi_venta_dao.getVentas()

                    for ven in ventas:
                        if int(ven.getIDventa()) == int(IDventa):
                            ven.setFechaVenta(mi_venta.getFechaVenta())
                            ven.setIDvehiculo(mi_venta.getIDvehiculo())
                            ven.setRepara(mi_venta.getRepara())
                            ven.setIDcliente(mi_venta.getIDcliente())
                            ven.setPiezas(mi_venta.getPiezas())
                            ven.setCantidad(mi_venta.getCantidad())
                            ven.setConcesionario(mi_venta.getConcesionario())
                            mi_venta_dao.updateVenta(ven)
                            print(f"Modificado correctamente la venta --> {IDventa}")
                            return ("Correcto", "Venta modificado correctamente")
                    
                    return ("Error", "La venta no está registrada")

            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al insertar o modificar una venta: {str(e)}")
                return ("Error", "Error al insertar o modificar una venta")
        ###########################################################################################################
        elif queHago == "eliminar":
            try:
                ID = mi_venta.getIDventa()
                ventas = mi_venta_dao.getVentas()

                for ven in ventas:
                    if ven.getIDventa() == int(ID):
                        print(f"Eliminando venta --> {ven.getIDventa()}")
                        mi_venta_dao.deleteVenta(ID)
                        return ("Correcto", "Has introducido bien los datos")
                    
                return ("Error", "Esa venta no está registrada")
            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al eliminar la venta: {str(e)}")
                return ("Error", "Error al eliminar la venta")

    def obtener_todas_ventas(self):
        try:
            mi_venta_dao = VentaDao()
            ventas = mi_venta_dao.getVentas()
            
            ventas_data = []
            for ven in ventas:
                ventas_data.append({
                    "IDventa": ven.getIDventa(),
                    "FechaVenta": ven.getFechaVenta(),
                    'IDvehiculo': ven.getIDvehiculo(),
                    'Repara': ven.getRepara(),
                    'IDcliente': ven.getIDcliente(),
                    'Piezas': ven.getPiezas(),
                    'Cantidad': ven.getCantidad(),
                    'Concesionario': ven.getConcesionario()
                })
            return ventas_data
        except Exception as e:
            messagebox.showwarning("Advertencia", f"Error al buscar ventas: {str(e)}")



##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################



    #FUNCIONES PARA LA VENTANA ALMACEN
    def validar_registro_piezas(self, mi_almacen: AlmacenVO, queHago):
        
        mi_almacen_dao = AlmacenDao()
        almacen = mi_almacen_dao.getAlmacenes()

        if queHago == "aniadir" or queHago == "modificar":
            try:
                pieza = mi_almacen.getPieza()
                cantidad = mi_almacen.getCantidad()
                precio_pieza = mi_almacen.getPrecioPieza()
                concesionario = mi_almacen.getConcesionario()
                

                # Compruebo números negativos
                if not cantidad:
                    return ("Error", "Falta la cantidad")
                elif int(cantidad) < 0:
                    return ("Error", "Cantidad menor a 0")
                
                if precio_pieza != "": #SIGNIFICA QUE VAS A ANIADIR PIEZAS YA EXISTENTES
                    if int(precio_pieza) < 0:
                        return ("Error", "Precio negativo")


                # Comprobando el formato del nombre del concesionario
                if concesionario:
                    conc = self.comprobarFormatoConcesionario(concesionario)
                    if conc[0] == "Error":
                        return conc
                    elif conc[0] == "Corregido":
                        concesionario = conc[1]
                        mi_almacen.setConcesionario(concesionario)
                else:
                    return ("Error", "Falta el concesionario")

                # Compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if not conc:
                    return ("Error", "El concesionario no existe")

                
                # Realizar la inserción o modificación de la venta según el caso
                if queHago == "aniadir":
                    #compruebo que si la pieza existe y si existe sumo la cantidad a la actual en el concesionario en especifico
                    for a in almacen:
                        if a.getPieza() == pieza and a.getConcesionario() == mi_almacen.getConcesionario():
                            numero = int(cantidad) + int(a.getCantidad())
                            a.setCantidad(numero)
                            a.setPrecioPieza(a.getPrecioPieza())
                            a.setConcesionario(mi_almacen.getConcesionario())
                            mi_almacen_dao.updateAlmacen(a)
                            return ("Correcto", "Has introducido bien los datos")
        
                    mi_almacen_dao.insertAlmacen(mi_almacen)
                    return ("Correcto", "Has introducido bien los datos")
                
                elif queHago == "modificar":
                    
                    encontrado = False
                    concesionario = mi_almacen.getConcesionario()
                    for a in almacen:
                        if a.getPieza() == pieza:
                            if concesionario == "":
                                a.setCantidad(mi_almacen.getCantidad())
                                a.setPrecioPieza(mi_almacen.getPrecioPieza())
                                a.setConcesionario(mi_almacen.getConcesionario())
                                mi_almacen_dao.updateAlmacen(a)
                                print(f"Modificado correctamente la pieza --> {pieza}")
                                encontrado = True
                            elif a.getConcesionario() == concesionario:
                                a.setCantidad(mi_almacen.getCantidad())
                                a.setPrecioPieza(mi_almacen.getPrecioPieza())
                                a.setConcesionario(mi_almacen.getConcesionario())
                                mi_almacen_dao.updateAlmacen(a)
                                print(f"Modificado correctamente la pieza --> {pieza}")
                                encontrado = True

                    if encontrado:
                        return ("Correcto", "La pieza se ha modificado correctamente")
                    else:
                        return ("Error", "La pieza no está registrada")

            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al insertar o modificar una pieza: {str(e)}")
                return ("Error", "Error al insertar o modificar una pieza")

        elif queHago == "eliminar":
            try:
                pieza = mi_almacen.getPieza()
                concesionario = mi_almacen.getConcesionario()
                almacen = mi_almacen_dao.getAlmacenes()
                encontrado = False

                for a in almacen:
                    if a.getPieza() == pieza:
                        if concesionario == "":
                            print(f"Eliminando pieza en todos los concesionarios --> {a.getPieza()}")
                            mi_almacen_dao.deleteAlmacen(pieza)
                            encontrado = True
                        elif a.getConcesionario() == concesionario:
                            print(f"Eliminando pieza en el concesionario {concesionario} --> {a.getPieza()}")
                            mi_almacen_dao.deleteAlmacen(pieza, concesionario)
                            encontrado = True

                if encontrado:
                    return ("Correcto", "La pieza se ha eliminado correctamente")
                else:
                    return ("Error", "Esa pieza no está registrada en el concesionario especificado")
            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al eliminar la pieza: {str(e)}")
                return ("Error", "Error al eliminar la pieza")

    def obtener_todas_piezas(self):
        try:
            mi_almacen_dao = AlmacenDao()
            almacen = mi_almacen_dao.getAlmacenes()
            
            almacen_data = []
            for a in almacen:
                almacen_data.append({
                    "Pieza": a.getPieza(),
                    "Cantidad": a.getCantidad(),
                    'Precio': a.getPrecioPieza(),
                    'Concesionario': a.getConcesionario()
                })
            return almacen_data
        except Exception as e:
            messagebox.showwarning("Advertencia", f"Error al buscar piezas: {str(e)}")





##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################



    #FUNCIONES PARA LA VENTANA PAGOS
    def validar_registro_pagos(self, mi_pago: Pago, queHago):
        
        mi_pago_dao = PagoDao()
        mi_venta_dao = VentaDao()
        mi_vehiculo_dao = VehiculoDao()
        mi_almacen_dao = AlmacenDao()
        ventas = mi_venta_dao.getVentas()
        venta = Venta()

        def precioCalculo(idventa):
            
            vehiculos = mi_vehiculo_dao.getVehiculos()
            piezas = mi_almacen_dao.getAlmacenes()
            
            idvehiculo = ""
            pieza = ""
            concesionario = ""
            cantidadPiezas = 0
            precioPieza = 0
            for i in ventas:
                if int(i.getIDventa()) == int(idventa):
                    if i.getRepara() == "No":
                        print("HolaA")
                        idvehiculo = i.getIDvehiculo()
                    
                    elif i.getRepara() == "Si":
                        pieza = i.getPiezas()
                        cantidadPiezas = int(i.getCantidad())
                        concesionario = i.getConcesionario()
                        idvehiculo = 0
            if idvehiculo != 0:
                for i in vehiculos:
                    if idvehiculo == i.getIDvehiculo():
                        return int(i.getPrecio())
                    
            elif pieza != "":
                for i in piezas:
                    if pieza == i.getPieza() and i.getConcesionario() == concesionario:
                        precioPieza = int(i.getPrecioPieza())
                return cantidadPiezas * precioPieza
            
            
            return "Error"

            

        if queHago == "aniadir" or queHago == "modificar":
            try:
                IDpago = mi_pago.getIDpago()
                precio = mi_pago.getPrecio()
                Idventa = mi_pago.getIDventa()
                concesionario = mi_pago.getConcesionario()
                
                IDpago = ""
                mi_pago.setIDpago(IDpago)
                
                #print("Hola0")
                # Compruebo números negativos
                if not Idventa:
                    return ("Error", "Falta el IDventa")
                elif int(Idventa) < 0:
                    return ("Error", "IDventa menor a 0")
                

                #print("Hola1")
                if not precio or precio=="Se calcula automaticamente" or precio=="":
                    precio = precioCalculo(Idventa)
                    #print(precio)
                    if precio == "Error":
                        return ("Error", "Error al calcular el precio")
                    else:
                        mi_pago.setPrecio(precio)

                #print("Hola2")
                # Comprobando el formato del nombre del concesionario
                if concesionario:
                    conc = self.comprobarFormatoConcesionario(concesionario)
                    if conc[0] == "Error":
                        return conc
                    elif conc[0] == "Corregido":
                        concesionario = conc[1]
                        mi_pago.setConcesionario(concesionario)
                else:
                    return ("Error", "Falta el concesionario")

                # Compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if not conc:
                    return ("Error", "El concesionario no existe")
                

                #si se repara un vehiculo, su id inicial sera 0 pero hay que convertila en Reparado para que no de error

                # Realizar la inserción o modificación de la venta según el caso
                if queHago == "aniadir":
                    #print("Hola4")
                    mi_pago_dao.insertPago(mi_pago)
            
                    return ("Correcto", "Has introducido bien los datos")
                
                elif queHago == "modificar":
                    pagos = mi_pago_dao.getPagos()

                    for a in pagos:
                        if a.getIDpago() == int(IDpago):
                            a.setPrecio(mi_pago.getPrecio())
                            a.setIDventa(mi_pago.getIDventa())
                            a.setConcesionario(mi_pago.getConcesionario())
                            mi_pago_dao.updatePago(a)
                            print(f"Modificado correctamente el pago --> {IDpago}")
                            return ("Correcto", "Pago modificado correctamente")
                    
                    return ("Error", "El pago no está registrado")

            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al insertar o modificar un pago: {str(e)}")
                return ("Error", "Error al insertar o modificar un pago")

        elif queHago == "eliminar":
            try:
                pago = mi_pago.getIDpago()
                pagos = mi_pago_dao.getPagos()

                for a in pagos:
                    if a.getIDpago() == int(pago):
                        print(f"Eliminando pago --> {a.getIDpago()}")
                        mi_pago_dao.deletePago(pago)
                        return ("Correcto", "Has introducido bien los datos")
                    
                return ("Error", "Ese pago no está registrado")
            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al eliminar el pago: {str(e)}")
                return ("Error", "Error al eliminar el pago")

    def obtener_todos_pagos(self):
        try:
            mi_pago_dao = PagoDao()
            pagos = mi_pago_dao.getPagos()
            
            pagos_data = []
            for a in pagos:
                pagos_data.append({
                    "IDpago": a.getIDpago(),
                    "Precio": a.getPrecio(),
                    'IDventa': a.getIDventa(),
                    'Concesionario': a.getConcesionario()
                })
            return pagos_data
        except Exception as e:
            messagebox.showwarning("Advertencia", f"Error al buscar pagos: {str(e)}")



##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################



    #FUNCIONES PARA LA VENTANA VENTAS
    def validar_registro_maquinaria(self, mi_taller: Taller, queHago):
        
        mi_taller_dao = TallerDao()
        taller = mi_taller_dao.getTalleres()

        if queHago == "aniadir" or queHago == "modificar":
            try:
                IDmaquinaria = mi_taller.getIDmaquinaria()
                cantidad = mi_taller.getCantidad()
                nombre = mi_taller.getMaquinaria()
                concesionario = mi_taller.getConcesionario()
                

                # Compruebo números negativos
                if not cantidad:
                    return ("Error", "Falta la cantidad")
                elif int(cantidad) < 0:
                    return ("Error", "Cantidad menor a 0")

                if not nombre:
                    return ("Error", "Falta el nombre")
                
                #Mayusculas
                try:
                    mi_taller.setMaquinaria(self.mayuscula(nombre))                    
                except:
                    return ("Error", "Verifica el nombre")

                # Comprobando el formato del nombre del concesionario
                if concesionario:
                    conc = self.comprobarFormatoConcesionario(concesionario)
                    if conc[0] == "Error":
                        return conc
                    elif conc[0] == "Corregido":
                        concesionario = conc[1]
                        mi_taller.setConcesionario(concesionario)
                else:
                    return ("Error", "Falta el concesionario")

                # Compruebo si existe el concesionario en la base de datos
                conc = self.comprobarExistenciaConcesionario(concesionario)
                if not conc:
                    return ("Error", "El concesionario no existe")

                # Realizar la inserción o modificación de la venta según el caso
                if queHago == "aniadir":
                    mi_taller_dao.insertTaller(mi_taller)
                    return ("Correcto", "Has introducido bien los datos")
                
                elif queHago == "modificar":
                    for a in taller:
                        if a.getIDmaquinaria() == int(IDmaquinaria):
                            a.setCantidad(mi_taller.getCantidad())
                            a.setMaquinaria(mi_taller.getMaquinaria())
                            a.setConcesionario(mi_taller.getConcesionario())
                            mi_taller_dao.updateTaller(a)
                            print(f"Modificado correctamente la maquina --> {mi_taller.getMaquinaria()}")
                            return ("Correcto", "Maquina modificada correctamente")
                    
                    return ("Error", "La maquina no está registrada")

            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al insertar o modificar una maquina: {str(e)}")
                return ("Error", "Error al insertar o modificar una maquina")

        elif queHago == "eliminar":
            try:
                ID = mi_taller.getIDmaquinaria() 
                taller = mi_taller_dao.getTalleres()

                for a in taller:
                    if a.getIDmaquinaria() == int(ID):
                        print(f"Eliminando maquina --> {ID}")
                        mi_taller_dao.deleteTaller(ID)
                        return ("Correcto", "Has introducido bien los datos")
                    
                return ("Error", "Esa maquina no está registrada")
            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al eliminar la maquina: {str(e)}")
                return ("Error", "Error al eliminar la maquina")

    def obtener_todas_maquinas(self):
        try:
            mi_taller_dao = TallerDao()
            taller = mi_taller_dao.getTalleres()
            
            taller_data = []
            for a in taller:
                taller_data.append({
                    "IDmaquinaria": a.getIDmaquinaria(),
                    "Maquinaria": a.getMaquinaria(),
                    "Cantidad": a.getCantidad(),
                    'Concesionario': a.getConcesionario()
                })
            return taller_data
        except Exception as e:
            messagebox.showwarning("Advertencia", f"Error al buscar maquinaria: {str(e)}")



##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################

    def comprarReparaVehiculoCliente(self, mi_vehiculo: Vehiculo, queHago, dondeEstoy, quienSoy=None):
        try:
            mi_notificacion = NotificacionVO()
            mi_notificacion_dao = NotificacionDao()
            notificaciones = mi_notificacion_dao.getNotificaciones()
            mi_vehiculo_dao = VehiculoDao()
            vehiculos = mi_vehiculo_dao.getVehiculos()
            
            for i in notificaciones:
                if mi_vehiculo.getIDvehiculo() == i.getID():
                    return ("Error", "Ya has solicitado una venta/reparacion")
            

            if queHago == "Comprar":
                encontrado = False  # Variable para rastrear si se encontró el vehículo
                for veh in vehiculos:
                    if mi_vehiculo.getIDvehiculo() == veh.getIDvehiculo():
                        print(f"Notificando al personal sobre tu compra --> {veh.getMarca()}, {veh.getModelo()}")
                        mi_notificacion.setID(veh.getIDvehiculo())
                        encontrado = True
                        break  # Salimos del bucle ya que hemos encontrado y procesado el vehículo

                if not encontrado:
                    return ("Error", "El ID introducido no es correcto")
            elif queHago == "Reparar":
                mi_notificacion.setID(0) 
            
            

            if quienSoy is not None:
                mi_notificacion.setIDcliente(quienSoy)

            if queHago == "Comprar":
                mi_notificacion.setTipo("Venta")
            elif queHago == "Reparar":
                mi_notificacion.setTipo("Reparacion")

            mi_notificacion.setEstado("En proceso")
            mi_notificacion.setConcesionario(dondeEstoy)
            mi_notificacion_dao.insertNotificacion(mi_notificacion)
            return ("Correcto", "Notificando al personal")
            
        except Exception as e:
            messagebox.showwarning("Advertencia", f"Error al buscar vehiculos ---> {e}")
            return ("Error", "Envio de notificacion fallido")
        

    def obtenerTodasNotificaciones(self):
        try:
            notificacionDao = NotificacionDao()
            notificaciones = notificacionDao.getNotificaciones()
            
            notificaciones_data = []
            for notificacion in notificaciones:
                notificaciones_data.append({
                    "IDnotificacion": notificacion.getID(),
                    "IDcliente": notificacion.getIDcliente(),
                    "Tipo": notificacion.getTipo(),
                    "Estado": notificacion.getEstado(),
                    'Concesionario': notificacion.getConcesionario()
                })
            return notificaciones_data
        except Exception as e:
            messagebox.showwarning("Advertencia", f"Error al buscar notificaciones: {str(e)}")
            return ("Error", "Error al buscar notificaciones")


    

