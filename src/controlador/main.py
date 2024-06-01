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
import imagen_rc
import imagenDes_rc
import nissan2
import nissanGtrClaro
import botonAtrasBlanco
import botonAtrasBlancoAzul

#RESTO
from src.vista.RegistroClienteVentana import RegistroClienteVentana
from src.controlador.Coordinador import Coordinador
from src.modelo.Logica import Logica

from src.vista.RegistroConcesionarioVentana import RegistroConcesionarioVentana


def mostrar_ventana(ventanaInicial, ventanaFinal):
    ventanaInicial.hide()
    ventanaFinal.show()

def atras(ventanaInicial, ventanaFinal):
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
        ui_ventana4_ui.atras.clicked.connect(lambda: atras(ventanaConcesionario, ventanaAdmin))
        ui_ventana4_ui.botonAniadirModificar.clicked.connect(funcionConcesionarios)
        ui_ventana4_ui.botonEliminar.clicked.connect(funcionConcesionarios)
        ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.tablaYbusquedaVisibilidad)
        ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.mostrasConcesionarios)

    elif a[0] in ['administrador', 'jefeZona', 'jefeDepartamento', 'personal']:
        ui_ventana2_ui.hacerVisible(False)
        if a[0] == "administrador":
            mostrar_ventana(ventanaIniciarSesion, ventanaAdmin)
            ui_ventana3_ui.hola_2.setText(a[1])
            ui_ventana3_ui.Concesionario.clicked.connect(lambda: mostrar_ventana(ventanaAdmin, ventanaConcesionario))
            ui_ventana4_ui.atras.clicked.connect(lambda: atras(ventanaConcesionario, ventanaAdmin))
            ui_ventana4_ui.botonAniadirModificar.clicked.connect(funcionConcesionarios)
            ui_ventana4_ui.botonEliminar.clicked.connect(funcionConcesionarios)
            ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.tablaYbusquedaVisibilidad)
            ui_ventana4_ui.BuscarCon.clicked.connect(ui_ventana4_ui.mostrasConcesionarios)
        

    else:
        ui_ventana2_ui.hacerVisible(True)
#"""

def sync_checkbox_state(state, origin, target):
    target.blockSignals(True)
    target.setCheckState(state)
    if target == ui_ventana4_ui.checkBox:
        ui_ventana4_ui.modoClOs()
    elif target == ui_ventana3_ui.checkBox:
        ui_ventana3_ui.modoClOs()
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

    # A cada ventada hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    #ventanaRegistroConcesionario.setCoordinador(controlador)
    ui_ventana1.setCoordinador(controlador)
    ui_ventana2_ui.setCoordinador(controlador)
    ui_ventana3_ui.setCoordinador(controlador)
    ui_ventana4_ui.setCoordinador(controlador)


    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    #controlador.setViewRegistroConcesionario(controlador)
    controlador.setViewVentanaPrincipal(controlador)
    controlador.setViewVentanaIniciarSesion(controlador)
    controlador.setViewVentanaAdmin(controlador)
    controlador.setViewRegistroConcesionario(controlador)

    ventana_principal.show()
    ui_ventana2_ui.IniciarSesion.clicked.connect(comprobarSesion)
    
    ui_ventana3_ui.atras.clicked.connect(lambda: atras(ventanaAdmin, ventanaIniciarSesion))
    
    
    ui_ventana3_ui.checkBox.stateChanged.connect(lambda state: sync_checkbox_state(state, ui_ventana3_ui.checkBox, ui_ventana4_ui.checkBox))
    ui_ventana4_ui.checkBox.stateChanged.connect(lambda state: sync_checkbox_state(state, ui_ventana4_ui.checkBox, ui_ventana3_ui.checkBox))

    sys.exit(app.exec_())


    
