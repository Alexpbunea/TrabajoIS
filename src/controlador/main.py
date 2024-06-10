# En el cmd de Anaconda: pip install pyqt5
# Una vez isntalado en C:\Users\"user"\anaconda3\Library\bin executamos el designer.exe
# Para abrir un nuevo proyecto: Archivo -> Nuevo -> main Windows
# Arriba a la derecha borramos todo menos el central widget
# guardamos la ventana en la carpeta vista
import sys
ruta_modulo = "./"
sys.path.append(ruta_modulo)


#VENTANA PRINCIPAL
#from src.vista.Controlador import Controlador
from PyQt5 import QtWidgets
from borrarPycache import borrar_pycache
directorio_proyecto =r".\src"

from src.vista.VentanaPrincipal_ui import Ui_MainWindow
from src.vista.VentanaIniciarSesion_ui import Ui_MainWindow2
from src.vista.VentanaAdmin import Ui_MainWindow3
from src.vista.VentanaConcesionario import Ui_MainWindow4
from src.vista.VentanaTrabajadores import Ui_MainWindow5
from src.vista.VentanaClientes import Ui_MainWindow6
from src.vista.VentanaVehiculos import Ui_MainWindow7
from src.vista.VentanaVentas import Ui_MainWindow8
from src.vista.VentanaAlmacen import Ui_MainWindow9
from src.vista.VentanaParaClientes import Ui_MainWindowClientes
from src.vista.VentanaTaller import Ui_MainWindow10
from src.vista.VentanaPago import Ui_MainWindow11
from src.vista.VentanaJefeZona import Ui_MainWindow_JefeZona
from src.vista.VentanaPersonal import Ui_MainWindow_Personal
from src.vista.funciones import *

import Imagespy.imagen_rc
import Imagespy.imagenDes_rc
import Imagespy.nissan2
import Imagespy.nissanGtrClaro
import Imagespy.botonAtrasBlanco
import Imagespy.botonAtrasBlancoAzul

#RESTO
from src.controlador.Coordinador import Coordinador
from src.modelo.Logica import Logica




def mostrar_ventana(ventanaInicial, ventanaFinal):
    ventanaInicial.hide()
    ventanaFinal.show()

def atras2(ventanaInicial, ventanaFinal):
    ventanaInicial.hide()
    ventanaFinal.show()

def resetear_campos_inicio_sesion():
    ui_ventana2_ui.LineaDni.setText("")
    ui_ventana2_ui.LineaContra.setText("")
    
def funcionA(ventana, ventana2, boton, boton2):
    if ventana2.c.text() != "":
            ventana.LineaConc.setReadOnly(True)
            boton = getattr(ventana, boton)
            boton2 = getattr(ventana, boton2)
            boton.clicked.connect(lambda: ventana.LineaConc.setText(ventana2.c.text()))
            boton2.clicked.connect(lambda: ventana.LineaConc.setText(ventana2.c.text()))

def comprobarSesion():
    #"""
    #comprobar si el dni y la contrasenia son correctos
    a = ui_ventana2_ui.obtener_datos_ingresados()

    if a is False:
        ui_ventana2_ui.hacerVisible(True)

    elif a[0] == "cliente":
        ui_ventana2_ui.hacerVisible(False)
        mostrar_ventana(ventanaIniciarSesion, ventanaParaClientes)
        ui_ventana_Clientes.hola_2.setText(a[1])
        ui_ventana_Clientes.concesionario.setText(a[2])
        ui_ventana_Clientes.BuscarVeh.clicked.connect(lambda: ui_ventana_Clientes.mostrarVehiculos(a[2]))
        ui_ventana_Clientes.atras.clicked.connect(lambda: atras2(ventanaParaClientes, ventanaIniciarSesion))
        ui_ventana_Clientes.botonComprarVeh.clicked.connect(lambda: ui_ventana_Clientes.obtener_datos_ingresados(a[2], a[3]))
        ui_ventana_Clientes.botonReparar.clicked.connect(lambda: ui_ventana_Clientes.obtener_datos_ingresados(a[2], a[3]))
        
        
        

    elif a[0] in ['administrador', 'jefeZona', 'personal', 'jefeVentas', 'jefeAlmacen', 'jefeTaller', 'jefeClientes']:
        ui_ventana2_ui.hacerVisible(False)
        if a[0] == "administrador":
            ui_ventana2_ui.hacerVisible(False)
            mostrar_ventana(ventanaIniciarSesion, ventanaAdmin)
            ui_ventana3_ui.hola_2.setText(a[1])
            ui_ventana3_ui.c.setText(a[2])
            ui_ventana3_ui.atras.clicked.connect(lambda: atras2(ventanaAdmin, ventanaIniciarSesion))
            ui_ventana3_ui.Concesionario.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaConcesionario))
            
            ui_ventana4_ui.atras.clicked.connect(lambda: atras2(ventanaConcesionario, ventanaAdmin))
            ui_ventana4_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana4_ui.obtener_datos_ingresados())
            ui_ventana4_ui.botonEliminar.clicked.connect(lambda: ui_ventana4_ui.obtener_datos_ingresados())
            ui_ventana4_ui.BuscarCon.clicked.connect(lambda: ui_ventana4_ui.mostrasConcesionarios())

            ui_ventana3_ui.Trabajador.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaTrabajadores))
            ui_ventana5_ui.atras.clicked.connect(lambda: atras2(ventanaTrabajadores, ventanaAdmin))
            ui_ventana5_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana5_ui.obtener_datos_ingresados())
            ui_ventana5_ui.botonEliminar.clicked.connect(lambda:ui_ventana5_ui.obtener_datos_ingresados())
            ui_ventana5_ui.BuscarTra.clicked.connect(lambda: ui_ventana5_ui.mostrarTrabajadores())

            ui_ventana3_ui.Cliente.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaClientes))
            ui_ventana6_ui.atras.clicked.connect(lambda: atras2(ventanaClientes, ventanaAdmin))
            ui_ventana6_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana6_ui.obtener_datos_ingresados())
            ui_ventana6_ui.botonEliminar.clicked.connect(lambda: ui_ventana6_ui.obtener_datos_ingresados())
            ui_ventana6_ui.BuscarCli.clicked.connect(lambda: ui_ventana6_ui.mostrarClientes())

            ui_ventana3_ui.vehiculos.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaVehiculos))
            ui_ventana7_ui.atras.clicked.connect(lambda: atras2(ventanaVehiculos, ventanaAdmin))
            ui_ventana7_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana7_ui.obtener_datos_ingresados())
            ui_ventana7_ui.botonEliminar.clicked.connect(lambda: ui_ventana7_ui.obtener_datos_ingresados())
            ui_ventana7_ui.BuscarVeh.clicked.connect(lambda: ui_ventana7_ui.mostrarVehiculos())

            ui_ventana3_ui.ventas.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaVentas))
            ui_ventana8_ui.atras.clicked.connect(lambda: atras2(ventanaVentas, ventanaAdmin))
            ui_ventana8_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana8_ui.obtener_datos_ingresados())
            ui_ventana8_ui.botonEliminar.clicked.connect(lambda: ui_ventana8_ui.obtener_datos_ingresados())
            ui_ventana8_ui.BuscarVen.clicked.connect(lambda:ui_ventana8_ui.mostrarVentas())

            ui_ventana3_ui.Almacen.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaAlmacen))
            ui_ventana9_ui.atras.clicked.connect(lambda: atras2(ventanaAlmacen, ventanaAdmin))
            ui_ventana9_ui.botonAniadirModificar.clicked.connect(lambda:ui_ventana9_ui.obtener_datos_ingresados())
            ui_ventana9_ui.botonEliminar.clicked.connect(lambda:ui_ventana9_ui.obtener_datos_ingresados())
            ui_ventana9_ui.BuscarPieza.clicked.connect(lambda:ui_ventana9_ui.mostrarAlmacenes())

            ui_ventana3_ui.Taller.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaTaller))
            ui_ventana10_ui.atras.clicked.connect(lambda: atras2(ventanaTaller, ventanaAdmin))
            ui_ventana10_ui.botonAniadirModificar.clicked.connect(lambda:ui_ventana10_ui.obtener_datos_ingresados())
            ui_ventana10_ui.botonEliminar.clicked.connect(lambda:ui_ventana10_ui.obtener_datos_ingresados())
            ui_ventana10_ui.BuscarMaquinaria.clicked.connect(lambda:ui_ventana10_ui.mostrarTaller())

            ui_ventana3_ui.pago.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaPagos))
            ui_ventana11_ui.atras.clicked.connect(lambda: atras2(ventanaPagos, ventanaAdmin))
            ui_ventana11_ui.botonAniadirModificar.clicked.connect(lambda:ui_ventana11_ui.obtener_datos_ingresados())
            ui_ventana11_ui.botonEliminar.clicked.connect(lambda:ui_ventana11_ui.obtener_datos_ingresados())
            ui_ventana11_ui.BuscarPago.clicked.connect(lambda: ui_ventana11_ui.mostrarPagos())

        elif a[0] == "jefeZona":
            ui_ventana2_ui.hacerVisible(False)
            mostrar_ventana(ventanaIniciarSesion, ventanaJefeZona)
            ui_ventana_jefeZona.hola_2.setText(a[1])
            ui_ventana_jefeZona.c.setText(a[2])
            ui_ventana_jefeZona.atras.clicked.connect(lambda: atras2(ventanaJefeZona, ventanaIniciarSesion))

            ui_ventana_jefeZona.Trabajador.clicked.connect(lambda: mostrar_ventana(ventanaJefeZona, ventanaTrabajadores))
            funcionA(ui_ventana5_ui, ui_ventana_jefeZona, 'aniadirTra', 'ModificarTra')
            ui_ventana5_ui.atras.clicked.connect(lambda: atras2(ventanaTrabajadores, ventanaJefeZona))
            ui_ventana5_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana5_ui.obtener_datos_ingresados(a[2]))
            ui_ventana5_ui.botonEliminar.clicked.connect(lambda: ui_ventana5_ui.obtener_datos_ingresados(a(2)))
            ui_ventana5_ui.BuscarTra.clicked.connect(lambda: ui_ventana5_ui.mostrarTrabajadores(a[2]))

            ui_ventana_jefeZona.Cliente.clicked.connect(lambda: mostrar_ventana(ventanaJefeZona, ventanaClientes))
            funcionA(ui_ventana6_ui, ui_ventana_jefeZona, 'aniadirCli', 'ModificarCli')
            ui_ventana6_ui.atras.clicked.connect(lambda: atras2(ventanaClientes, ventanaJefeZona))
            ui_ventana6_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana6_ui.obtener_datos_ingresados(a[2]))
            ui_ventana6_ui.botonEliminar.clicked.connect(lambda: ui_ventana6_ui.obtener_datos_ingresados(a[2]))
            ui_ventana6_ui.BuscarCli.clicked.connect(lambda:ui_ventana6_ui.mostrarClientes(a[2]))

            ui_ventana_jefeZona.vehiculos.clicked.connect(lambda: mostrar_ventana(ventanaJefeZona, ventanaVehiculos))
            funcionA(ui_ventana7_ui, ui_ventana_jefeZona, 'aniadirVeh', 'ModificarVeh')
            ui_ventana7_ui.atras.clicked.connect(lambda: atras2(ventanaVehiculos, ventanaJefeZona))
            ui_ventana7_ui.botonAniadirModificar.clicked.connect(lambda:ui_ventana7_ui.obtener_datos_ingresados(a[2]))
            ui_ventana7_ui.botonEliminar.clicked.connect(lambda:ui_ventana7_ui.obtener_datos_ingresados(a[2]))
            ui_ventana7_ui.BuscarVeh.clicked.connect(lambda:ui_ventana7_ui.mostrarVehiculos(a[2]))

            ui_ventana_jefeZona.ventas.clicked.connect(lambda: mostrar_ventana(ventanaJefeZona, ventanaVentas))
            funcionA(ui_ventana8_ui, ui_ventana_jefeZona, 'aniadirVen', 'ModificarVen')
            ui_ventana8_ui.atras.clicked.connect(lambda: atras2(ventanaVentas, ventanaJefeZona))
            ui_ventana8_ui.botonAniadirModificar.clicked.connect(lambda:ui_ventana8_ui.obtener_datos_ingresados(a[2]))
            ui_ventana8_ui.botonEliminar.clicked.connect(lambda:ui_ventana8_ui.obtener_datos_ingresados(a[2]))
            ui_ventana8_ui.BuscarVen.clicked.connect(lambda:ui_ventana8_ui.mostrarVentas(a[2]))

        
            ui_ventana_jefeZona.Taller.clicked.connect(lambda: mostrar_ventana(ventanaJefeZona, ventanaTaller))
            funcionA(ui_ventana10_ui, ui_ventana_jefeZona, 'aniadirMaquinaria', 'ModificarMaquinaria')
            ui_ventana10_ui.atras.clicked.connect(lambda: atras2(ventanaTaller, ventanaJefeZona))
            ui_ventana10_ui.botonAniadirModificar.clicked.connect(lambda:ui_ventana10_ui.obtener_datos_ingresados(a[2]))
            ui_ventana10_ui.botonEliminar.clicked.connect(lambda:ui_ventana10_ui.obtener_datos_ingresados(a[2]))
            ui_ventana10_ui.BuscarMaquinaria.clicked.connect(lambda:ui_ventana10_ui.mostrarTaller(a[2]))

            ui_ventana_jefeZona.pago.clicked.connect(lambda: mostrar_ventana(ventanaJefeZona, ventanaPagos))
            funcionA(ui_ventana11_ui, ui_ventana_jefeZona, 'aniadirPago', 'ModificarPago')
            ui_ventana11_ui.atras.clicked.connect(lambda: atras2(ventanaPagos, ventanaJefeZona))
            ui_ventana11_ui.botonAniadirModificar.clicked.connect(lambda:ui_ventana11_ui.obtener_datos_ingresados(a[2]))
            ui_ventana11_ui.botonEliminar.clicked.connect(lambda:ui_ventana11_ui.obtener_datos_ingresados(a[2]))
            ui_ventana11_ui.BuscarPago.clicked.connect(lambda:ui_ventana11_ui.mostrarPagos(a[2]))

        elif a[0] == "jefeVentas":
            mostrar_ventana(ventanaIniciarSesion, ventanaVentas)
            #funcionA(ui_ventana6_ui, ui_ventana_jefeZona, 'aniadirCli', 'ModificarCli')
            ui_ventana8_ui.hola.setText("Hola de nuevo")
            ui_ventana8_ui.hola_2.setText(a[1])
            ui_ventana8_ui.c.setText(a[2])
            ui_ventana8_ui.LineaConc.setText(a[2])
            ui_ventana8_ui.LineaConc.setReadOnly(True)
            ui_ventana8_ui.atras.clicked.connect(lambda: atras2(ventanaVentas, ventanaIniciarSesion))
            ui_ventana8_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana8_ui.obtener_datos_ingresados(a[2]))
            ui_ventana8_ui.botonEliminar.clicked.connect(lambda: ui_ventana8_ui.obtener_datos_ingresados(a[2]))
            ui_ventana8_ui.BuscarVen.clicked.connect(lambda:ui_ventana8_ui.mostrarVentas(a[2]))

        elif a[0] == "jefeAlmacen":
            mostrar_ventana(ventanaIniciarSesion, ventanaAlmacen)
            #funcionA(ui_ventana6_ui, ui_ventana_jefeZona, 'aniadirCli', 'ModificarCli')
            ui_ventana9_ui.hola.setText("Hola de nuevo")
            ui_ventana9_ui.hola_2.setText(a[1])
            ui_ventana9_ui.c.setText(a[2])
            ui_ventana9_ui.LineaConc.setText(a[2])
            ui_ventana9_ui.LineaConc.setReadOnly(True)
            ui_ventana9_ui.Lineaconcesionario2.setText(a[2])
            ui_ventana9_ui.Lineaconcesionario2.setReadOnly(True)
            ui_ventana9_ui.atras.clicked.connect(lambda: atras2(ventanaAlmacen, ventanaIniciarSesion))
            ui_ventana9_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana9_ui.obtener_datos_ingresados(a[2]))
            ui_ventana9_ui.botonEliminar.clicked.connect(lambda: ui_ventana9_ui.obtener_datos_ingresados(a[2]))
            ui_ventana9_ui.BuscarPieza.clicked.connect(lambda:ui_ventana9_ui.mostrarAlmacenes(a[2]))
        
        elif a[0] == "jefeTaller":
            mostrar_ventana(ventanaIniciarSesion, ventanaTaller)
            #funcionA(ui_ventana6_ui, ui_ventana_jefeZona, 'aniadirCli', 'ModificarCli')
            ui_ventana10_ui.hola.setText("Hola de nuevo")
            ui_ventana10_ui.hola_2.setText(a[1])
            ui_ventana10_ui.c.setText(a[2])
            ui_ventana10_ui.LineaConc.setText(a[2])
            ui_ventana10_ui.LineaConc.setReadOnly(True)
            ui_ventana10_ui.atras.clicked.connect(lambda: atras2(ventanaTaller, ventanaIniciarSesion))
            ui_ventana10_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana10_ui.obtener_datos_ingresados(a[2]))
            ui_ventana10_ui.botonEliminar.clicked.connect(lambda: ui_ventana10_ui.obtener_datos_ingresados(a[2]))
            ui_ventana10_ui.BuscarMaquinaria.clicked.connect(lambda:ui_ventana10_ui.mostrarTaller(a[2]))

        elif a[0] == "jefeClientes":
            mostrar_ventana(ventanaIniciarSesion, ventanaClientes)
            #funcionA(ui_ventana6_ui, ui_ventana_jefeZona, 'aniadirCli', 'ModificarCli')
            ui_ventana6_ui.hola.setText("Hola de nuevo")
            ui_ventana6_ui.hola_2.setText(a[1])
            ui_ventana6_ui.c.setText(a[2])
            ui_ventana6_ui.LineaConc.setText(a[2])
            ui_ventana6_ui.LineaConc.setReadOnly(True)
            ui_ventana6_ui.atras.clicked.connect(lambda: atras2(ventanaClientes, ventanaIniciarSesion))
            ui_ventana6_ui.botonAniadirModificar.clicked.connect(lambda: ui_ventana6_ui.obtener_datos_ingresados(a[2]))
            ui_ventana6_ui.botonEliminar.clicked.connect(lambda: ui_ventana6_ui.obtener_datos_ingresados(a[2]))
            ui_ventana6_ui.BuscarCli.clicked.connect(lambda:ui_ventana6_ui.mostrarClientes(a[2]))

        elif a[0] == "personal":
            mostrar_ventana(ventanaIniciarSesion, ventanaPersonal)
            ui_ventana_personal.hola_2.setText(a[1])
            ui_ventana_personal.c.setText(a[2])
            ui_ventana_personal.Notificaciones.clicked.connect(lambda: ui_ventana_personal.mostrarNotificaciones(a[2]))
            ui_ventana_personal.taller.clicked.connect(lambda: ui_ventana_personal.mostrarTaller(a[2]))
            ui_ventana_personal.Almacen.clicked.connect(lambda: ui_ventana_personal.mostrarAlmacenes(a[2]))
            ui_ventana_personal.atras.clicked.connect(lambda: atras2(ventanaPersonal, ventanaIniciarSesion))
            ui_ventana_personal.vender.clicked.connect(lambda: ui_ventana_personal.LineaConc.setText(a[2]))
            ui_ventana_personal.botonAniadirModificar.clicked.connect(lambda: ui_ventana_personal.obtener_datos_ingresados(a[2], a[0]))

        else:
            return "Error"

        

    else:
        ui_ventana2_ui.hacerVisible(True)
#"""

def sync_checkbox_state(state, origin, target):
    target.blockSignals(True)
    target.setCheckState(state)

    # Diccionario que mapea (origin, target) a los argumentos de modoClOs
    sync_map = {
        (ui_ventana3_ui.checkBox, ui_ventana4_ui.checkBox): (ui_ventana4_ui.checkBox, ui_ventana4_ui.label, ui_ventana4_ui.lista, ui_ventana4_ui.listaFrames, ui_ventana4_ui.listaTexto, ui_ventana4_ui.ayuda),
        (ui_ventana4_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),

        (ui_ventana3_ui.checkBox, ui_ventana5_ui.checkBox): (ui_ventana5_ui.checkBox, ui_ventana5_ui.label, ui_ventana5_ui.lista, ui_ventana5_ui.listaFrames, ui_ventana5_ui.listaTexto, ui_ventana5_ui.ayuda),
        (ui_ventana5_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),

        (ui_ventana3_ui.checkBox, ui_ventana6_ui.checkBox): (ui_ventana6_ui.checkBox, ui_ventana6_ui.label, ui_ventana6_ui.lista, ui_ventana6_ui.listaFrames, ui_ventana6_ui.listaTexto, ui_ventana6_ui.ayuda),
        (ui_ventana6_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),

        (ui_ventana3_ui.checkBox, ui_ventana7_ui.checkBox): (ui_ventana7_ui.checkBox, ui_ventana7_ui.label, ui_ventana7_ui.lista, ui_ventana7_ui.listaFrames, ui_ventana7_ui.listaTexto, ui_ventana7_ui.ayuda),
        (ui_ventana7_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),

        (ui_ventana3_ui.checkBox, ui_ventana8_ui.checkBox): (ui_ventana8_ui.checkBox, ui_ventana8_ui.label, ui_ventana8_ui.lista, ui_ventana8_ui.listaFrames, ui_ventana8_ui.listaTexto, ui_ventana8_ui.ayuda),
        (ui_ventana8_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),

        (ui_ventana3_ui.checkBox, ui_ventana9_ui.checkBox): (ui_ventana9_ui.checkBox, ui_ventana9_ui.label, ui_ventana9_ui.lista, ui_ventana9_ui.listaFrames, ui_ventana9_ui.listaTexto, ui_ventana9_ui.ayuda),
        (ui_ventana9_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),

        (ui_ventana3_ui.checkBox, ui_ventana10_ui.checkBox): (ui_ventana10_ui.checkBox, ui_ventana10_ui.label, ui_ventana10_ui.lista, ui_ventana10_ui.listaFrames, ui_ventana10_ui.listaTexto, ui_ventana10_ui.ayuda),
        (ui_ventana10_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),

        (ui_ventana3_ui.checkBox, ui_ventana11_ui.checkBox): (ui_ventana11_ui.checkBox, ui_ventana11_ui.label, ui_ventana11_ui.lista, ui_ventana11_ui.listaFrames, ui_ventana11_ui.listaTexto, ui_ventana11_ui.ayuda),
        (ui_ventana11_ui.checkBox, ui_ventana3_ui.checkBox): (ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista),
    }

    sync_map2 = {
        (ui_ventana_jefeZona.checkBox, ui_ventana5_ui.checkBox): (ui_ventana5_ui.checkBox, ui_ventana5_ui.label, ui_ventana5_ui.lista, ui_ventana5_ui.listaFrames, ui_ventana5_ui.listaTexto, ui_ventana5_ui.ayuda),
        (ui_ventana5_ui.checkBox, ui_ventana_jefeZona.checkBox): (ui_ventana_jefeZona.checkBox, ui_ventana_jefeZona.imagen, ui_ventana_jefeZona.lista),

        (ui_ventana_jefeZona.checkBox, ui_ventana6_ui.checkBox): (ui_ventana6_ui.checkBox, ui_ventana6_ui.label, ui_ventana6_ui.lista, ui_ventana6_ui.listaFrames, ui_ventana6_ui.listaTexto, ui_ventana6_ui.ayuda),
        (ui_ventana6_ui.checkBox, ui_ventana_jefeZona.checkBox): (ui_ventana_jefeZona.checkBox, ui_ventana_jefeZona.imagen, ui_ventana_jefeZona.lista),

        (ui_ventana_jefeZona.checkBox, ui_ventana7_ui.checkBox): (ui_ventana7_ui.checkBox, ui_ventana7_ui.label, ui_ventana7_ui.lista, ui_ventana7_ui.listaFrames, ui_ventana7_ui.listaTexto, ui_ventana7_ui.ayuda),
        (ui_ventana7_ui.checkBox, ui_ventana_jefeZona.checkBox): (ui_ventana_jefeZona.checkBox, ui_ventana_jefeZona.imagen, ui_ventana_jefeZona.lista),

        (ui_ventana_jefeZona.checkBox, ui_ventana8_ui.checkBox): (ui_ventana8_ui.checkBox, ui_ventana8_ui.label, ui_ventana8_ui.lista, ui_ventana8_ui.listaFrames, ui_ventana8_ui.listaTexto, ui_ventana8_ui.ayuda),
        (ui_ventana8_ui.checkBox, ui_ventana_jefeZona.checkBox): (ui_ventana_jefeZona.checkBox, ui_ventana_jefeZona.imagen, ui_ventana_jefeZona.lista),

        (ui_ventana_jefeZona.checkBox, ui_ventana10_ui.checkBox): (ui_ventana10_ui.checkBox, ui_ventana10_ui.label, ui_ventana10_ui.lista, ui_ventana10_ui.listaFrames, ui_ventana10_ui.listaTexto, ui_ventana10_ui.ayuda),
        (ui_ventana10_ui.checkBox, ui_ventana_jefeZona.checkBox): (ui_ventana_jefeZona.checkBox, ui_ventana_jefeZona.imagen, ui_ventana_jefeZona.lista),

        (ui_ventana_jefeZona.checkBox, ui_ventana11_ui.checkBox): (ui_ventana11_ui.checkBox, ui_ventana11_ui.label, ui_ventana11_ui.lista, ui_ventana11_ui.listaFrames, ui_ventana11_ui.listaTexto, ui_ventana11_ui.ayuda),
        (ui_ventana11_ui.checkBox, ui_ventana_jefeZona.checkBox): (ui_ventana_jefeZona.checkBox, ui_ventana_jefeZona.imagen, ui_ventana_jefeZona.lista),
}

    # Llamar a modoClOs con los argumentos correspondientes
    if (origin, target) in sync_map:
        modoClOs(*sync_map[(origin, target)])
    
    if (origin, target) in sync_map2:
        modoClOs(*sync_map[(origin, target)])

    target.blockSignals(False)

    

if __name__ == "__main__":
    import sys
    
    logica = Logica()
    controlador = Coordinador()
    # Al coordinador también hay que asignarle la lógica del modelo
    controlador.setModel(logica)


    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = QtWidgets.QMainWindow()
    ui_ventana1 = Ui_MainWindow()
    ui_ventana1.setupUi(ventana_principal)
    ui_ventana1.Continuar.clicked.connect(lambda: mostrar_ventana(ventana_principal, ventanaIniciarSesion))

    ventanaIniciarSesion = QtWidgets.QMainWindow()
    ui_ventana2_ui = Ui_MainWindow2()
    ui_ventana2_ui.setupUi(ventanaIniciarSesion)
    ventanaIniciarSesion.hide()

    ventanaAdmin = QtWidgets.QMainWindow()
    ui_ventana3_ui = Ui_MainWindow3()
    ui_ventana3_ui.setupUi(ventanaAdmin)
    ventanaAdmin.hide()

    ventanaConcesionario = QtWidgets.QMainWindow()
    ui_ventana4_ui = Ui_MainWindow4()
    ui_ventana4_ui.setupUi(ventanaConcesionario)
    ventanaConcesionario.hide()

    ventanaTrabajadores = QtWidgets.QMainWindow()
    ui_ventana5_ui = Ui_MainWindow5()
    ui_ventana5_ui.setupUi(ventanaTrabajadores)
    ventanaTrabajadores.hide()

    ventanaClientes = QtWidgets.QMainWindow()
    ui_ventana6_ui = Ui_MainWindow6()
    ui_ventana6_ui.setupUi(ventanaClientes)
    ventanaClientes.hide()

    ventanaVehiculos = QtWidgets.QMainWindow()
    ui_ventana7_ui = Ui_MainWindow7()
    ui_ventana7_ui.setupUi(ventanaVehiculos)
    ventanaVehiculos.hide()

    ventanaVentas = QtWidgets.QMainWindow()
    ui_ventana8_ui = Ui_MainWindow8()
    ui_ventana8_ui.setupUi(ventanaVentas)
    ventanaVentas.hide()

    ventanaAlmacen = QtWidgets.QMainWindow()
    ui_ventana9_ui = Ui_MainWindow9()
    ui_ventana9_ui.setupUi(ventanaAlmacen)
    ventanaAlmacen.hide()

    ventanaTaller = QtWidgets.QMainWindow()
    ui_ventana10_ui = Ui_MainWindow10()
    ui_ventana10_ui.setupUi(ventanaTaller)
    ventanaTaller.hide()

    ventanaPagos = QtWidgets.QMainWindow()
    ui_ventana11_ui = Ui_MainWindow11()
    ui_ventana11_ui.setupUi(ventanaPagos)
    ventanaPagos.hide()

    ventanaParaClientes = QtWidgets.QMainWindow()
    ui_ventana_Clientes = Ui_MainWindowClientes()
    ui_ventana_Clientes.setupUi(ventanaParaClientes)
    ventanaParaClientes.hide()

    ventanaJefeZona = QtWidgets.QMainWindow()
    ui_ventana_jefeZona = Ui_MainWindow_JefeZona()
    ui_ventana_jefeZona.setupUi(ventanaJefeZona)
    ventanaJefeZona.hide()

    ventanaPersonal =  QtWidgets.QMainWindow()
    ui_ventana_personal = Ui_MainWindow_Personal()
    ui_ventana_personal.setupUi(ventanaPersonal)
    ventanaPersonal.hide()

    # A cada ventada hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    #ventanaRegistroConcesionario.setCoordinador(controlador)
    ui_ventana1.setCoordinador(controlador)
    ui_ventana2_ui.setCoordinador(controlador)
    ui_ventana3_ui.setCoordinador(controlador)
    ui_ventana4_ui.setCoordinador(controlador)
    ui_ventana5_ui.setCoordinador(controlador)
    ui_ventana6_ui.setCoordinador(controlador)
    ui_ventana7_ui.setCoordinador(controlador)
    ui_ventana8_ui.setCoordinador(controlador)
    ui_ventana9_ui.setCoordinador(controlador)
    ui_ventana10_ui.setCoordinador(controlador)
    ui_ventana11_ui.setCoordinador(controlador)
    ui_ventana_Clientes.setCoordinador(controlador)
    ui_ventana_jefeZona.setCoordinador(controlador)
    ui_ventana_personal.setCoordinador(controlador)


    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    #controlador.setViewRegistroConcesionario(controlador)
    controlador.setViewVentanaPrincipal(controlador)
    controlador.setViewVentanaIniciarSesion(controlador)
    controlador.setViewVentanaAdmin(controlador)
    controlador.setViewRegistroConcesionario(controlador)
    controlador.setViewVentanaTrabajadores(controlador)
    controlador.setViewVentanaClientes(controlador)
    controlador.setViewVentanaVehiculos(controlador)
    controlador.setViewVentanaParaClientes(controlador)
    controlador.setViewVentanaAlmacen(controlador)
    controlador.setViewVentanaTaller(controlador)
    controlador.setViewVentanaPago(controlador)
    controlador.setViewRegistroVentas(controlador)
    controlador.setViewVentanaParaJefeZona(controlador)
    controlador.setViewVentanaParaPersonal(controlador)

    ventana_principal.show()
    ui_ventana2_ui.IniciarSesion.clicked.connect(comprobarSesion)
    
    #ui_ventana3_ui.atras.clicked.connect(lambda: atras2(ventanaAdmin, ventanaIniciarSesion))
    #ui_ventana_Clientes.atras.clicked.connect(lambda: atras2(ventanaParaClientes, ventanaIniciarSesion))
    #ui_ventana_jefeZona.atras.clicked.connect(lambda: atras2(ventanaJefeZona, ventanaIniciarSesion))
    #ui_ventana_personal.atras.clicked.connect(lambda: atras2(ventanaPersonal, ventanaIniciarSesion))
    
########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################
    
    #se encarga de mantener el modo oscuro o no entre ventanas
    def sync_checkbox_state(state, current_checkbox, other_checkbox):
        other_checkbox.setChecked(current_checkbox.isChecked())

    def connect_checkboxes(main_ui, other_ui):
        main_ui.checkBox.stateChanged.connect(lambda state: sync_checkbox_state(state, main_ui.checkBox, other_ui.checkBox))
        other_ui.checkBox.stateChanged.connect(lambda state: sync_checkbox_state(state, other_ui.checkBox, main_ui.checkBox))

    # Función para conectar las combinaciones
    def connect_all_checkboxes(ui_elements):
        for i in range(len(ui_elements)):
            for j in range(i + 1, len(ui_elements)):
                connect_checkboxes(ui_elements[i], ui_elements[j])

    # En el código que cambia de ventana, conecta las casillas de verificación
    ui_elements = [ui_ventana3_ui, ui_ventana4_ui, ui_ventana5_ui, ui_ventana6_ui, ui_ventana7_ui, ui_ventana8_ui, ui_ventana9_ui, ui_ventana10_ui, ui_ventana11_ui]
    connect_all_checkboxes(ui_elements)

    ui_elements2 = [ui_ventana_jefeZona, ui_ventana5_ui, ui_ventana6_ui, ui_ventana7_ui, ui_ventana8_ui, ui_ventana10_ui, ui_ventana11_ui]
    connect_all_checkboxes(ui_elements2)
########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

    #borra los pycache automaticamente al cerrar la aplicacion
    app.aboutToQuit.connect(lambda: borrar_pycache(directorio_proyecto))

    sys.exit(app.exec_())


    
