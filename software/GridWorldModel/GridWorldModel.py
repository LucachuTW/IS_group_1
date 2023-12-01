# Realizado por @antonvm2004
import pygame
import os

class GridWorldModel:
    def __init__(self, square):
        self.square = square
        self.images = {}
        self.matrix = []  # Define your matrix here
        self.screen = pygame.display.set_mode((24 * square, 12 * square))

    def load_images(self):
        images = ["1", "2", "3", "4", "5", "7", "11"]
        for piece in images:
            img_path = f"./software/GridWorldModel/imagenes/{piece}.png"
            image = pygame.image.load(img_path)
            formatted_image = pygame.transform.scale(image, (self.square, self.square))
            self.images[piece] = formatted_image

    def show_piece(self):
        for index_i, i in enumerate(self.matrix):
            for index_j, j in enumerate(i):
                if j != "0":
                    self.screen.blit(self.images[j], (index_j * self.square, index_i * self.square))

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.show_piece()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    # Create an instance of GridWorldModel
    grid = GridWorldModel(70)

    # Call the methods
    grid.load_images()

    # Start the Pygame main loop
    grid.mainloop()