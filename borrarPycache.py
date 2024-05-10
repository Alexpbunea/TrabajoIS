import os
import shutil

def borrar_pycache(directorio):
    # Iterar sobre los archivos y directorios dentro del directorio dado
    for elemento in os.listdir(directorio):
        ruta = os.path.join(directorio, elemento)
        # Si es un directorio, recurrir para eliminar su __pycache__
        if os.path.isdir(ruta):
            if elemento == "__pycache__":
                print(f"Borrando directorio: {ruta}")
                try:
                    shutil.rmtree(ruta)  # Eliminar el directorio __pycache__ y su contenido
                    print(f"Directorio eliminado: {ruta}")
                except Exception as e:
                    print(f"Error al eliminar directorio {ruta}: {e}")
            else:
                borrar_pycache(ruta)

# Ruta del directorio principal de tu proyecto
directorio_proyecto =r"C:\Users\Dell XPS 9510\Desktop\Ingenieria del software\TrabajoFinal\src"

# Llamar a la función para borrar los archivos __pycache__
print("Eliminando archivos __pycache__...")
borrar_pycache(directorio_proyecto)
print("¡Eliminación completada!")


