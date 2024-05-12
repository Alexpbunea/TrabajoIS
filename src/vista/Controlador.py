from PyQt5 import QtWidgets
from VentanaPrincipal_ui import Ui_MainWindow
from VentanaIniciarSesion_ui import Ui_MainWindow2

class Controlador(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_ventana1 = Ui_MainWindow()
        self.ui_ventana1.setupUi(self)

        # Conectar el botón en la ventana 1 para cambiar a la ventana 2
        self.ui_ventana1.Continuar.clicked.connect(self.mostrar_ventana2)

        # Crear una instancia de la ventana 2 pero oculta por ahora
        self.ui_ventana2 = QtWidgets.QMainWindow()  # Crear una instancia de QMainWindow
        self.ui_ventana2_ui = Ui_MainWindow2()  # Crear una instancia de la clase de la interfaz de usuario
        self.ui_ventana2_ui.setupUi(self.ui_ventana2)  # Configurar la interfaz en la instancia de QMainWindow
        self.ui_ventana2.hide()  # Ocultar la ventana 2

    def mostrar_ventana2(self):
        self.hide()
        self.ui_ventana2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = Controlador()
    ventana_principal.show()
    sys.exit(app.exec_())
