# Realizado por @antonvm2004

import tkinter as tk
import json

class App():
    def __init__(self, L_QUADRADO):

        # Cargar la lista desde un archivo JSON
        with open('./software/GridWorldModel/datos_lista.json', 'r') as archivo_entrada:
            self.gs = json.load(archivo_entrada)


        self.L_QUADRADO = L_QUADRADO
        self.imagenes = {}

        self.ventana = tk.Tk()
        self.ventana.title("casa")
        self.ventana.geometry(f"{str(L_QUADRADO * 24)}x{str(L_QUADRADO * 12)}")
        self.ventana.resizable(0, 0)

        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def dibujarTablero(self):
        for i in range(24):
            for j in range(12):
                self.interfaz.create_rectangle(i * self.L_QUADRADO, j * self.L_QUADRADO,
                                               (i + 1) * self.L_QUADRADO, (j + 1) * self.L_QUADRADO)

    def cargarImagenes(self):
        piezas = ["0", "1", "2"]
        for pieza in piezas:
            # Cargar la imagen original
            img = tk.PhotoImage(file="./software/GridWorldModel/imagenes/" + pieza + ".png")

            # Ajustar la imagen al tamaño del cuadrado
            img = img.subsample(int(img.width() / self.L_QUADRADO), int(img.height() / self.L_QUADRADO))

            self.imagenes[pieza] = img

    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs):
            for indice_j, j in enumerate(i):
                if j != "--":
                    self.interfaz.create_image(indice_j * self.L_QUADRADO, indice_i * self.L_QUADRADO,
                                               image=self.imagenes[j], anchor='nw')

# Crear la aplicación y ejecutarla
MotorDeAjedrez = App(70)
MotorDeAjedrez.dibujarTablero()
MotorDeAjedrez.cargarImagenes()
MotorDeAjedrez.mostrarPiezas()

MotorDeAjedrez()