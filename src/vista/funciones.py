from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QTimer

blanco = "#FFFFFF"
negro = "#282e2a"
_translate = QtCore.QCoreApplication.translate


def actualizarTextoIncorrecto2(incorrecto, color, nuevo_texto):
    estilo_html = "<html><head/><body><p align=\"center\"><span style=\" color:{};\">{}</span></p></body></html>"
    incorrecto.setText(QtCore.QCoreApplication.translate("MainWindow", estilo_html.format(color, nuevo_texto)))

#FUNCIONES ESTETICAS PARA LOS MENSAJES AL INSERTAR ALGUN TEXTO
def hide_incorrecto(incorrecto):
    # Hacer invisible el QLabel
    incorrecto.setVisible(False)

def show_incorrecto_for_5_seconds(incorrecto):
    # Hacer visible el QLabel
    incorrecto.setVisible(True)

    # Crear un temporizador que ocultará el QLabel después de 5 segundos
    QTimer.singleShot(5000, lambda: hide_incorrecto(incorrecto))




#FUNCIONES PARA EL MODO OSCURO/CLARO
def estilosClaro(lista):
    for i in lista:
        i.setStyleSheet(
            "QPushButton {\n"
            "    background-color: white;\n"
            "    border: 2px solid black;\n"
            "    color: black;\n"
            "    border-radius: 10px;\n"
            "    font-weight: bold;\n"
            "}\n"
            
            "QPushButton:pressed {\n"
            "    background-color: #2980b9;\n"
            "    color: white;\n"
            "    font-weight: bold;\n"
            "}\n"
        )

def estilosOscuro(lista):
    for i in lista:
        i.setStyleSheet(
            "QPushButton {\n"
            "    background-color: transparent;\n"
            "    border: 2px solid white;\n"
            "    color: white;\n"
            "    border-radius: 10px;\n"
            "    font-weight: bold;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: black;\n"
            "    color: white;\n"
            "    font-weight: bold;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: #2980b9;\n"
            "    color: black;\n"
            "    font-weight: bold;\n"
            "}\n"
        )



#BOTON MODO OSCURO
def modoClOs(checkBox, imagen, lista, listaFrames = [], listaTexto =[]):
    
    if checkBox.isChecked(): #modo oscuro
        #print("Hola1")
        imagen.setStyleSheet("background-image: url(:/direccion/nissan_skyline_gt_r_r34-HD2.jpg);")
        imagen.setPixmap(QtGui.QPixmap("nissan_skyline_gt_r_r34-HD2.jpg"))
        estilosOscuro(lista)
        checkBox.setStyleSheet("QCheckBox::indicator {\n"
                        "    width: 25px;\n"
                        "    height: 25px;\n"
                        "    text-align: right;\n"
                        "}\n"
                        "QCheckBox {\n"
                        "    font-size: 16px; /* Tamaño de la letra en píxeles */\n"
                        "    font-weight: bold;\n"
                        "    color: white;\n"
                        "}")
        if len(listaFrames) == 0:
            pass
        else:
            for i in listaFrames:
                i.setStyleSheet(f"background-color: {negro};\n"
                                "border-radius: 20px;")
        if len(listaTexto) == 0:
            pass
        else:
            for i in listaTexto:
                a = i.objectName()
                i.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-weight:600; color:{blanco};\">{a}:</span></p></body></html>"))

        
    else: #modo claro
        #print("Hola2")
        imagen.setStyleSheet("background-image: url(:/direccion/nissanGtrClaro.jpg);")
        imagen.setPixmap(QtGui.QPixmap("nissanGtrClaro.jpg"))
        estilosClaro(lista)
        checkBox.setStyleSheet("QCheckBox::indicator {\n"
                        "    width: 25px;\n"
                        "    height: 25px;\n"
                        "    text-align: right;\n"
                        "}\n"
                        "QCheckBox {\n"
                        "    font-size: 16px; /* Tamaño de la letra en píxeles */\n"
                        "    font-weight: bold;\n"
                        "    color: black;\n"
                        "}")
        if len(listaFrames) == 0:
            pass
        else:
            for i in listaFrames:
                i.setStyleSheet(f"background-color: {blanco};\n"
                                "border-radius: 20px;")
        if len(listaTexto) == 0:
            pass
        else:
            for i in listaTexto:
                a = i.objectName()
                i.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-weight:600; color:{negro};\">{a}:</span></p></body></html>"))

                
