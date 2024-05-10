# En el cmd de Anaconda: pip install pyqt5
# Una vez isntalado en C:\Users\"user"\anaconda3\Library\bin executamos el designer.exe
# Para abrir un nuevo proyecto: Archivo -> Nuevo -> main Windows
# Arriba a la derecha borramos todo menos el central widget
# guardamos la ventana en la carpeta vista
import sys
ruta_modulo = r'C:\Users\Dell XPS 9510\Desktop\Ingenieria del software\TrabajoFinal'
sys.path.append(ruta_modulo)

from src.vista.RegistroClienteVentana import RegistroClienteVentana
from src.controlador.Coordinador import Coordinador
from src.modelo.Logica import Logica

from src.vista.RegistroConcesionarioVentana import RegistroConcesionarioVentana




if __name__ == "__main__":
    #root = tk.Tk()
    ventanaRegistroConcesionario = RegistroConcesionarioVentana()
    ventanaRegistroCliente = RegistroClienteVentana()
    logica = Logica()
    controlador = Coordinador()

    # A cada ventada hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    ventanaRegistroConcesionario.setCoordinador(controlador)
    ventanaRegistroCliente.setCoordinador(controlador)

    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    controlador.setViewRegistroConcesionario(controlador)
    controlador.setViewRegistroCliente(controlador)

    # Al coordinador también hay que asignarle la lógica del modelo
    controlador.setModel(logica)

    #Para comenzar con la pantalla de inicio: True aparece la pantalla y False la destruye
    ventanaRegistroConcesionario.setVisible(True)
    ventanaRegistroCliente.setVisible(True)

    
