import AbstractHouseView
import tkinter as tk

class HouseView(AbstractHouseView.AbstractHouseView):
    def __init__(self):
        self.tkinterNotPrepared = True

    def draw(self):
        # @antonoterof
        # Modified by @SantiagoRR2004
        model = self.getModel()
        return model.getAttribute("grid")

    def drawAgent(self, object):
        # @antonoterof
        # Modified by @SantiagoRR2004
        model = self.getModel()
        return model.getAttribute(object)
    
    def setUpTkinter(self):
        # @SantiagoRR2004
        self.prepareTkinter()
        self.print_interface()
        self.load_images()
        self.show_piece()
        self.windows.mainloop()
    
    def prepareTkinter(self, square:int = 70) -> None:
        # @antonvm2004
        # @SantiagoRR2004
        self.square = square
        self.images = {}

        self.windows = tk.Tk()
        self.windows.title("HOUSE")
        self.windows.geometry(f"{str(square * 24)}x{str(square * 12)}")
        self.windows.resizable(0, 0)

        self.interface = tk.Canvas(self.windows)
        self.interface.pack(fill="both", expand=True)

    def print_interface(self):
        # @antonvm2004
        # @SantiagoRR2004
        for i in range(24):
            for j in range(12):
                self.interface.create_rectangle(i * self.square, j * self.square,
                                               (i + 1) * self.square, (j + 1) * self.square)
                
    def load_images(self):
        # @antonvm2004
        # @SantiagoRR2004
        images = self.drawAgent("symbols").values()
        for piece in images:
            img_path = f"./software/GridWorldModel/imagenes/{piece}.png"
            images = tk.PhotoImage(file=img_path)
            images = images.subsample(int(images.width() / self.square), int(images.height() / self.square))
            self.images[piece] = images


    def show_piece(self):
        # @antonvm2004
        # @SantiagoRR2004
        for index_i, i in enumerate(self.draw()):
            for index_j, j in enumerate(i):
                if j != "0":
                    self.interface.create_image(index_j * self.square, index_i * self.square,
                                               image=self.images[int(j)], anchor='nw')
                    
    def updateTkinter(self):
        # @SantiagoRR2004
        if self.tkinterNotPrepared:
            self.setUpTkinter()
            self.tkinterNotPrepared = False
        #self.show_piece()
        #self.windows.wait_window()
        self.windows.update()
        self.windows.update_idletasks()
        #self.windows.mainloop()
