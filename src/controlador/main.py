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
from src.vista.funciones import *

import Imagespy.imagen_rc
import Imagespy.imagenDes_rc
import Imagespy.nissan2
import Imagespy.nissanGtrClaro
import Imagespy.botonAtrasBlanco
import Imagespy.botonAtrasBlancoAzul

#RESTO
from src.vista.RegistroClienteVentana import RegistroClienteVentana
from src.controlador.Coordinador import Coordinador
from src.modelo.Logica import Logica

from src.vista.RegistroConcesionarioVentana import RegistroConcesionarioVentana


def mostrar_ventana(ventanaInicial, ventanaFinal):
    ventanaInicial.hide()
    ventanaFinal.show()

def atras2(ventanaInicial, ventanaFinal):
    ventanaInicial.hide()
    ventanaFinal.show()
    
        

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

        ui_ventana_Clientes.botonComprarVeh.clicked.connect(ui_ventana_Clientes.obtener_datos_ingresados)
        ui_ventana_Clientes.botonReparar.clicked.connect(ui_ventana_Clientes.obtener_datos_ingresados)
        
        
        

    elif a[0] in ['administrador', 'jefeZona', 'personal', 'jefeVentas', 'jefeAlmacen', 'jefeTaller', 'jefeClientes']:
        ui_ventana2_ui.hacerVisible(False)
        if a[0] == "administrador":
            ui_ventana2_ui.hacerVisible(False)
            mostrar_ventana(ventanaIniciarSesion, ventanaAdmin)
            ui_ventana3_ui.hola_2.setText(a[1])
            ui_ventana3_ui.Concesionario.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaConcesionario))
            
            ui_ventana4_ui.atras.clicked.connect(lambda: atras2(ventanaConcesionario, ventanaAdmin))
            ui_ventana4_ui.botonAniadirModificar.clicked.connect(ui_ventana4_ui.obtener_datos_ingresados)
            ui_ventana4_ui.botonEliminar.clicked.connect(ui_ventana4_ui.obtener_datos_ingresados)
            ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.mostrasConcesionarios)

            ui_ventana3_ui.Trabajador.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaTrabajadores))
            ui_ventana5_ui.atras.clicked.connect(lambda: atras2(ventanaTrabajadores, ventanaAdmin))
            ui_ventana5_ui.botonAniadirModificar.clicked.connect(ui_ventana5_ui.obtener_datos_ingresados)
            ui_ventana5_ui.botonEliminar.clicked.connect(ui_ventana5_ui.obtener_datos_ingresados)
            ui_ventana5_ui.BuscarTra.clicked.connect(ui_ventana5_ui.mostrarTrabajadores)

            ui_ventana3_ui.Cliente.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaClientes))
            ui_ventana6_ui.atras.clicked.connect(lambda: atras2(ventanaClientes, ventanaAdmin))
            ui_ventana6_ui.botonAniadirModificar.clicked.connect(ui_ventana6_ui.obtener_datos_ingresados)
            ui_ventana6_ui.botonEliminar.clicked.connect(ui_ventana6_ui.obtener_datos_ingresados)
            ui_ventana6_ui.BuscarCli.clicked.connect(ui_ventana6_ui.mostrarClientes)

            ui_ventana3_ui.vehiculos.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaVehiculos))
            ui_ventana7_ui.atras.clicked.connect(lambda: atras2(ventanaVehiculos, ventanaAdmin))
            ui_ventana7_ui.botonAniadirModificar.clicked.connect(ui_ventana7_ui.obtener_datos_ingresados)
            ui_ventana7_ui.botonEliminar.clicked.connect(ui_ventana7_ui.obtener_datos_ingresados)
            ui_ventana7_ui.BuscarVeh.clicked.connect(ui_ventana7_ui.mostrarVehiculos)

            ui_ventana3_ui.ventas.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaVentas))
            ui_ventana8_ui.atras.clicked.connect(lambda: atras2(ventanaVentas, ventanaAdmin))
            ui_ventana8_ui.botonAniadirModificar.clicked.connect(ui_ventana8_ui.obtener_datos_ingresados)
            ui_ventana8_ui.botonEliminar.clicked.connect(ui_ventana8_ui.obtener_datos_ingresados)
            ui_ventana8_ui.BuscarVen.clicked.connect(ui_ventana8_ui.mostrarVentas)

            ui_ventana3_ui.Almacen.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaAlmacen))
            ui_ventana9_ui.atras.clicked.connect(lambda: atras2(ventanaAlmacen, ventanaAdmin))
            ui_ventana9_ui.botonAniadirModificar.clicked.connect(ui_ventana9_ui.obtener_datos_ingresados)
            ui_ventana9_ui.botonEliminar.clicked.connect(ui_ventana9_ui.obtener_datos_ingresados)
            ui_ventana9_ui.BuscarPieza.clicked.connect(ui_ventana9_ui.mostrarAlmacenes)

            ui_ventana3_ui.Taller.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaTaller))
            ui_ventana10_ui.atras.clicked.connect(lambda: atras2(ventanaTaller, ventanaAdmin))
            ui_ventana10_ui.botonAniadirModificar.clicked.connect(ui_ventana10_ui.obtener_datos_ingresados)
            ui_ventana10_ui.botonEliminar.clicked.connect(ui_ventana10_ui.obtener_datos_ingresados)
            ui_ventana10_ui.BuscarMaquinaria.clicked.connect(ui_ventana10_ui.mostrarTaller)

            ui_ventana3_ui.pago.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaPagos))
            ui_ventana11_ui.atras.clicked.connect(lambda: atras2(ventanaPagos, ventanaAdmin))
            ui_ventana11_ui.botonAniadirModificar.clicked.connect(ui_ventana11_ui.obtener_datos_ingresados)
            ui_ventana11_ui.botonEliminar.clicked.connect(ui_ventana11_ui.obtener_datos_ingresados)
            ui_ventana11_ui.BuscarPago.clicked.connect(ui_ventana11_ui.mostrarPagos)

        elif a[0] == "jefeZona":
            pass

        elif a[0] == "jefeVentas":
            pass

        elif a[0] == "jefeAlmacen":
            pass
        
        elif a[0] == "jefeTaller":
            pass

        elif a[0] == "jefeClientes":
            pass

        elif a[0] == "personal":
            mostrar_ventana(ventanaIniciarSesion, ventanaAdmin)
            ui_ventana3_ui.hola_2.setText(a[1])
            ui_ventana3_ui.Concesionario.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaConcesionario))
            
            ui_ventana4_ui.atras.clicked.connect(lambda: atras2(ventanaConcesionario, ventanaAdmin))
            ui_ventana4_ui.botonAniadirModificar.clicked.connect(ui_ventana4_ui.obtener_datos_ingresados)
            ui_ventana4_ui.botonEliminar.clicked.connect(ui_ventana4_ui.obtener_datos_ingresados)
            ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.mostrasConcesionarios)

        else:
            return "Error"

        

    else:
        ui_ventana2_ui.hacerVisible(True)
#"""

def sync_checkbox_state(state, origin, target):
    target.blockSignals(True)
    target.setCheckState(state)
    #caso ventanaAdmin-VentanaConcesionario
    if origin == ui_ventana3_ui.checkBox and target == ui_ventana4_ui.checkBox:
        modoClOs(ui_ventana4_ui.checkBox, ui_ventana4_ui.label, ui_ventana4_ui.lista, ui_ventana4_ui.listaFrames, ui_ventana4_ui.listaTexto, ui_ventana4_ui.ayuda)
    elif origin == ui_ventana4_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)

    #caso ventanaAdmin-VentanaTrabajadores
    elif origin == ui_ventana3_ui.checkBox and target == ui_ventana5_ui.checkBox:
        modoClOs(ui_ventana5_ui.checkBox, ui_ventana5_ui.label, ui_ventana5_ui.lista, ui_ventana5_ui.listaFrames, ui_ventana5_ui.listaTexto, ui_ventana5_ui.ayuda)
    elif origin == ui_ventana5_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)


    #caso ventanaAdmin-VentanaClientes
    elif origin == ui_ventana3_ui.checkBox and target == ui_ventana6_ui.checkBox:
        modoClOs(ui_ventana6_ui.checkBox, ui_ventana6_ui.label, ui_ventana5_ui.lista, ui_ventana6_ui.listaFrames, ui_ventana6_ui.listaTexto, ui_ventana6_ui.ayuda)
    elif origin == ui_ventana6_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)

    #caso ventanaAdmin-VentanaVehiculos
    elif origin == ui_ventana3_ui.checkBox and target == ui_ventana7_ui.checkBox:
        modoClOs(ui_ventana7_ui.checkBox, ui_ventana7_ui.label, ui_ventana7_ui.lista, ui_ventana7_ui.listaFrames, ui_ventana7_ui.listaTexto, ui_ventana7_ui.ayuda)
    elif origin == ui_ventana7_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)

    #caso ventanaAdmin-VentanaVentas
    elif origin == ui_ventana3_ui.checkBox and target == ui_ventana8_ui.checkBox:
        modoClOs(ui_ventana8_ui.checkBox, ui_ventana8_ui.label, ui_ventana8_ui.lista, ui_ventana8_ui.listaFrames, ui_ventana8_ui.listaTexto, ui_ventana8_ui.ayuda)
    elif origin == ui_ventana8_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)

    #caso ventanaAdmin-VentanaAlmacen
    elif origin == ui_ventana3_ui.checkBox and target == ui_ventana9_ui.checkBox:
        modoClOs(ui_ventana9_ui.checkBox, ui_ventana9_ui.label, ui_ventana9_ui.lista, ui_ventana9_ui.listaFrames, ui_ventana9_ui.listaTexto, ui_ventana9_ui.ayuda)
    elif origin == ui_ventana9_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)

    #caso ventanaAdmin-VentanaTaller
    elif origin == ui_ventana3_ui.checkBox and target == ui_ventana10_ui.checkBox:
        modoClOs(ui_ventana10_ui.checkBox, ui_ventana10_ui.label, ui_ventana10_ui.lista, ui_ventana10_ui.listaFrames, ui_ventana10_ui.listaTexto, ui_ventana10_ui.ayuda)
    elif origin == ui_ventana10_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)
    
    #caso ventanaAdmin-VetanaPago
    elif origin == ui_ventana3_ui.checkBox and target == ui_ventana11_ui.checkBox:
        modoClOs(ui_ventana11_ui.checkBox, ui_ventana11_ui.label, ui_ventana11_ui.lista, ui_ventana11_ui.listaFrames, ui_ventana11_ui.listaTexto, ui_ventana11_ui.ayuda)
    elif origin == ui_ventana11_ui.checkBox and target == ui_ventana3_ui.checkBox:
        modoClOs(ui_ventana3_ui.checkBox, ui_ventana3_ui.imagen, ui_ventana3_ui.lista)

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

    ventana_principal.show()
    ui_ventana2_ui.IniciarSesion.clicked.connect(comprobarSesion)
    
    ui_ventana3_ui.atras.clicked.connect(lambda: atras2(ventanaAdmin, ventanaIniciarSesion))
    ui_ventana_Clientes.atras.clicked.connect(lambda: atras2(ventanaParaClientes, ventanaIniciarSesion))
    
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

########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

    #borra los pycache automaticamente al cerrar la aplicacion
    app.aboutToQuit.connect(lambda: borrar_pycache(directorio_proyecto))

    sys.exit(app.exec_())


    
