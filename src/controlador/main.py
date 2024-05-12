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
import imagen_rc
import imagenDes_rc

#RESTO
from src.vista.RegistroClienteVentana import RegistroClienteVentana
from src.controlador.Coordinador import Coordinador
from src.modelo.Logica import Logica

from src.vista.RegistroConcesionarioVentana import RegistroConcesionarioVentana


def mostrar_ventana2():
    ventana_principal.hide()
    ventanaIniciarSesion.show()

def comprobarSesion():
    #"""
    #comprobar si el dni y la contrasenia son correctos
    if ui_ventana2_ui.obtener_datos_ingresados() is True:
        ui_ventana2_ui.hacerVisible(False)
    elif ui_ventana2_ui.obtener_datos_ingresados() is False:
        ui_ventana2_ui.hacerVisible(True)
#"""

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
    ui_ventana1.Continuar.clicked.connect(mostrar_ventana2)

    ventanaIniciarSesion = QtWidgets.QMainWindow()
    ui_ventana2_ui = Ui_MainWindow2()
    ui_ventana2_ui.setupUi(ventanaIniciarSesion)
    ventanaIniciarSesion.hide()

    # A cada ventada hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    #ventanaRegistroConcesionario.setCoordinador(controlador)
    ui_ventana1.setCoordinador(controlador)
    ui_ventana2_ui.setCoordinador(controlador)

    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    #controlador.setViewRegistroConcesionario(controlador)
    controlador.setViewVentanaPrincipal(controlador)
    controlador.setViewVentanaIniciarSesion(controlador)

    ventana_principal.show()
    ui_ventana2_ui.IniciarSesion.clicked.connect(comprobarSesion)


    sys.exit(app.exec_())


    
