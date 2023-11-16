# Este codigo fue creado por @antonvm2004
# Consiste en el desarrollo del GridWorldModel la creacion de la cuadricula en Tkinter y las opciones graficas de la misma

from tkinter import *
from tkinter import PhotoImage

import os 

class GridWorldModel(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        #self.geometry("640x640+500+150")
        self.plan=Canvas(self)
        self.plan.pack(fill="both", expand=True)
        self.imagenes = {}

        self.square()
        #self.cargarImagenes()
        #self.mostrarPiezas()
        #self.load_images()
    
    def square(self):
        for i in range(24):
            for j in range(12):
                
                # Creacion de paredes
                # Paredes Verticales
                if (i==8):
                    for a in range(11):
                        print(a)
                        if (a == 6):
                            pass
                        else:
                            self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                

                elif (i==14 and j== 0):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==14 and j== 1):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==14 and j== 2):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")


                # Paredes Horizontales
                elif (i==1 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==2 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==3 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==4 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")          
                elif (i==5 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==6 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==7 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==8 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==9 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==10 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")          
                elif (i==11 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==13 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==14 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==15 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==16 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==17 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==18 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")          
                elif (i==19 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==20 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==21 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==22 and j== 7):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")

                elif (i==9 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==10 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==11 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==13 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==14 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==15 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==16 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==17 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==18 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==19 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==20 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==21 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")
                elif (i==22 and j== 4):
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60, fill="black")                    
                
                else:
                    self.plan.create_rectangle(i*60, j*60, (i+1)*60, (j+1)*60)

    def load_images(self):
        # Cambia 'ruta_de_la_imagen.png' por la ruta de tu imagen
        image_path = 'a.png'
        
        # Carga la imagen
        img = PhotoImage(file=image_path)

        # Añade la imagen al canvas en la posición 0x0
        self.imagenes['imagen_0x0'] = img
        self.plan.create_image(0, 0, anchor=NW, image=img)

if __name__=="__main__":

    app = GridWorldModel()
    app.mainloop()
