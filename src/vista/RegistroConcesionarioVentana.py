# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:09:58 2024

@author: Dell XPS 9510
"""


import tkinter as tk
from src.modelo.vo.ConcesionarioVO import Concesionario
from tkinter import messagebox


class RegistroConcesionarioVentana:
    def __init__(self, controlador = None):
        # Crea la ventana principal
        self.root = tk.Tk()
        # Almacena una referencia al controlador
        self.coordinador = controlador

        self.nombre_label = tk.Label(self.root, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()


        self.direccion_label = tk.Label(self.root, text="Direccion:")
        self.direccion_label.pack()
        self.direccion_label = tk.Entry(self.root)
        self.direccion_label.pack()
        
        self.ciudad_label = tk.Label(self.root, text="Ciudad:")
        self.ciudad_label.pack()
        self.ciudad_entry = tk.Entry(self.root)
        self.ciudad_entry.pack()
        
        self.fecha_label = tk.Label(self.root, text="Fecha inauguracion:")
        self.fecha_label.pack()
        self.fecha_label = tk.Entry(self.root)
        self.fecha_label.pack()

        self.boton = tk.Button(self.root, text="Guardar", command=self.registrarConcesionario)
        self.boton.pack()

    def limpiar(self):
        self.nombre_entry.delete(0, tk.END)
        self.direccion_label.delete(0, tk.END)
        self.ciudad_entry.delete(0, tk.END)
        self.fecha_label.delete(0, tk.END)

    def setVisible(self, visible: bool) -> None:
        if visible:
            self.root.mainloop()
        else:
            self.root.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    #############################Listeners##############################

    def registrarConcesionario(self) -> None:
        try:
            concesionario = Concesionario(
                Nombre=self.nombre_entry.get(),
                Direccion=self.direccion_label.get(),
                Ciudad=self.ciudad_entry.get(),
                FechaInauguracion=self.fecha_label.get()
            )
                
            self.coordinador.registrarConcesionario(concesionario)
            self.limpiar()
        except Exception as ex:
            messagebox.showwarning("Error", ex)