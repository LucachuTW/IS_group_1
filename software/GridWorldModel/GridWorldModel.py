# Realizado por @antonvm2004
import tkinter as tk
import json


class GridWorldModel:
    def __init__(self, square):
        with open("./software/GridWorldModel/datos_lista.json", "r") as archivo_entrada:
            self.matrix = json.load(archivo_entrada)

        self.square = square
        self.images = {}

        self.windows = tk.Tk()
        self.windows.title("HOUSE")
        self.windows.geometry(f"{str(square * 24)}x{str(square * 12)}")
        self.windows.resizable(0, 0)

        self.interface = tk.Canvas(self.windows)
        self.interface.pack(fill="both", expand=True)

    def __call__(self):
        self.windows.mainloop()

    def print_interface(self):
        for i in range(24):
            for j in range(12):
                self.interface.create_rectangle(
                    i * self.square,
                    j * self.square,
                    (i + 1) * self.square,
                    (j + 1) * self.square,
                )

    def load_images(self):
        images = ["1", "2", "3", "4", "5", "7", "11"]
        for piece in images:
            img_path = f"./software/GridWorldModel/imagenes/{piece}.png"
            image = tk.PhotoImage(file=img_path)
            formattedImage = image.subsample(
                int(image.width() / self.square), int(image.height() / self.square)
            )
            self.images[piece] = formattedImage

    def show_piece(self):
        for index_i, i in enumerate(self.matrix):
            for index_j, j in enumerate(i):
                if j != "0":
                    self.interface.create_image(
                        index_j * self.square,
                        index_i * self.square,
                        image=self.images[j],
                        anchor="nw",
                    )


if __name__ == "__main__":
    # Create an instance of GridWorldModel
    grid = GridWorldModel(70)

    # Call the methods
    grid.print_interface()
    grid.load_images()
    grid.show_piece()

    # Start the Tkinter main loop
    grid()
