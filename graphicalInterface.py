import pygame
import functools
from typing import Any, List
import sys
from events import Events  # pip install events


class GraphicalInterface:
    def __init__(self, view: Any, controllers: List = []) -> None:
        """
        Initializes the graphical interface. This should work but it doesn't.

        Args:
            - view (Any): The view of the house.
            - controllers (List): A list of controllers.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        self.pygameNotReady = True
        self.view = view
        self.events = Events()
        self.events.on_change += self.handle_change
        self.controllers = set(controllers)
        self.setControllers(controllers)

    def setControllers(self, controllers: List) -> None:
        """
        Sets the controllers. This tries to make it so when a function
        in changes is run it calls the handle_change function.

        Args:
            - controllers (List): A list of controllers.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        for i in controllers:
            changes = i.getFunctionsChangeModel()
            print(changes)
            for j in changes:
                self.events.on_change += lambda *args, j=j, **kwargs: j(
                    self.handle_change, *args, **kwargs
                )

    def handle_change(self):
        # This method will be called when any change occurs
        self.updateImage()

    def load_images(self) -> None:
        """
        Loads and scales images for the house view.

        Returns:
            None

        Contributors:
            - @antonvm2004
        """
        images = {}
        for name, number in self.drawAgent("symbols").items():
            img_path = f"./images/{name}.png"
            image = pygame.image.load(img_path)
            image = pygame.transform.scale(image, (self.GRID_SIZE, self.GRID_SIZE))
            images[number] = image
        self.images = images

    def draw_grid(self) -> None:
        """
        Draw the grid.

        Args:
            - None

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        for x in range(0, self.num_columns * self.GRID_SIZE, self.GRID_SIZE):
            pygame.draw.line(
                self.screen, self.BLACK, (x, 0), (x, self.num_rows * self.GRID_SIZE)
            )
        for y in range(0, self.num_rows * self.GRID_SIZE, self.GRID_SIZE):
            pygame.draw.line(
                self.screen, self.BLACK, (0, y), (self.num_columns * self.GRID_SIZE, y)
            )

    def draw_pieces(self, matrix: List) -> None:
        """
        Draw the pieces on the matrix.

        Args:
            - matrix (List): The matrix representing the game board.

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        for index_i, row in enumerate(matrix):
            for index_j, piece in enumerate(row):
                if piece != 0:
                    pieces = self.getModel().PrimeFactorization(piece)
                    for pi in pieces:
                        self.screen.blit(
                            self.images.get(pi, self.images[2]),
                            (index_j * self.GRID_SIZE, index_i * self.GRID_SIZE),
                        )

    def move_robot(self, matrix: List, from_pos: List, to_pos: List) -> None:
        """
        Move the robot from one position to another in the matrix.

        Args:
            - matrix (List[List[str]]): The matrix representing the house view.
            - from_pos (List[int]): The current position of the robot in the matrix.
            - to_pos (List[int]): The target position where the robot should be moved.

        Returns:
            - None

        Contributors:
            - @antonvm2004
        """
        current_piece = matrix[from_pos[0]][from_pos[1]]

        if 0 <= to_pos[0] < len(matrix) and 0 <= to_pos[1] < len(matrix[0]):
            target_piece = matrix[to_pos[0]][to_pos[1]]

            if current_piece == "11":
                if target_piece == "3":
                    matrix[to_pos[0]][to_pos[1]] = current_piece
                    matrix[from_pos[0]][from_pos[1]] = "0"
                elif target_piece == "0":
                    matrix[to_pos[0]][to_pos[1]] = current_piece
                    matrix[from_pos[0]][from_pos[1]] = "0"
                else:
                    matrix[from_pos[0]][from_pos[1]] = current_piece

    def preparePygame(self) -> None:
        """
        Prepare pygame.

        This method initializes the pygame library and
        sets up the necessary variables and configurations for the game interface.

        Args:
            - None

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        pygame.init()

        # Define colors
        self.WHITE = (246, 246, 246)
        self.BLACK = (0, 0, 0)

        # Grid size
        self.GRID_SIZE = 50

        matrix = self.draw()

        door_info = self.drawAgent("door")

        num_rows = len(matrix)
        self.num_rows = num_rows
        num_columns = len(matrix[0]) if num_rows > 0 else 0
        self.num_columns = num_columns

        WINDOW_WIDTH = num_columns * self.GRID_SIZE
        WINDOW_HEIGHT = num_rows * self.GRID_SIZE

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Interface with Mobile Image")

        self.load_images()

    def showImage(self) -> None:
        """
        Show the image.

        This method displays the image on the screen using the Pygame library.
        It draws a grid and the pieces of the image on the screen.

        Args:
            - None

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        matrix = self.draw()

        for index_i, row in enumerate(matrix):
            for index_j, piece in enumerate(row):
                pygame.draw.rect(
                    self.screen,
                    self.WHITE,
                    (
                        index_j * self.GRID_SIZE,
                        index_i * self.GRID_SIZE,
                        self.GRID_SIZE,
                        self.GRID_SIZE,
                    ),
                )

        self.draw_grid()
        self.draw_pieces(matrix)
        pygame.display.flip()

    def updateImage(self) -> None:
        """
        Update the image.

        This method prepares Pygame if it is not ready and then shows the image.

        Args:
            - None

        Returns:
            - None: This method does not return any value.

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        if self.pygameNotReady:
            self.preparePygame()
            self.pygameNotReady = False

        self.showImage()
