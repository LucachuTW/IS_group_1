import tkinter as tk
from typing import Any
import mapa

class App():
    def __init__(self, L_QUADRADO):
        self.gs = mapa.State()
        self.L_QUADRADO = L_QUADRADO
        self.imagenes = {}

        self.ventana = tk.Tk()
        self.ventana.title("casa")
        self.ventana.geometry(f"{str(L_QUADRADO * 24)}x{str(L_QUADRADO * 12)}")
        self.ventana.resizable(0,0)

        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
    
    def __call__(self):
        self.ventana.mainloop()
    
    def dibujarTablero(self):

        for i in range (24):
            for j in range(12):
                self.interfaz.create_rectangle(i*self.L_QUADRADO, j*self.L_QUADRADO, (i+1)*self.L_QUADRADO, (j+1)*self.L_QUADRADO)

    def cargarImagenes(self):
        piezas = ["1"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(file="./imagenes/" + pieza + ".png")
            print(self.imagenes)

    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs.piezas):
            for indice_j, j in enumerate(i):
                if j != "--":
                    print(self.imagenes[j])
                    self.interfaz.create_image(indice_j*self.L_QUADRADO, indice_i*self.L_QUADRADO, image=self.imagenes[j], anchor="nw")
        
MotorDeAjedrez  = App(70)
MotorDeAjedrez.dibujarTablero()
MotorDeAjedrez.cargarImagenes()
MotorDeAjedrez.mostrarPiezas()

MotorDeAjedrez()