from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QTimer

blanco = "#FFFFFF"
negro = "#282e2a"
_translate = QtCore.QCoreApplication.translate


#CLASE PARA QUE LAS LETRAS DE ARRIBA TENGAN UNA LINEA DE CONTORNO NEGRA POR SI NO SE VEN
class BorderedTextLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("color: white;")  # Set text color to white
        

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        painter.setPen(pen)

        # Draw the text with a border
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    painter.drawText(self.rect().adjusted(dx, dy, dx, dy), QtCore.Qt.AlignLeft, self.text())

        # Draw the text itself
        pen.setColor(QtCore.Qt.white)
        painter.setPen(pen)
        painter.drawText(self.rect(), QtCore.Qt.AlignLeft, self.text())
        painter.end()






#funcion atras presente en todas las ventanas
def setAtras(centralWidget):
    atras = QtWidgets.QPushButton(centralWidget)
    atras.setGeometry(QtCore.QRect(1160, 640, 51, 51))
    atras.setStyleSheet("#atras{\n"
                        "border-image: url(:/direccion/botonAtrasBlanco.png);\n"
                        "background-color: transparent;\n"
                        "background: none;\n"
                        "border: none;\n"
                        "background-repeat: none;\n"
                    "}\n"
                    "#atras:pressed{\n"
                        "border-image: url(:/direccion/bottonAtrasBlancoAzul.jpg);\n"
                        "background-color: transparent;\n"
                        "background: none;\n"
                        "border: none;\n"
                        "background-repeat: none;\n"
                    "}")
    atras.setText("")
    atras.setObjectName("atras")
    atras.setToolTip("Atras")
    return atras

def ayuda(centralwiddget, dondeEstoy=None):
    textEdit = QtWidgets.QTextEdit(centralwiddget)
    textEdit.setObjectName("textEdit")

    if dondeEstoy == "Ventana concesionario":
        textEdit.setGeometry(QtCore.QRect(200, 180, 221, 200))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Direccion: texto sin restricciones</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ciudad: Texto sin restricciones</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fecha: dd-mm-yyyy</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    
    elif dondeEstoy == "Ventana trabajadores":
        textEdit.setGeometry(QtCore.QRect(110, 170, 221, 265))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IDtrabajador: DNI correcto</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre y apellidos: Mas de una letra</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sueldo: numero</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rol: administrador, jefeZona,</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     jefeDepartamento, personal</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    
    elif dondeEstoy == "Ventana clientes":
        textEdit.setGeometry(QtCore.QRect(110, 170, 221, 265))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IDcliente: DNI correcto</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre y apellidos: Mas de una letra</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Direccion: texto sin formato</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email: @ en él</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    
    elif dondeEstoy == "Ventana vehiculos":
        textEdit.setGeometry(QtCore.QRect(110, 170, 221, 265))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IDvehiculo: número bastidor idealmente</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Marca y modelo: Más de una letra</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Combustible: gasolina, eléctrico</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">             diésel, híbrido</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Km: Número positivo menor o</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    igual que 2000000</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    

    elif dondeEstoy == "Ventana ventas":
        textEdit.setGeometry(QtCore.QRect(110, 170, 221, 265))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IDvehiculo: número bastidor idealmente</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Marca y modelo: Más de una letra</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Combustible: gasolina, eléctrico</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">             diésel, híbrido</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Km: Número positivo menor o</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    igual que 2000000</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    
    elif dondeEstoy == "Ventana almacen":
        textEdit.setGeometry(QtCore.QRect(110, 170, 221, 265))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IDvehiculo: número bastidor idealmente</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Marca y modelo: Más de una letra</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Combustible: gasolina, eléctrico</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">             diésel, híbrido</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Km: Número positivo menor o</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    igual que 2000000</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    
    elif dondeEstoy == "Ventana taller":
        textEdit.setGeometry(QtCore.QRect(110, 170, 221, 265))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IDvehiculo: número bastidor idealmente</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Marca y modelo: Más de una letra</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Combustible: gasolina, eléctrico</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">             diésel, híbrido</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Km: Número positivo menor o</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    igual que 2000000</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    

    elif dondeEstoy == "Ventana pago":
        textEdit.setGeometry(QtCore.QRect(110, 170, 221, 265))
        textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formato:</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IDvehiculo: número bastidor idealmente</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Marca y modelo: Más de una letra</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Combustible: gasolina, eléctrico</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">             diésel, híbrido</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Km: Número positivo menor o</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    igual que 2000000</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nombre: Cofemotor + texto/num</p>\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ej: &quot;Cofermotor20&quot;</p>\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        return textEdit
    
    elif dondeEstoy == "Ventana para clientes":
        textEdit.setGeometry(QtCore.QRect(200, 180, 221, 200))

        return textEdit



###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################


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



#FUNCIONES DE LA VISIBILIDAD, OSCULTAR O MOSTRAR FRAMES
def toggle_frame_visibility(frame1, frame2, tabla, barra, ayuda=None):
    if frame2.isVisible(): 
        frame2_visibility(frame1, frame2, tabla, barra, ayuda)
    elif tabla.isVisible():
        tablaYbusquedaVisibilidad(frame1, frame2, tabla, barra, ayuda)
    current_visibility = frame1.isVisible()
    frame1.setVisible(not current_visibility)
    if ayuda is None:
        pass
    else:
        ayuda.setVisible(not current_visibility)
    

def frame2_visibility(frame1, frame2, tabla, barra, ayuda=None):
    if frame1.isVisible():
        toggle_frame_visibility(frame1, frame2, tabla, barra, ayuda)
    elif tabla.isVisible():
        tablaYbusquedaVisibilidad(frame1, frame2, tabla, barra, ayuda)
    current_visibility = frame2.isVisible()
    frame2.setVisible(not current_visibility)
    if ayuda is None:
        pass
    else:
        ayuda.setVisible(False)

def tablaYbusquedaVisibilidad(frame1, frame2, tabla, barra, ayuda=None):
    if frame1.isVisible():
        toggle_frame_visibility(frame1, frame2, tabla, barra, ayuda)
    elif frame2.isVisible(): 
        frame2_visibility(frame1, frame2, tabla, barra, ayuda)
    current_visibility = tabla.isVisible()
    tabla.setVisible(not current_visibility)
    barra.setVisible(not current_visibility)
    if ayuda is None:
        pass
    else:
        ayuda.setVisible(False)

def actualizarBotonFrame(palabra, boton):
    boton.setText(palabra)




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
def modoClOs(checkBox, imagen, lista, listaFrames = [], listaTexto =[], ayuda = None, tabla=None, barra=None):
    
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
        
        if ayuda == None:
            pass
        else:
            ayuda.setStyleSheet("""
                QTextEdit {
                border-radius: 20px;      /* Bordes redondeados */
                color: white;             /* Letra blanca */
                background-color: "#282e2a";   /* Fondo oscuro para contraste */
                }
                """)
        
        if barra == None:
            pass
        else:
            barra.setStyleSheet(f"""
            QLineEdit {{
                background-color: {negro};  /* Fondo negro */
                color: white;             /* Letras blancas */
                border: 2px solid white;  /* Borde blanco */
                border-radius: 5px;       /* Bordes redondeados */
            }}
            """)

        if tabla == None:
            pass
        else:
            tabla.setStyleSheet(f"""
            QTableWidget {{
                gridline-color: {blanco};   /* Líneas de la cuadrícula blancas */
            }}
            QHeaderView::section {{
                background-color: {negro};  /* Fondo negro en el encabezado */
                color: {blanco};            /* Letras blancas en el encabezado */
            }}
            QTableWidget::item {{
                background-color: {negro};  /* Fondo negro en las celdas */
                color: {blanco};            /* Letras blancas en las celdas */
            }}
            QTableWidget::item:selected {{
                background-color: {blanco}; /* Fondo blanco en las celdas seleccionadas */
                color: {negro};             /* Letras negras en las celdas seleccionadas */
            }}
            QTableWidget QTableCornerButton::section {{
                background-color: {negro};  /* Fondo negro en la esquina superior izquierda */
            }}
        """)

        
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
        
        if ayuda == None:
            pass
        else:
            ayuda.setStyleSheet("""
                QTextEdit {
                border-radius: 20px;      /* Bordes redondeados */
                color: black;             /* Letra blanca */
                background-color: #FFFFFF;   /* Fondo oscuro para contraste */
                }
                """)
                
        if barra == None:
            pass
        else:
            barra.setStyleSheet(f"""
            QLineEdit {{
                background-color: {blanco};  /* Fondo negro */
                color: black;             /* Letras blancas */
                border: 2px solid black;  /* Borde blanco */
                border-radius: 5px;       /* Bordes redondeados */
            }}
            """)

        if tabla == None:
            pass
        else:
            tabla.setStyleSheet(f"""
            QTableWidget {{
                background-color: {blanco};  /* Fondo negro */
                color: black;             /* Letras blancas */
                gridline-color: white;    /* Líneas de la cuadrícula blancas */
            }}
            QHeaderView::section {{
                background-color: {blanco};  /* Fondo negro en el encabezado */
                color: black;             /* Letras blancas en el encabezado */
            }}
            QTableWidget QTableCornerButton::section {{
                background-color: {blanco};  /* Fondo negro en la esquina superior izquierda */
            }}
            """)

                
