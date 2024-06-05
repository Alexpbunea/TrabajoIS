# En el cmd de Anaconda: pip install pyqt5
# Una vez isntalado en C:\Users\"user"\anaconda3\Library\bin executamos el designer.exe
# Para abrir un nuevo proyecto: Archivo -> Nuevo -> main Windows
# Arriba a la derecha borramos todo menos el central widget
# guardamos la ventana en la carpeta vista
import sys
ruta_modulo = r'C:\Users\Dell XPS 9510\Desktop\Ingenieria del software\TrabajoFinal'
sys.path.append(ruta_modulo)


#VENTANA PRINCIPAL
#from src.vista.Controlador import Controlador
from PyQt5 import QtWidgets
from src.vista.VentanaPrincipal_ui import Ui_MainWindow
from src.vista.VentanaIniciarSesion_ui import Ui_MainWindow2
from src.vista.VentanaAdmin import Ui_MainWindow3
from src.vista.VentanaConcesionario import Ui_MainWindow4
from src.vista.VentanaTrabajadores import Ui_MainWindow5
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
    


def funcionConcesionarios():
        ui_ventana4_ui.obtener_datos_ingresados()

def comprobarSesion():
    #"""
    #comprobar si el dni y la contrasenia son correctos
    a = ui_ventana2_ui.obtener_datos_ingresados()

    if a is False:
        ui_ventana2_ui.hacerVisible(True)

    elif a[0] == "cliente":
        ui_ventana2_ui.hacerVisible(False)
        mostrar_ventana(ventanaIniciarSesion, ventanaAdmin)
        ui_ventana3_ui.hola_2.setText(a[1])
        ui_ventana3_ui.Concesionario.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaConcesionario))
        
        ui_ventana4_ui.atras.clicked.connect(lambda: atras2(ventanaConcesionario, ventanaAdmin))
        ui_ventana4_ui.botonAniadirModificar.clicked.connect(funcionConcesionarios)
        ui_ventana4_ui.botonEliminar.clicked.connect(funcionConcesionarios)
        ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.mostrasConcesionarios)

        ui_ventana3_ui.Trabajador.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaTrabajadores))
        ui_ventana5_ui.atras.clicked.connect(lambda: atras2(ventanaTrabajadores, ventanaAdmin))
        ui_ventana5_ui.botonAniadirModificar.clicked.connect(ui_ventana5_ui.obtener_datos_ingresados)
        ui_ventana5_ui.botonEliminar.clicked.connect(ui_ventana5_ui.obtener_datos_ingresados)
        ui_ventana5_ui.BuscarTra.clicked.connect(ui_ventana5_ui.mostrarTrabajadores)

    elif a[0] in ['administrador', 'jefeZona', 'jefeDepartamento', 'personal']:
        ui_ventana2_ui.hacerVisible(False)
        if a[0] == "administrador":
            mostrar_ventana(ventanaIniciarSesion, ventanaAdmin)
            ui_ventana3_ui.hola_2.setText(a[1])
            ui_ventana3_ui.Concesionario.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaConcesionario))
            
            ui_ventana4_ui.atras.clicked.connect(lambda: atras2(ventanaConcesionario, ventanaAdmin))
            ui_ventana4_ui.botonAniadirModificar.clicked.connect(funcionConcesionarios)
            ui_ventana4_ui.botonEliminar.clicked.connect(funcionConcesionarios)
            ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.tablaYbusquedaVisibilidad)
            ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.mostrasConcesionarios)
        
        elif a[0] == "jefeZona":
            pass

        elif a[0] == "jefeDepartamento":
            pass

        elif a[0] == "personal":
            mostrar_ventana(ventanaIniciarSesion, ventanaAdmin)
            ui_ventana3_ui.hola_2.setText(a[1])
            ui_ventana3_ui.Concesionario.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaConcesionario))
            
            ui_ventana4_ui.atras.clicked.connect(lambda: atras2(ventanaConcesionario, ventanaAdmin))
            ui_ventana4_ui.botonAniadirModificar.clicked.connect(funcionConcesionarios)
            ui_ventana4_ui.botonEliminar.clicked.connect(funcionConcesionarios)
            ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.tablaYbusquedaVisibilidad)
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

    # A cada ventada hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    #ventanaRegistroConcesionario.setCoordinador(controlador)
    ui_ventana1.setCoordinador(controlador)
    ui_ventana2_ui.setCoordinador(controlador)
    ui_ventana3_ui.setCoordinador(controlador)
    ui_ventana4_ui.setCoordinador(controlador)
    ui_ventana5_ui.setCoordinador(controlador)


    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    #controlador.setViewRegistroConcesionario(controlador)
    controlador.setViewVentanaPrincipal(controlador)
    controlador.setViewVentanaIniciarSesion(controlador)
    controlador.setViewVentanaAdmin(controlador)
    controlador.setViewRegistroConcesionario(controlador)
    controlador.setViewVentanaTrabajadores(controlador)

    ventana_principal.show()
    ui_ventana2_ui.IniciarSesion.clicked.connect(comprobarSesion)
    
    ui_ventana3_ui.atras.clicked.connect(lambda: atras2(ventanaAdmin, ventanaIniciarSesion))
    
    


    
    #se encarga de mantener el modo oscuro o no entre ventanas
    def sync_checkbox_state(state, current_checkbox, other_checkbox):
        other_checkbox.setChecked(current_checkbox.isChecked())

    def connect_checkboxes(main_ui, other_ui):
        main_ui.checkBox.stateChanged.connect(lambda state: sync_checkbox_state(state, main_ui.checkBox, other_ui.checkBox))
        other_ui.checkBox.stateChanged.connect(lambda state: sync_checkbox_state(state, other_ui.checkBox, main_ui.checkBox))

    # En el código que cambia de ventana, conecta las casillas de verificación
    connect_checkboxes(ui_ventana3_ui, ui_ventana4_ui)
    connect_checkboxes(ui_ventana3_ui, ui_ventana5_ui)
    connect_checkboxes(ui_ventana4_ui, ui_ventana5_ui)




    sys.exit(app.exec_())


    
