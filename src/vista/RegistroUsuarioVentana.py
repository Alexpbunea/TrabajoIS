
import tkinter as tk
from src.modelo.vo.UserVO import UserVO
from tkinter import messagebox


class RegistroUsuarioVentana:
    def __init__(self, controlador = None):
        # Crea la ventana principal
        self.root = tk.Tk()
        # Almacena una referencia al controlador
        self.coordinador = controlador

        self.id_label = tk.Label(self.root, text="Id:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.nombre_label = tk.Label(self.root, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()

        self.appe1_label = tk.Label(self.root, text="Apellido 1:")
        self.appe1_label.pack()
        self.appe1_entry = tk.Entry(self.root)
        self.appe1_entry.pack()

        self.appe2_label = tk.Label(self.root, text="Apellido 2:")
        self.appe2_label.pack()
        self.appe2_entry = tk.Entry(self.root)
        self.appe2_entry.pack()

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.boton = tk.Button(self.root, text="Guardar", command=self.registrarPersona)
        self.boton.pack()

    def limpiar(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.appe1_entry.delete(0, tk.END)
        self.appe2_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def setVisible(self, visible: bool) -> None:
        if visible:
            self.root.mainloop()
        else:
            self.root.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    #############################Listeners##############################

    def registrarPersona(self) -> None:
        try:
            persona = UserVO(
                idUser =  int(self.id_entry.get()),
                nombre = self.nombre_entry.get(),
                apellido1 = self.appe1_entry.get(),
                apellido2 = self.appe2_entry.get(),
                email = self.email_entry.get()
            )
            self.coordinador.registrarUsuario(persona)
            self.limpiar()
        except Exception as ex:
            messagebox.showwarning("Error", ex)